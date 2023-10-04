"""This module contains the game logic like methods"""
import random
from Role1 import Pizza

def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2
    print("You rolled " + str(sum))   
    return sum

