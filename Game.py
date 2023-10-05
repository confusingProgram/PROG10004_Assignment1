"""This module contains the game logic like methods"""
import random
from Role1 import Pizza
from Role2 import Mail


def roll_dice(stat): #stat = c1._str for example
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2 + stat
    print("You rolled " + str(sum) + "!")   
    return sum

  
#Chapter 1
def chapter_1_cutscene(c1): #c1 is the character
    """This method contains the game cutscene for Chapter 1 for both roles"""
    if c1._role == "pd": #Pizza Driver
        print('                                    *Chapter 1: The Pizza Shop*')
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
            
            print("Options:") # Displays options
            print("1 [STR]. " + op1 + ".")
            print("2 [DEX]. " + op2 + ".")
            print("3 [CHR]. " + op3 + ".")

            while True: # Choosing options loop
                option = input("Type in 1, 2, or 3: ")
                if option == "1":
                    op = op1
                    break # If user selects a valid option, options loop will exit
                elif option == "2":
                    op = op2
                    break
                elif option == "3":
                    op = op3
                    break
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
            print("Carrying the pizzas to the car requires a roll of 6 to complete.")
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
                print("Critical lose! Are these pizzas actually pizzas, or cinder blocks?! You fall and drop the food, but luckily nothing spills. -1 Strength.")
                c1.challenge_result(1, 0)
                c1.mod_stat(str, -1)
        elif option == "2":
            print("Using a cart to bring the pizzas requires a roll of 4 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c1._dex)
            if num > 10: #11-12
                print("Critical win! Why work hard when you can just handle a cart instead? Piece of cake! +1 Dexterity")
                c1.challenge_result(1, 1)
                c1.mod_stat(dex, 1)
            elif num > 3: #4-10
                print("Win! Sure is handy having this cart around.")
                c1.challenge_result(1, 1)
            elif num > 2: #3
                print("Lose! What on earth? One of the back wheels on the cart came undone. That's coming out of your paycheque.")
                c1.challenge_result(1, 0)
            else: #2
                print("Critical lose! Hastily, you run with the cart, but lose control and smash your hand into the door frame! Yowch!! -1 Dexterity.")
                c1.challenge_result(1, 0)
                c1.mod_stat(dex, -1)
        elif option == "3":
            print("Persuading your boss to carry them requires a roll of 8 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c1._chr)
            if num > 10: #11-12
                print('Boss: "Hey! What are you standing around for?!"')
                print(c1._name + ': "Boss, can you carry the pizzas for me? I uhhh, really need to use the bathroom, like really really badly."')
                print('Boss: "..."')
                print('      "Fine, but make it quick!"')
                print("Critical win! Huh, guess you're doing even less work. +1 Charisma")
                c1.challenge_result(1, 1)
                c1.mod_stat(chr, 1)
            elif num > 7: #8-10
                print('                                         *SNAP SNAP SNAP*                                ')
                print('Boss: "Hey! Are you even listening?!"')
                print('      "Geez, do I have to do everything myself?!"')
                print('       *GRUMBLES*') 
                print("Win! And you didn't even say anything.")
                c1.challenge_result(1, 1)
            elif num > 3: #4-7
                print(c1._name + ': "Boss, can you carry the pizzas for me? I uhhh, forgot how to walk."')
                print('Boss: "What do you mean you forgot how to walk? Just do your job!"')
                print("Lose! Not the most convincing argument I've heard recently.")
                c1.challenge_result(1, 0)
            else: #2-3
                print(c1._name + ''': "Boss, can you carry the pizzas for me? I'll do you a favour."''')
                print('       *WINK*')
                print('Boss: "..."')
                print('      "How about you do me this favour, and carry the darn order to the car?!"')
                print("Critical lose! Very daring to ask your boss a favour when you're already on their bad side. -1 Charisma.")
                c1.challenge_result(1, 0)
                c1.mod_stat(chr, -1)
    elif c1._role == "mc": #challenge 1 for Mail Courier
        print()
    print('                                                 *End of Chapter 1*')


#Chapter 1 finished

def chapter_2_cutscene(c1): #c1 is the character
    if c1._role == "pd": #pizza driver
        print('                                    *Chapter 2: On The Road*')
        print("You are driving down a road on your way to 123 Somewhere Street.")
        print(c1._name + ': "..."')
        print('       *SQUINTS*')
        print('      "What is that?"')
        print("It is an imposing boulder, impeding your path!")
        print(c1._name + ': "I should probably pull over."')
        print('                                     *SCREEEEEEEEEEEECH*                                ')
        print('''Passerby: "Wow, that is a large boulder. I hope you don't plan on asking me for help."''')
        print('                                     Objective: Move the boulder')
        print("Who just leaves a boulder in the middle of a road? An urban one at that. Where did this come from?")
        print("The boulder is propped up against another large rock, but you can drive around that one if you can move the large boulder first.")
        print("How on earth are you going to move the boulder?")
        print("You could try pushing it yourself; using a sturdy tree branch to use it as a lever; or smooth-talk the passerby in helping.")

    elif c1._role == "mc": # mail courier
        print()
        
def chapter_2_challenge(c1):
    if c1._role == "pd": #pizza driver
        option = ""
        while True: # Selection loop
            op1 = "push it yourself" # requires 8 strength, +1 strength if 11-12, -1 strength on loss if 3-4
            op2 = "use a tree branch as a lever" # requires 5 dexterity to pass, +1 dexterity if 11-12, -1 charisma on loss if 2-3
            op3 = "smooth-talk the passerby" # requires 6 charisma to pass, +1 charisma if 11-12, -1 charisma on loss if 2-3
            
            print("Options:") # Displays options
            print("1 [STR]. " + op1 + ".")
            print("2 [DEX]. " + op2 + ".")
            print("3 [CHR]. " + op3 + ".")

            while True: # Choosing options loop
                option = input("Type in 1, 2, or 3: ")
                if option == "1":
                    op = op1
                    break # If user selects a valid option, options loop will exit
                elif option == "2":
                    op = op2
                    break
                elif option == "3":
                    op = op3
                    break
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
            print("Pushing it yourself requires a roll of 8 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c1._str)
            if num > 10: #11-12
                print("Critical win! Woah, do you go to the gym?! That boulder basically moved itself! +1 strength!")
                c1.challenge_result(2, 1)
                c1.mod_stat(str, 1)
            elif num > 7: #8-10
                print("Win! It's pretty heavy, but you're able to manage and roll the boulder out.")
                c1.challenge_result(2, 1)
            elif num > 3: #4-7
                print("Lose! The boulder's too heavy. Now you're too tired to move it in any way. Time to find a different route.")
                c1.challenge_result(2, 0)
            else: #2-3
                print("Critical lose! You push and push and it does not budge. You also pull 3 different muscles in the process. -1 Strength.")
                c1.challenge_result(2, 0)
                c1.mod_stat(str, -1)
        elif option == "2":
            print("Using a tree branch as a lever requires a roll of 5 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c1._dex)
            if num > 10: #11-12
                print("Critical win! Is this a measure of dexterity or intellect? Either way, better than brute force. +1 Dexterity")
                c1.challenge_result(2, 1)
                c1.mod_stat(dex, 1)
            elif num > 4: #5-10
                print("Win! Good thing this is an oak branch, and not balsa.")
                c1.challenge_result(2, 1)
            elif num > 2: #3-4
                print("Lose! The boulder is somehow put in an even worse position, before the branch breaks. Now you really can't move it.")
                c1.challenge_result(2, 0)
            else: #2
                print("Critical lose! The branch becomes dislodged and breaks as it fractures your wrist. You didn't need that right? -1 Dexterity.")
                c1.challenge_result(2, 0)
                c1.mod_stat(dex, -1)
        elif option == "3":
            print("Smooth-talking the passerby requires a roll of 6 to complete.")
            input("Press Enter to roll the dice.")
            num = roll_dice(c1._chr)
            if num > 10: #11-12
                print(c1._name + ': "Hey, do you wanna help me push the boulder?"')
                print('Passerby: "Uh, no. It looks really heavy."')
                print(c1._name + ''': "Come on! Don't you wanna say that you've pushed a boulder?"''')
                print('Passerby: "..."')
                print('      "You make a convincing argument. Alright."')
                print("Critical win! It does sound cool to say that you've moved a big boulder! +1 Charisma")
                c1.challenge_result(2, 1)
                c1.mod_stat(chr, 1)
            elif num > 5: #6-10
                print(c1._name + ': "Actually, can you help me push the boulder?"')
                print('''Passerby: "What's in it for me? The boulder isn't my problem."''')
                print(c1._name + ': "I could give you a buy-one-get-one free pizza coupon...?"')
                print('''Passerby: "I do like pizza. Alright then, let's get to it."''')
                print("Win! An extra customer! Your boss will be quite pleased.")
                c1.challenge_result(2, 1)
            elif num > 3: #4-5
                print(c1._name + ''': "Could you help me with the boulder? It's really heavy. And geez, it could crush one of us."''')
                print('''Passerby: "That makes me wanna move it even less. You're on your own."''')
                print("You try moving the boulder by yourself but it seems to gotten 8 times heavier after the passerby leaves!")
                print("Lose! Why did it get heavier after they left??")
                c1.challenge_result(2, 0)
            else: #2-3
                print(c1._name + ''': "Geez, wouldn't kill you to be a little kinder."''')
                print('''Passerby: "How rude! I'm calling your store and leaving a bad review!"''')
                print("Critical lose! You'll be lucky if your boss doesn't fire you after this. -1 Charisma.")
                c1.challenge_result(2, 0)
                c1.mod_stat(chr, -1)


    elif c1._role == "mc": #mail courier
        print()
    print('                                                 *End of Chapter 2*')


