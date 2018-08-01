### Monty Hall Game


from datascience import *
import numpy as np

doors = make_array(1,2,3)
prizes = make_array('goat 1','goat 2', 'car')

def setup():
    return Table().with_columns(
    'door', doors,
    'prize', np.random.choice(prizes,size = 3, replace = False)
    )

def behind_door(game, door_no):
    return game.where('door', door_no).column('prize').item(0)
def find_door(game,prize):
    return game.where('prize', prize).column('door').item(0)
def find_other_door(game,guessed,exposed):
    return (1 + 2 + 3) - guessed - exposed

def expose(game,door):
    if behind_door(game,door) == 'car':
        return np.random.choice(make_array(find_door(game,'goat 1'),find_door(game,'goat 2')))
    elif behind_door(game,door) == 'goat 1':
        return find_door(game,'goat 2')
    else:
        return find_door(game,'goat 1')

def game_play1():
    game_board = setup()
    choose_door = int(input('select a door: '))
    other_door = expose(game_board,choose_door)
    prize_behind_other_door = behind_door(game_board,other_door)
    print('other door is',other_door,'and prize behind other door is',prize_behind_other_door)
    print()
    question = input('do you want to change the door ? y/n')
    print()
    if question == 'n' or question == 'N':
        print('door you choose is',choose_door)
        result = behind_door(game_board,choose_door)
    elif question == 'y' or question == 'Y':
        print('door you choose is',other_door)
        result = behind_door(game_board,find_other_door(game_board,choose_door,other_door))
    print()
    print(game_board)
    return result

def game_play():
    t = game_play1()
    if t == 'car':
        return '***** congrats you got a car *****'
    else:
        return 'you lose, try again'

output = game_play()
print(output)