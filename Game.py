"""This module contains the game logic like methods"""
import random
from Role1 import Pizza

def roll_dice(stat): #stat = c1._str for example
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2 + stat
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
    if c1._role == "pd": #Challenge 1 for Pizza Driver
        option = ""
        while True: # Selection loop
            op1 = "carry pizzas to the car" # requires 6 strength, +1 strength if 11-12, -1 strength on loss if 2-3
            op2 = "use a cart to bring the pizzas" # requires 4 dexterity to pass, +1 dexterity if 11-12, -1 charisma on loss if 2-3
            op3 = "persuade your boss to carry them" # requires 8 charisma to pass, +1 charisma if 11-12, -1 charisma on loss if 3-4
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
        if option == "1":
            print("Carrying the pizzas to the car requires 6 strength to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c1._str)
            if num > 10: #11-12
                print("Critical win! The pizzas and wings feel as light as paper, and you feel even stronger! +1 strength!")
                c1.challenge_result(1, 1)
                c1.mod_stat(str, 1)
            elif num > 5: #6-10
                print("Win! With some trouble, but not too much trouble, you put the order into the car, and you're on your way.")
                c1.challenge_result(1, 1)
            elif num > 3: #4-5
                print("Lose! The food turns out to be a little heavier than you would've thought, and you stumble and hit your elbow on your way out.")
                c1.challenge_result(1, 0)
            else: #2-3
                print("Critical lose! Are these pizzas actually pizzas, or cinder blocks?! You fall and drop the food, but luckily nothing spills. -1 Strength")
                c1.challenge_result(1, 0)
                c1.mod_stat(str, -1)
    if c1._role == "mc": #challenge 1 for Mail Courier
        print()

#Chapter 1 finished

