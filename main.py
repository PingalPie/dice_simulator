import random

def dice():
    num = random.randint(1, 6)
    guess = int(input('Guess the number - '))
    if guess == int(num):
        print('Your answer is right')
        redo = int(input('If you want to play again press 1 and enter - '))
        if redo == 1:
            dice()
    else:
        print(num, 'was the number')
        redo_else = int(input('Sorry to tell you that you lost the round press 1 to replay - '))
        if redo_else == 1:
            dice()

dice()
