import random


def game(comp, player):
    if comp == 'scissor':
        if player == 'paper':
            return False
        elif player == 'stone':
            return True
    elif comp == 'paper':
        if player == 'scissor':
            return True
        elif player == 'stone':
            return False
    elif comp == 'stone':
        if player == 'paper':
            return True
        elif player == 'scissor':
            return False
    elif comp == player:
        return None


round = 1
win = 0
while (round < 4):
    print(f'\n##### ROUND {round} #####')
    round += 1
    comp = print('Its computer turn. Choose (Stone), (Paper) or (Scissor).')
    rand = random.randint(1, 3)
    if rand == 1:
        comp = 'stone'
    elif rand == 2:
        comp = 'paper'
    elif rand == 3:
        comp = 'scissor'

    print('Computer choose!!!!')
    # print(f'computer choose: {comp}')
    player = input('Your turn: Choose(stone), (paper) or (scissor): ')
    a = game(comp, player)
    print(f'Computer choose "{comp}" and you choose "{player}".')

    if a == True:
        win += 1
    print(f'You win {win} rounds out of 3.')

if win == 2 or win == 3:
    print(f'Congratulation, You win.\nYou win {win} rounds out of 3.')
else:
    print(f'Sorry,You loose.\nYou only win {win} round out of 3.')