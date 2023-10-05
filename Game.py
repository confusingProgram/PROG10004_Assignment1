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
    elif c2._role == "mc": #Mail Courier 
        print("Nothing") # Where the cutscene for the mail courier will go.

print('                                        Chapter 1: Canada Post')
print( '                                    * Mail Courier arrives at Canada Post*'          )
print('                                            *DING DING *        ')
print('                                                    *Door Opens ')
print(                              "Good morning! Have you got any boxes for me to deliver?")
print(          'Boss: "Good morning '+ c2.name +', I have the boxes right here."')
print(              'Boss: "You have to deleiver it to House number 123 on That Street"')
print(              'Boss:"But be carefull, these boxes are heavy "' )
print(                                 'Ok Boss! I got this!!!')
print('                                             Objective: Deliver the Boxes!!!')
print('                I hope that this delivery goes smoothly')
print(  'Hmmmm... Which vehicle should I take?  ')
print("You could choose to deliver the boxes in your van; a customer's car; or motorbike")

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

def chapter_1_challenge(c2):
    if c2._role =="mc": #mail courier 
        option = 0
        while True: # Selection loop
            op1 = "Use your van to deliver mail"
            op2 = "Use a Customer's car to deliver mail"
            op3 = "Use a motocycle to deliver mail"
            op = ""
            print("Options:") # Displays options
            print("1 [STR]. " + op1 + ".")
            print("2 [DEX]. " + op2 + ".")
            print("3 [IQ]. " +  op3 + ".")

            while True: # Choosing options loop
                options = input("Type in 1, 2, or 3: ")
                if option == "1" or option == "2" or option == "3":
                    break # If user selects a valid option, then options loop will exit
                else:
                    print("Error, invalid answer.")

            while True: #Confrim loop
                choice = input("Are you sure you want to " +op + "?  Yes or No: ")
                if choice == "Yes" or choice == "No":
                    break # If user says Yes or No, confirm loop will exit
                else:
                    print("Error, invalid answer.")
            
            if choice == "Yes":
                print("You have chosen to: " + op + ".")
                break # If user said yes, selection loop will exit.
        
        print("Alright, Let's start the challenge!!")
        
    elif c2._role == "mc": #Challenge 1 for Mail Courier
         if option == "1":
            print("Carry the boxes to your van car requires a roll of 8 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c2._str)
            if num > 10: #11-12
                print("Critical win! The boxes are not that heavy and you can tell that your workout paid off! +1 strength!")
                c2.challenge_result(1, 1)
                c2.mod_stat(str, 1)
            elif num > 5: #6-10
                print("Win! you had a bit of troblue but you got it, you put the boxes in the van and you're off to the journey!")
                c2.challenge_result(1, 1)
            elif num > 3: #4-5
                print("Lose! The boxes you carried a a lot heavier than you thought, maybe you do need those gym sessions!")
                c2.challenge_result(1, 0)
            else: #2-3
                print("Critical lose! What is inside these boxes?! You almost drop the boxes, howvere your boss saw you and came to help you. -1 Strength.")
                c2.challenge_result(1, 0)
                c2.mod_stat(str, -1)
         elif option == "2":
            print("Using a customer's car requires a roll of 2 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c2._dex)
            if num > 10: #11-12
                print("Critical win! WoW that customer lend you their car? This is going to be quick! +1 Dexterity")
                c2.challenge_result(1, 1)
                c2.mod_stat(dex, 1)
            elif num > 3: #4-10
                print("Win! The customer didn't trust to but gave you their car anyway .")
                c2.challenge_result(1, 1)
            elif num > 2: #3
                print("Lose! You didn't get the car and the customer ran over your foot! Ouch!! Thats got to hurt.")
                c2.challenge_result(1, 0)
            else: #2
                print("Critical lose! You got into a car accident as soon as you got in the car")
                print( "The customer was really mad! Sigh! you are gonna pay for that! -1 Dexterity.")
                c2.challenge_result(1, 0)
                c2.mod_stat(dex, -1)
    elif option == "3":
            print("Using a motorbike requires a roll of 6 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c2._iq)
            if num > 10: #11-12
                print("Critical win! Hmm, I guess you're going to be delivering these boxes in no time!. +1 Intelligence")
                c2.challenge_result(1, 1)
                c2.mod_stat(iq, 1)
            elif num > 7: #8-10
                print("Win! Just hope that there is no traffic, that would suck!.")
                c2.challenge_result(1, 1)
            elif num > 3: #4-7
                print("Lose! Not the most convincing argument I've heard recently.")
                c2.challenge_result(1, 0)
            else: #2-3
                print("You left the motorbike unattended and running, someone stole it! I mean who does that!!. -1 Intelligence.")
                c2.challenge_result(1, 0)
                c2.mod_stat(iq, -1)
    print('                                                 *This Ends Chapter 1*')

#Chapter 1 finished
