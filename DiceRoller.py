''' The intent for this project is to simulate a dice roll.  W
When the program runs, it will randomly choose a number between 1 and 6.
The program will then print what that number is.  It will then ask
If you'd like to roll again.  This program uses while loops, random
functions, integers, and print.'''

import random
from sys import exit

def DiceRoll():
    roll_dice = str(random.randint(1,6))

    print(f'You rolled a {roll_dice}, would you like to roll again?')

    answer = input("> ")
    if "yes" in answer:
        DiceRoll()
    else:
        exit()

DiceRoll()
