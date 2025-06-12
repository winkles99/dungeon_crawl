# dice.py

import random

def roll_d20():
    return random.randint(1, 20)

def roll_d6():
    return random.randint(1, 6)

def roll_dice(sides):
    return random.randint(1, sides)
