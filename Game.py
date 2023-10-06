"""This module contains the game logic such as methods."""
import random

def roll_dice(stat): #stat = pd._str for example
    """This function will randomly pick integers ranging from 1 to 6 (inclusive), 
    and add that sum to the stat modifier (ranging from -2 to +2), then print the result."""
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2 + stat
    print("You rolled " + str(sum) + "!")   
    return sum
