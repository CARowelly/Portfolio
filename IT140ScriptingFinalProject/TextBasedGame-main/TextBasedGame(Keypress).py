from pynput import keyboard
from pynput.keyboard import Key, Listener
import Project2Text

# a dictionary linking a room to other rooms

rooms = {
    'Atrium': {
        Key.left: 'Courtyard'  # exit
    },
    'Courtyard': {
        Key.left: 'Great Hall', Key.right: 'Atrium'
    },
    'Great Hall': {
        Key.left: 'Arboretum', Key.up: 'Laboratory', Key.right: 'Courtyard'
    },
    'Arboretum': {
        Key.right: 'Great Hall'
    },
    'Laboratory': {
        Key.left: 'Library', Key.down: 'Great Hall'
    },
    'Library': {
        Key.up: 'Antechamber', Key.right: 'Laboratory'
    },
    'Antechamber': {
        Key.right: 'Inner Sanctum', Key.down: 'Library'
    },
    'Inner Sanctum': {
        Key.left: 'Antechamber'
    },
}

# dictionary of items and rooms that contain items

items = {'Courtyard': 'the base of a small leather box', 'Great Hall': 'scroll', 'Arboretum': 'scroll',
         'Laboratory': 'scroll', 'Library': 'scroll', 'Antechamber': 'the top of a small leather box'}

# start the player in the Atrium with no items
SCROLL = False
PHYLACTERY = 0
current_room = 'Atrium'
answer = ''

Project2Text.intro()


def instructions():
    # game instructions able to be referenced by typing help
    if current_room == 'Atrium':
        print('\nCommands: up arrow = Go up, left arrow = Go left, down arrow = Go down, right arrow = Go right \n'
              'f = Pick up item, i = Location and Inventory, m = Map, esc = Exit')
    else:
        print('\nCommands: up arrow = Go up, left arrow = Go left, down arrow = Go down, right arrow = Go right\n'
              'f = Pick up item, i= Location and Inventory, m = Map')


instructions()


def show_status():
    # prints the player's current location and inventory
    print('\nYou\'re in the {}.'.format(current_room),
          '\nYour satchel contains {} pieces of the phylactery.'.format(str(PHYLACTERY)))


def inventory():
    # allows player to pick up items and store them in their inventory
    global SCROLL
    global PHYLACTERY
    if current_room in items:
        if items[current_room] == 'scroll' and SCROLL is False:
            print('\nYou pick up the {}'.format(items[current_room]), 'and place it in your satchel.')
            SCROLL = True
        elif items[current_room] == 'scroll' and SCROLL is True:
            print('\nYou pick up another {}'.format(items[current_room]), 'and place it in your satchel.')
        else:
            print('\nYou pick up the {}'.format(items[current_room]), 'and place it in your satchel.')
        PHYLACTERY += 1
        del items[current_room]
        if PHYLACTERY == 6:
            print('\nCongratulations! You have assembled the Lich\'s Phylactery.\n'
                  'Enter its Inner Sanctum and burn the artifact at the altar to\n'
                  'send the monster\'s wretched soul to the Abyss.')
    else:
        print('\nYou find nothing.')


def game_text():
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


def win_or_lose():
    if current_room == 'Inner Sanctum' and PHYLACTERY < 6:
        # checks for lose condition
        Project2Text.inner_sanctum_lose()
        exit()
    elif current_room == 'Inner Sanctum' and PHYLACTERY == 6:
        # checks for win condition
        Project2Text.inner_sanctum_win()
        yes_or_no()


def yes_or_no():
    input('yes or no: ')  # gives player choice to end game or continue to explore
    if answer.lower() == 'yes':
        # endgame win condition
        Project2Text.end_game()
        exit()
    elif answer.lower() == 'no':
        # sends player back to Antechamber to continue navigating the tower
        print('\nYou back out of the room and the flame subsides for now.\n'
              'The Lich continues its wretched existence, writhing on the floor, too weak to stand.')
        check_key(Key.left)
    elif answer.lower() != 'yes' or answer.lower() != 'no':
        # input validation
        print('\nYou cannot do that, enter ')
        yes_or_no()


# The currently active modifiers
current = set()


def execute():
    print("Do Something")


def on_press(key):
    # print('{0} pressed'.format(key)fff)
    check_key(key)


def on_release(key):
    # print('{0} release'.format(
    # key))
    if key == Key.esc and current_room == 'Atrium':
        # Stop listener
        return False
    elif key == Key.esc and current_room != 'Atrium':
        print('You must return to the Atrium to exit the Tower.')


def check_key(key):
    global current_room
    global answer
    next_room = rooms[current_room]
    if key in [Key.up, Key.down, Key.left, Key.right]:
        if key in rooms[current_room]:
            current_room = next_room[key]
            game_text()
            win_or_lose()
            print('\nFor a list of commands, press \"c\"', '\n', '-' * 20)
        else:
            print('Wrong way!')
    elif key == keyboard.KeyCode(char='c'):
        instructions()
    elif key == keyboard.KeyCode(char='f'):
        inventory()
    elif key == keyboard.KeyCode(char='i'):
        show_status()
    elif key == keyboard.KeyCode(char='m'):
        Project2Text.game_map()
    else:  # key not in commands
        print('You cannot do that!')


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
