"""This module contains the game logic like methods"""
import random
from Role1 import Pizza

def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2
    print("You rolled " + str(sum))   
    return sum

#Chapter 1
def chapter_1_cutscene(c1): #c1 is the character
    if c1._role == "pd": #Pizza Driver
        print('                                 *Chapter 1: The Pizza Shop*')
        print('                                         *RING RING RING*                                ')
        print('                                             *KERCHUNK*                                      ')
        print('Boss: "Hello, welcome to Supernova Pizza, how can I help you?"')
        print('''      "..Uh huh... Uh huh... Got it, we'll have your order there in no time. Goodbye."''')
        print('                                             *KERCHUNK*                                      ')
        print('Boss: "Alright ' + c1._name + ', we got a new order for 123 Somewhere Street."')
        print('      "The order is 3 pepperoni pizzas, and 12 pc. wings. We have some already. Go load them into your car."')
        print('      "You better show these customers that Supernova Pizza is the fastest restaurant around!"')
        print('      "And no slacking! Last time, I had a customer complain that their pizza was so cold, it could cool their drinks!"')
        print()
        print('                                     Objective: Load the order')
        print('Gee, he sure sounds angry!')
        print('Now... how to load the pizzas into the car?')
        print("""You could try simply carrying out the pizzas to your car; use a cart; or you're feeling adventurous, persuade your boss.""")
    elif c1._role == "mc":
        print("Nothing") # Where the cutscene for the mail courier will go.

def chapter_1_challenge(c1): #c1 is the character:
    if c1._role == "pd": #Pizza Driver
        print("Nothing")# Where the challenge for pizza driver will go