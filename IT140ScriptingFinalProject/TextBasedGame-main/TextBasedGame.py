# Project 2 Text Adventure Game

# Craig Rowell

import Project2Text

# a dictionary linking a room to other rooms

rooms = {
    'Atrium': {
        'a': 'Courtyard'  # exit
    },
    'Courtyard': {
        'a': 'Great Hall', 'd': 'Atrium'
    },
    'Great Hall': {
        'a': 'Arboretum', 'w': 'Laboratory', 'd': 'Courtyard'
    },
    'Arboretum': {
        'd': 'Great Hall'
    },
    'Laboratory': {
        'a': 'Library', 's': 'Great Hall'
    },
    'Library': {
        'w': 'Antechamber', 'd': 'Laboratory'
    },
    'Antechamber': {
        'd': 'Inner Sanctum', 's': 'Library'
    },
    'Inner Sanctum': {
        'a': 'Antechamber'
    },
}

# dictionary of items and rooms that contain items

items = {'Courtyard': 'the base of a small leather box', 'Great Hall': 'scroll', 'Arboretum': 'scroll',
         'Laboratory': 'scroll', 'Library': 'scroll', 'Antechamber': 'the top of a small leather box'}

# start the player in the Atrium with no items
SCROLL = False
PHYLACTERY = 0
room = 'Atrium'


# a list of the four movement keys
directions = ['w', 'a', 's', 'd']


Project2Text.intro()


def instructions(current_room):
    # game instructions able to be referenced by typing help
    if current_room == 'Atrium':
        print('\nCommands: w = Go up, a = Go left, s = Go down, d = Go right \n'
              'f = Pick up item, z = Location and Inventory m = Map, x = Exit')
    else:
        print('\nCommands: w = Go up, a = Go left, s = Go down, d = Go right\n'
              'f = Pick up item, z = Location and Inventory, m = Map')


instructions(room)


def show_status(current_room):
    # prints the player's current location and inventory
    print('\nYou\'re in the {}.'.format(current_room),
          '\nYou have {} pieces of the phylactery.'.format(str(PHYLACTERY)))


def inventory(current_room):
    # allows player to pick up items and store them in their inventory
    global SCROLL
    global PHYLACTERY
    if current_room in items:
        if items[current_room] == 'scroll' and SCROLL is False:
            print('\nYou have found a {}'.format(items[current_room]), 'in the {}'.format(current_room))
            SCROLL = True
        elif items[current_room] == 'scroll' and SCROLL is True:
            print('\nYou have found another {}'.format(items[current_room]), 'in the {}'.format(current_room))
        else:
            print('\nYou have found {}'.format(items[current_room]), 'in the {}'.format(current_room))
        PHYLACTERY += 1
        del items[current_room]
        if PHYLACTERY == 6:
            print('\nCongratulations! You have assembled the Lich\'s Phylactery.\n'
                  'Enter its Inner Sanctum and burn the artifact at the altar to\n'
                  'send the monster\'s wretched soul to the Abyss.')
    else:
        print('\nYou find nothing.')


def game_text(current_room):
    if current_room == 'Atrium':
        Project2Text.atrium()  # text for atrium
    elif current_room == 'Courtyard':
        Project2Text.courtyard()  # text for courtyard
    elif current_room == 'Great Hall':
        Project2Text.great_hall()  # text for great hall
    elif current_room == 'Arboretum':
        Project2Text.arboretum()  # text for arboretum
    elif current_room == 'Laboratory':
        Project2Text.laboratory()  # text for laboratory
    elif current_room == 'Library':
        Project2Text.library()  # text for library
    elif current_room == 'Antechamber':
        Project2Text.antechamber()  # text for antechamber
    if current_room in items:
        Project2Text.room_item(current_room)  # text for item present in room


def win_or_lose(current_room):
    if current_room == 'Inner Sanctum' and PHYLACTERY < 6:
        # checks for lose condition
        Project2Text.inner_sanctum_lose()
        exit()
    elif current_room == 'Inner Sanctum' and PHYLACTERY == 6:
        # checks for win condition
        Project2Text.inner_sanctum_win()
        yes_or_no()


def yes_or_no():
    answer = input('Yes or No: ')  # gives player choice to end game or continue to explore
    if answer.lower() == 'yes':
        # endgame win condition
        Project2Text.end_game()
        exit()
    elif answer.lower() == 'no':
        # sends player back to Antechamber to continue navigating the tower
        print('\nYou back out of the room and the flame subsides for now.\n'
              'The Lich continues its wretched existence, writhing on the floor, too weak to stand.')
        main(current_room='Antechamber')
    else:
        # input validation
        print('\nYou cannot do that, enter ')
        yes_or_no()


def main(current_room):
    # allows player to input commands
    while True:
        # loops forever
        win_or_lose(current_room)  # checks for win or lose conditions
        next_room = rooms[current_room]  # sets next room equal to rooms adjoining current room
        print('For a list of commands, press \"c\"', '\n', '-' * 20)
        command = input('Enter your command: ')  # takes player input commands
        if command.lower() == 'c':
            # displays main menu and list of commands
            instructions(current_room)
        elif command.lower() == 'z':
            # sets command to show status menu
            show_status(current_room)
        elif command.lower() == 'f':
            # sets command to pick up item
            inventory(current_room)
        elif command.lower() == 'm':
            # sets command to show map
            Project2Text.game_map()
        elif command.lower() == 'x' and current_room == 'Atrium':
            # if command is set to 'x' and player is in Atrium'
            # ends the game
            print('\nGoodbye!')
            exit()
        elif command.lower() == 'x' and current_room != 'Atrium':
            # input validation for exit room when player is not in the Atrium
            print('\nYou must return to the Atrium to exit the Tower.')
        elif command.lower() in directions:
            if command.lower() in rooms[current_room]:
                # checks for valid direction and moves player to next room if true
                current_room = next_room[command.lower()]
                print('You have entered the {}.'.format(current_room))
                game_text(current_room)
            else:
                # input validation for wrong direction
                print('\nYou cannot go that way!')
        else:
            # input validation for invalid commands
            print('\nYou cannot do that!')


main(room)
