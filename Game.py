"""This module contains the game logic like methods"""
import random
from Role1 import Pizza
from Role2 import Mail

def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2
    print("You rolled " + str(sum))   
    return sum

  
#Chapter 1
def chapter_1_cutscene(c1): #c1 is the character
    """This method contains the game cutscene for Chapter 1 for both roles"""
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
        print('Gee, they sure sounds angry!')
        print('Now... how to load the pizzas into the car?')
        print("""You could try simply carrying out the pizzas to your car; use a cart; or you're feeling adventurous, persuade your boss to carry them.""")
    elif c1._role == "mc":
        print("Nothing") # Where the cutscene for the mail courier will go.

def chapter_1_challenge(c1): #c1 is the character:
    if c1._role == "pd": #Pizza Driver
        option = 0
        while True: # Selection loop
            op1 = "carry pizzas to the car"
            op2 = "use a cart to bring the pizzas"
            op3 = "persuade your boss to carry them"
            op = ""
            print("Options:") # Displays options
            print("1 [STR]. " + op1 + ".")
            print("2 [DEX]. " + op2 + ".")
            print("3 [CHR]. " + op3 + ".")

            while True: # Choosing options loop
                option = input("Type in 1, 2, or 3: ")
                if option == "1" or option == "2" or option == "3":
                    break # If user selects a valid option, options loop will exit
                else:
                    print("Error, invalid answer.")

            while True: #Confirmation loop
                choice = input("Are you sure you want to " +op + "?  Yes or No: ")
                if choice == "Yes" or choice == "No":
                    break # If user says Yes or No, confirmation loop will exit
                else:
                    print("Error, invalid answer.")
            
            if choice == "Yes":
                print("You have chosen to: " + op + ".")
                break # If user said yes, selection loop will exit.
        
        print("Let's get into the challenge.")



