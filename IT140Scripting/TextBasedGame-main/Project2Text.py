# this file contains multiline text for TextBasedGame.py, in order to save space and keep code more readable

def intro():
    print('The Lich\'s Tower Text Adventure Game\n Welcome to the Lich\'s Tower.\n'
          'The grounds are encircled by a thick, crenellated wall.\n'
          'You have entered an atrium through the main gate.\n'
          'To the north, past the tower grounds, you see the main entrance to the tower itself.')


def atrium():
    # atrium text
    print('\nYou return to the small guard post by which you traversed the outer wall.\n'
          'There is little of note here save a means of egress. Do you wish to leave?')


def courtyard():
    # courtyard text
    print('\nYou stand in a wide courtyard. Looming over you are the massive doors of the main building,\n'
          'a stark 3-story stone structure. The doors to the Great Hall stand slightly ajar,\n'
          'just enough for you to squeeze through.')


def great_hall():
    # great hall text
    print('\nThe main body of the ground floor is a dark, cold great hall.\n'
          'A giant marble hearth lays neglected on the west wall,\n'
          'containing the remnants of soot and ash from a long-dead fire.\n'
          'To the east, a spiral staircase wraps up the outer walls, leading to the floors above.\n'
          'The north wall is one giant pane of dusty stained glass. At the center, a wrought-iron trellis serves\n'
          'as an entrance to the enclosed arboretum beyond.')


def arboretum():
    # arboretum text
    print('\nThe arboretum is a finely crafted glass structure, almost as tall as the tower itself.\n'
          'It is overgrown with long-dead, dried up brambles. Left unattended, the blackened, rotting trees\n'
          'have grown through the glass panes in places creating a draft.')


def laboratory():
    # laboratory text
    print('\nYou enter a small laboratory adjoining the library via a short corridor.\n'
          'A workbench that has clearly been used for vile purposes rests on the east wall,\n'
          'covered with the tools and ingredients for making poisons and unholy elixirs.')


def library():
    # library text
    print('\nNext to the laboratory the space opens up into an larger room, covered from wall to wall\n'
          'in bookshelves containing volumes upon volumes of books, manuscripts, tomes, manuals, and handbooks.\n'
          'The spiral staircase continues up around the inner wall of the tower through an entrance on the North wall.')


def antechamber():
    # antechamber text
    print('\nThe top of the stairs lead to an antechamber where soldiers once stood guard over their liege.\n'
          'Fancily carved wooden doors on the south wall lead to the vile lich\'s inner sanctum.')


def room_item(current_room):
    if current_room == 'Courtyard':
        print('\nYou spot the base of a small leather box laying on its side.')
    elif current_room == 'Great Hall':
        print('\nYou see the corner of a piece of vellum sticking out in sharp contrast to the blackened logs.\n'
              'It is surely one of the scrolls that belong to the phylactery.')
    elif current_room == 'Arboretum':
        print('\nYou hear the flutter of paper amongst the rustling of dead leaves.\n'
              'A dust devil whirls in the corner, a parchment spinning amidst the other debris.\n'
              'It must be one of the scrolls.')
    elif current_room == 'Laboratory':
        print('\nAmidst various vials of ominous looking liquids on the workbench,\n'
              'you see a spoon coated in a viscous substance.\n'
              'Stuck to that spoon is a sheet of papyrus that can only be one of the scrolls you seek.')
    elif current_room == 'Library':
        print('\nAfter poring over page after page in book after book, you finally come across a bookfell\n'
              'that resembles the scrolls you are after')
    elif current_room == 'Antechamber':
        print('\nA filigreed leather box top with a leather strap and buckle riveted to the center lays abandoned\n'
              'in the corner of the room.')


def inner_sanctum_win():
    # win text
    print('\nYou behold the Lich guarding a blazing altar in its circle of power\n'
          'The assembled phylactery begins to glow as it absorbs the villain\'s soul!\n'
          'You see the circle of power encasing the Lich and altar begin to fade as it dematerializes.\n'
          'The altar\'s flame erupts into a conflagration! Do you cast the phylactery into the fire?')


def end_game():
    # endgame text
    print('\nYou cast the phylactery into the altar\'s blue-blazing flame and it bursts with a corona of white light\n'
          'The Lich is incinerated in holy flame as its soul is banished to the Abyss to suffer for eternity.\n'
          'Congratulations! You have destroyed the abomination and freed the tower from its evil grasp.')


def inner_sanctum_lose():
    # lose text
    print('\nYou behold the Lich guarding a blazing altar in its circle of power!\n'
          'Without the assembled phylactery, you are unable to banish its soul to the Abyss.\n'
          'It utters a single word in a raspy, guttural voice and you fall helpless on the floor.\n'
          'You feel your life essence being drained as the creature feasts upon your soul.\n'
          'The world goes dark. You have been vanquished.')


def game_map():
    print('<-North  □-□      Antechamber: Inner Sanctum\n'
          '         S |\n'     
          '         □-□      Library: Laboratory\n'
          '         | S\n'
          '       □-□-□-□-□  Arboretum: Great Hall: Courtyard: Atrium\n')
