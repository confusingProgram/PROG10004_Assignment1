"""This module contains the game logic like methods"""
import random
from Role1 import Pizza
from Role2 import Mail

def roll_dice(stat): #stat = pd._str for example
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2 + stat
    print("You rolled " + str(sum) + "!")   
    return sum

  
# pd == Pizza Driver
def chapter_1_cutscene_pd(pd): #pd is the character
    """This method contains the game cutscene for Chapter 1 for the Pizza Driver"""
    print('                                    *Chapter 1: The Pizza Shop*')
    print('                                         *RING RING RING*                                ')
    print('                                             *KERCHUNK*                                      ')
    print('Boss: "Hello, welcome to Supernova Pizza, how can I help you?"')
    print('''      "..Uh huh... Uh huh... Got it, we'll have your order there in no time. Goodbye."''')
    print('                                             *KERCHUNK*                                      ')
    print('Boss: "Alright ' + pd._name + ', we got a new order for 123 Somewhere Street."')
    print('      "The order is 3 pepperoni pizzas, and 12 pc. wings. We have some already. Go load them into your car."')
    print('      "You better show these customers that Supernova Pizza is the fastest restaurant around!"')
    print('      "And no slacking! Last time, I had a customer complain that their pizza was so cold, it could cool their drinks!"')
    print()
    print('                                     Objective: Load the order')
    print('Gee, they sure sounds angry!')
    print('Now... how to load the pizzas into the car?')
    print("""You could try simply carrying out the pizzas to your car; use a cart; or you're feeling adventurous, persuade your boss to carry them.""")


def chapter_1_challenge_pd(pd): 
    """This method contains the game challenge for Chapter 1 for the Pizza Driver"""
    op_num = ""
    while True: # Selection loop
        op_text_1 = "carry pizzas to the car" # requires 6 strength, +1 strength if 11-12, -1 strength on loss if 2-3
        op_text_2 = "use a cart to bring the pizzas" # requires 4 dexterity to pass, +1 dexterity if 11-12, -1 charisma on loss if 2-3
        op_text_3 = "persuade your boss to carry them" # requires 8 charisma to pass, +1 charisma if 11-12, -1 charisma on loss if 3-4
        op_text = ""
        
        print("Options:")
        print("1 [STR]. " + op_text_1 + ".")
        print("2 [DEX]. " + op_text_2 + ".")
        print("3 [CHR]. " + op_text_3 + ".")
        while True: # Choosing options loop
            op_num = input("Type in 1, 2, or 3: ")
            if op_num == "1":
                op_text = op_text_1
                break # If user selects a valid op_num, options loop will exit
            elif op_num == "2":
                op_text = op_text_2
                break
            elif op_num == "3":
                op_text = op_text_3
                break
            else:
                print("Error, invalid answer.")
        while True: # Confirmation loop
            choice = input("Are you sure you want to " + op_text + "?  Yes or No: ")
            if choice == "Yes" or choice == "No":
                break # If user says Yes or No, confirmation loop will exit
            else:
                print("Error, invalid answer.")
        
        if choice == "Yes":
            print("You have chosen to: " + op_text + ".")
            break # If user said yes, selection loop will exit.
        
    print("Let's get into the challenge.")
    if op_num == "1":
        print("Carrying the pizzas to the car requires a roll of 6 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._str)
        if num > 10: #11-12
            print("Critical win! The pizzas and wings feel as light as paper, and you feel even stronger! +1 strength!")
            pd.challenge_result(1, 1)
            pd.mod_stat(str, 1)
        elif num > 5: #6-10
            print("Win! With some trouble, but not too much trouble, you put the order into the car, and you're on your way.")
            pd.challenge_result(1, 1)
        elif num > 3: #4-5
            print("Lose! The food turns out to be a little heavier than you would've thought, and you stumble and hit your elbow on your way out.")
            pd.challenge_result(1, 0)
        else: #2-3
            print("Critical lose! Are these pizzas actually pizzas, or cinder blocks?! You fall and drop the food, but luckily nothing spills. -1 Strength.")
            pd.challenge_result(1, 0)
            pd.mod_stat(str, -1)
    elif op_num == "2":
        print("Using a cart to bring the pizzas requires a roll of 4 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._dex)
        if num > 10: #11-12
            print("Critical win! Why work hard when you can just handle a cart instead? Piece of cake! +1 Dexterity")
            pd.challenge_result(1, 1)
            pd.mod_stat(dex, 1)
        elif num > 3: #4-10
            print("Win! Sure is handy having this cart around.")
            pd.challenge_result(1, 1)
        elif num > 2: #3
            print("Lose! What on earth? One of the back wheels on the cart came undone. That's coming out of your paycheque.")
            pd.challenge_result(1, 0)
        else: #2
            print("Critical lose! Hastily, you run with the cart, but lose control and smash your hand into the door frame! Yowch!! -1 Dexterity.")
            pd.challenge_result(1, 0)
            pd.mod_stat(dex, -1)
    elif op_num == "3":
        print("Persuading your boss to carry them requires a roll of 8 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._chr)
        if num > 10: #11-12
            print('Boss: "Hey! What are you standing around for?!"')
            print(pd._name + ': "Boss, can you carry the pizzas for me? I uhhh, really need to use the bathroom, like really really badly."')
            print('Boss: "..."')
            print('      "Fine, but make it quick!"')
            print("Critical win! Huh, guess you're doing even less work. +1 Charisma")
            pd.challenge_result(1, 1)
            pd.mod_stat(chr, 1)
        elif num > 7: #8-10
            print('                                         *SNAP SNAP SNAP*                                ')
            print('Boss: "Hey! Are you even listening?!"')
            print('      "Geez, do I have to do everything myself?!"')
            print('       *GRUMBLES*') 
            print("Win! And you didn't even say anything.")
            pd.challenge_result(1, 1)
        elif num > 3: #4-7
            print(pd._name + ': "Boss, can you carry the pizzas for me? I uhhh, forgot how to walk."')
            print('Boss: "What do you mean you forgot how to walk? Just do your job!"')
            print("Lose! Not the most convincing argument I've heard recently.")
            pd.challenge_result(1, 0)
        else: #2-3
            print(pd._name + ''': "Boss, can you carry the pizzas for me? I'll do you a favour."''')
            print('       *WINK*')
            print('Boss: "..."')
            print('      "How about you do me this favour, and carry the darn order to the car?!"')
            print("Critical lose! Very daring to ask your boss a favour when you're already on their bad side. -1 Charisma.")
            pd.challenge_result(1, 0)
            pd.mod_stat(chr, -1)
    print('                                                 *End of Chapter 1*')

def chapter_2_cutscene_pd(pd): 
    """This method contains the game cutscene for Chapter 2 for the Pizza Driver"""
    if pd._role == "pd": # Pizza Driver
        print('                                    *Chapter 2: On The Road*')
        print("You are driving down a road on your way to 123 Somewhere Street.")
        print(pd._name + ': "..."')
        print('      *SQUINTS*')
        print('      "What is that?"')
        print("It is an imposing boulder, impeding your path!")
        print(pd._name + ': "I should probably pull over."')
        print('                                     *SCREEEEEEEEEEEECH*                                ')
        print('''Passerby: "Wow, that is a large boulder. I hope you don't plan on asking me for help."''')
        print('                                     Objective: Move the boulder')
        print("Who just leaves a boulder in the middle of a road? An urban one at that. Where did this come from?")
        print("The boulder is propped up against another large rock, but you can drive around that one if you can move the large boulder first.")
        print("How on earth are you going to move the boulder?")
        print("You could try pushing it yourself; using a sturdy tree branch to use it as a lever; or smooth-talk the passerby in helping.")
        
def chapter_2_challenge_pd(pd):
    """This method contains the game challenge for Chapter 2 for the Pizza Driver"""
    op_num = ""
    while True: # Selection loop
        op_text_1 = "push it yourself" # requires 8 strength, +1 strength if 11-12, -1 strength on loss if 3-4
        op_text_2 = "use a tree branch as a lever" # requires 5 dexterity to pass, +1 dexterity if 11-12, -1 charisma on loss if 2-3
        op_text_3 = "smooth-talk the passerby" # requires 6 charisma to pass, +1 charisma if 11-12, -1 charisma on loss if 2-3
        op_text = ""
        
        print("Options:") # Displays options
        print("1 [STR]. " + op_text_1 + ".")
        print("2 [DEX]. " + op_text_2 + ".")
        print("3 [CHR]. " + op_text_3 + ".")
        while True: # Choosing options loop
            op_num = input("Type in 1, 2, or 3: ")
            if op_num == "1":
                op_text = op_text_1
                break # If user selects a valid op_num, options loop will exit
            elif op_num == "2":
                op_text = op_text_2
                break
            elif op_num == "3":
                op_text = op_text_3
                break
            else:
                print("Error, invalid answer.")
        while True: #Confirmation loop
            choice = input("Are you sure you want to " + op_text + "?  Yes or No: ")
            if choice == "Yes" or choice == "No":
                break # If user says Yes or No, confirmation loop will exit
            else:
                print("Error, invalid answer.")
        
        if choice == "Yes":
            print("You have chosen to: " + op_text + ".")
            break # If user said yes, selection loop will exit.
    
    print("Let's get into the challenge.")
    if op_num == "1":
        print("Pushing it yourself requires a roll of 8 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._str)
        if num > 10: #11-12
            print("Critical win! Woah, do you go to the gym?! That boulder basically moved itself! +1 strength!")
            pd.challenge_result(2, 1)
            pd.mod_stat(str, 1)
        elif num > 7: #8-10
            print("Win! It's pretty heavy, but you're able to manage and roll the boulder out.")
            pd.challenge_result(2, 1)
        elif num > 3: #4-7
            print("Lose! The boulder's too heavy. Now you're too tired to move it in any way. Time to find a different route.")
            pd.challenge_result(2, 0)
        else: #2-3
            print("Critical lose! You push and push and it does not budge. You also pull 3 different muscles in the process. -1 Strength.")
            pd.challenge_result(2, 0)
            pd.mod_stat(str, -1)
    elif op_num == "2":
        print("Using a tree branch as a lever requires a roll of 5 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._dex)
        if num > 10: #11-12
            print("Critical win! Is this a measure of dexterity or intellect? Either way, better than brute force. +1 Dexterity")
            pd.challenge_result(2, 1)
            pd.mod_stat(dex, 1)
        elif num > 4: #5-10
            print("Win! Good thing this is an oak branch, and not balsa.")
            pd.challenge_result(2, 1)
        elif num > 2: #3-4
            print("Lose! The boulder is somehow put in an even worse position, before the branch breaks. Now you really can't move it.")
            pd.challenge_result(2, 0)
        else: #2
            print("Critical lose! The branch becomes dislodged and breaks as it fractures your wrist. You didn't need that right? -1 Dexterity.")
            pd.challenge_result(2, 0)
            pd.mod_stat(dex, -1)
    elif op_num == "3":
        print("Smooth-talking the passerby requires a roll of 6 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._chr)
        if num > 10: #11-12
            print(pd._name + ': "Hey, do you wanna help me push the boulder?"')
            print('Passerby: "Uh, no. It looks really heavy."')
            print(pd._name + ''': "Come on! Don't you wanna say that you've pushed a boulder?"''')
            print('Passerby: "..."')
            print('      "You make a convincing argument. Alright."')
            print("Critical win! It does sound cool to say that you've moved a big boulder! +1 Charisma")
            pd.challenge_result(2, 1)
            pd.mod_stat(chr, 1)
        elif num > 5: #6-10
            print(pd._name + ': "Actually, can you help me push the boulder?"')
            print('''Passerby: "What's in it for me? The boulder isn't my problem."''')
            print(pd._name + ': "I could give you a buy-one-get-one free pizza coupon...?"')
            print('''Passerby: "I do like pizza. Alright then, let's get to it."''')
            print("Win! An extra customer! Your boss will be quite pleased.")
            pd.challenge_result(2, 1)
        elif num > 3: #4-5
            print(pd._name + ''': "Could you help me with the boulder? It's really heavy. And geez, it could crush one of us."''')
            print('''Passerby: "That makes me wanna move it even less. You're on your own."''')
            print("You try moving the boulder by yourself but it seems to gotten 8 times heavier after the passerby leaves!")
            print("Lose! Why did it get heavier after they left??")
            pd.challenge_result(2, 0)
        else: #2-3
            print(pd._name + ''': "Geez, wouldn't kill you to be a little kinder."''')
            print('''Passerby: "How rude! I'm calling your store and leaving a bad review!"''')
            print("Critical lose! You'll be lucky if your boss doesn't fire you after this. -1 Charisma.")
            pd.challenge_result(2, 0)
            pd.mod_stat(chr, -1)
    print('                                                 *End of Chapter 2*')

def chapter_3_cutscene_pd(pd): 
    """This method contains the game cutscene for Chapter 3 for the Pizza Driver"""
    if pd._role == "pd": #pizza driver
        print('                                    *Chapter 3: A Delicious Delivery*')
        print(pd._name + ''': "123 Somewhere Street, here it is."''')
        print('                                     *DING DING*                                ')
        print('                                          *SLAM*                                ')
        print("As you get out of the car, you're approached by a strange person.")
        print(pd._name + ''': "Uhh, can I help you?"''')
        print('''Stranger: "Why, yes you can. I would like those pizzas you have there."''')
        print(pd._name + ''': "Do you live at 123 Somewhere Street?"''')
        print('''Stranger: "If I get those pizzas, then yes."''')
        print(pd._name + ''': "You're gonna have to step aside, I need to deliver this food."''')
        print('''Stranger: "No can do. Those pizzas will be mine!"''')
        print('                                     Objective: Defend the pizzas!')
        print("Wow! They really want your pizzas! But you're determined to complete your job!")
        print("You can either fight in hand-to-hand combat; swing open the car door to knock them out; or intimidate them.")

def chapter_3_challenge_pd(pd):
    """This method contains the game challenge for Chapter 3 for the Pizza Driver"""
    op_num = ""
    while True: # Selection loop
        op_text_1 = "fight hand-to-hand" # requires 7 strength
        op_text_2 = "open the car door" # requires 7 dexterity to pass
        op_text_3 = "intimidate them" # requires 7 charisma to pass
        op_text = ""
        
        print("Options:") # Displays options
        print("1 [STR]. " + op_text_1 + ".")
        print("2 [DEX]. " + op_text_2 + ".")
        print("3 [CHR]. " + op_text_3 + ".")
        while True: # Choosing options loop
            op_num = input("Type in 1, 2, or 3: ")
            if op_num == "1":
                op_text = op_text_1
                break # If user selects a valid op_num, options loop will exit
            elif op_num == "2":
                op_text = op_text_2
                break
            elif op_num == "3":
                op_text = op_text_3
                break
            else:
                print("Error, invalid answer.")
        while True: #Confirmation loop
            choice = input("Are you sure you want to " + op_text + "?  Yes or No: ")
            if choice == "Yes" or choice == "No":
                break # If user says Yes or No, confirmation loop will exit
            else:
                print("Error, invalid answer.")
        
        if choice == "Yes":
            print("You have chosen to: " + op_text + ".")
            break # If user said yes, selection loop will exit.
    
    print("Let's get into the challenge.")
    if op_num == "1":
        print("Fighting hand-to-hand requires a roll of 7 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._str)
        if num > 10: #11-12
            print("Critical win! With one fell swing, the stranger is knocked unconscious. He'll be fine.")
            pd.challenge_result(3, 1)
            pd.mod_stat(str, 1)
        elif num > 6: #7-10
            print("Win! Your martial prowess is superior, and you defeat the stranger!")
            pd.challenge_result(3, 1)
        elif num > 3: #4-5
            print("Lose! Despite your best effort, the stranger comes out on top and takes the food!")
            pd.challenge_result(3, 0)
        else: #2-3
            print("Critical lose! Before you're even ready, the stranger delivers a mean right-hook! You wake up to find the stranger and the pizzas gone.")
            pd.challenge_result(3, 0)
    elif op_num == "2":
        print("Opening the car door requires a roll of 7 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._dex)
        if num > 10: #11-12
            print("Critical win! The car door swings open and knocks out the stranger! That's gonna leave a mark.")
            pd.challenge_result(3, 1)
        elif num > 6: #5-10
            print("Win! You catch the stranger off guard, knocking them off their feet and leaving them dazed.")
            pd.challenge_result(3, 1)
        elif num > 3: #4-5
            print("Lose! The car door catches on your foot, which the stranger uses to their advantage, as they take the pizzas.")
            pd.challenge_result(3, 0)
        else: #2-3
            print("Critical lose! Your footing wasn't in the right place, and you accidentally hit yourself with the door! The stranger flees with the pizzas.")
            pd.challenge_result(3, 0)
    elif op_num == "3":
        print("Intimidating the stranger requires a roll of 7 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(pd._chr)
        if num > 10: #11-12
            print(pd._name + ''': "Are you sure about this? You do not want to fight me."''')
            print('''Stranger: "I am very sure! As sure as those pizzas being tasty!"''')
            print("You swiftly step forward and grab their collar, picking them up.")
            print(pd._name + ''': "I implore you to reconsider."''')
            print('''Stranger: "Ack- Woah! I just remembered I had a big lunch!"''')
            print("Critical win! Quite the unassuming pizza driver!")
            pd.challenge_result(3, 1)
        elif num > 6: #7-10
            print(pd._name + ''': "You know, I've had a real bad day today. My boss yelled at me."''')
            print('      "I had to deal with a giant boulder. And now I have to deal with you!"')
            print('''      "I've been looking for an outlet for my anger!"''')
            print('''Stranger: "Hey, you know what?! You can keep the pizzas."''')
            print('''      "I just remembered I had an important business meeting. Haha..."''')
            print('      *FLEES*')
            print("Win! You have your own important business to tend to.")
            pd.challenge_result(3, 1)
        elif num > 3: #4-5
            print(pd._name + ''': "You think you can beat me? Don't make me laugh. Hah!"''')
            print('''Stranger: *KICK*''')
            print(pd._name + ''': "Ow!"''')
            print('''Stranger: "I just did, now the pizzas are mine!"''')
            print("Lose! Overconfidence got the best of you.")
            pd.challenge_result(3, 0)
        else: #2-3
            print(pd._name + ''': "Can you not do this? I'm not really a fighter."''')
            print('''Stranger: "Oh, this will be easy!"''')
            print('With their newfound confidence, the stranger steals the pizzas!')
            print("Critical lose! You can't show that you're scared.")
            pd.challenge_result(3, 0)
    print('                                                 *End of Chapter 3*')

def ending_cutscene_pd(pd): # Win condition is dependant on whether challenge 3 was successful
    """This method contains the ending cutscene for the Pizza Driver"""
    print('                                                 *Ending Cutscene*')
    if pd._challenge_3_result == 1:
        print("Exhausted, you make your way up the steps of the house.")
        print('                                     *DING DONG*                                ')
        print('                                     *CREEEEAK*                                ')
        print(pd._name + ''': "Hello, order of 3 pepperonis, and 12 pc. wings?"''')
        print('''Homeowner: "Yep, that's right! You look a little rough, everything alright?"''')
        print(pd._name + ''': "Just part of a day's work."''')
        print('''Homeowner: "Well, here's a tip, you deserve it."''')
        print(pd._name + ''': "Thank you. Have a nice day."''')
        print('                                     *SLAM*                                ')
        print("Congratulations! You delivered the pizzas!")
    elif pd._challenge_3_result == 0:
        print('                                         *RING RING*                                ')
        print('                                     *SLAM*                                ')
        print("Having lost the pizzas, you regretfully phone your boss as you get back into the car.")
        print('Boss: "WHAT DO YOU MEAN YOU LOST THE PIZZAS?!"')
        print("Game over! You failed to deliver the pizzas!")

"""This method contains the game cutscene for Chapter 3 for the Mail Courier"""
"""This method contains the game challenge for Chapter 3 for the Mail Courier"""
"""This method contains the ending cutscene for the Mail Courier"""

#mc == Mail Courier
def chapter_1_cutscene_mc(mc):
    """This method contains the game cutscene for Chapter 1 for the Mail Courier"""
    print('                                        Chapter 1: Canada Post')
    print( '                                    * Mail Courier arrives at Canada Post*'          )
    print('                                            *DING DING *        ')
    print('                                                    *Door Opens ')
    print(                              "Good morning! Have you got any boxes for me to deliver?")
    print(          'Boss: "Good morning '+ mc.name +', I have the boxes right here."')
    print(              'Boss: "You have to deleiver it to House number 123 on That Street"')
    print(              'Boss:"But be carefull, these boxes are heavy "' )
    print(                                 'Ok Boss! I got this!!!')
    print('                                             Objective: Deliver the Boxes!!!')
    print('                I hope that this delivery goes smoothly')
    print(  'Hmmmm... Which vehicle should I take?  ')
    print("You could choose to deliver the boxes in your van; a customer's car; or motorbike")


def chapter_1_challenge_mc(mc):
    """This method contains the game challenge for Chapter 1 for the Mail Courier"""
    op_num = 0
    while True: # Selection loop
        op_text_1 = "carry the boxes to your van car to deliver mail" # Requires 8 strength, +1 strength if 11-12, -1 strength if 2-3
        op_text_2 = "use a customer's car to deliver mail" # Requires 4 dexterity, +1 dexterity if 11-12, -1 dexterity if 2
        op_text_3 = "use a motocycle to deliver mail" # Requires 6 IQ, +1 IQ if 11-12, -1 IQ if 2-3
        op_text = ""
        print("Options:") # Displays options
        print("1 [STR]. " + op_text_1 + ".")
        print("2 [DEX]. " + op_text_2 + ".")
        print("3 [IQ]. " +  op_text_3 + ".")
        while True: # Choosing options loop
            options = input("Type in 1, 2, or 3: ")
            if op_num == "1" or op_num == "2" or op_num == "3":
                break # If user selects a valid op_num, then options loop will exit
            else:
                print("Error, invalid answer.")
        while True: #Confirm loop
            choice = input("Are you sure you want to " + op_text + "?  Yes or No: ")
            if choice == "Yes" or choice == "No":
                break # If user says Yes or No, confirm loop will exit
            else:
                print("Error, invalid answer.")
        
        if choice == "Yes":
            print("You have chosen to: " + op_text + ".")
            break # If user said yes, selection loop will exit.
    
    print("Alright, Let's start the challenge!!")
    
    if op_num == "1":
        print("Carrying the boxes to your van car to deliver mail requires a roll of 8 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(mc._str)
        if num > 10: #11-12
            print("Critical win! The boxes are not that heavy and you can tell that your workout paid off! +1 strength!")
            mc.challenge_result(1, 1)
            mc.mod_stat(str, 1)
        elif num > 7: #8-10
            print("Win! you had a bit of trouble but you got it, you put the boxes in the van and you're off to the journey!")
            mc.challenge_result(1, 1)
        elif num > 3: #4-7
            print("Lose! The boxes you carried were a lot heavier than you thought, maybe you do need those gym sessions!")
            mc.challenge_result(1, 0)
        else: #2-3
            print("Critical lose! What is inside these boxes?! You almost drop the boxes, howvere your boss saw you and came to help you. -1 Strength.")
            mc.challenge_result(1, 0)
            mc.mod_stat(str, -1)
    elif op_num == "2":
        print("Using a customer's car requires a roll of 4 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(mc._dex)
        if num > 10: #11-12
            print("Critical win! WoW that customer lend you their car? This is going to be quick! +1 Dexterity")
            mc.challenge_result(1, 1)
            mc.mod_stat(dex, 1)
        elif num > 3: #4-10
            print("Win! The customer didn't trust to but gave you their car anyway .")
            mc.challenge_result(1, 1)
        elif num > 2: #3
            print("Lose! You didn't get the car and the customer ran over your foot! Ouch!! Thats got to hurt.")
            mc.challenge_result(1, 0)
        else: #2
            print("Critical lose! You got into a car accident as soon as you got in the car")
            print( "The customer was really mad! Sigh! you are gonna pay for that! -1 Dexterity.")
            mc.challenge_result(1, 0)
            mc.mod_stat(dex, -1)
    elif op_num == "3":
        print("Using a motorbike requires a roll of 6 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(mc._iq)
        if num > 10: #11-12
            print("Critical win! Hmm, I guess you're going to be delivering these boxes in no time!. +1 Intelligence")
            mc.challenge_result(1, 1)
            mc.mod_stat(iq, 1)
        elif num > 5: #6-10
            print("Win! Just hope that there is no traffic, that would suck!.")
            mc.challenge_result(1, 1)
        elif num > 3: #4-5
            print("Lose! [chapter_1_challenge_3_3].")
            mc.challenge_result(1, 0)
        else: #2-3
            print("You left the motorbike unattended and running, someone stole it! I mean who does that!!. -1 Intelligence.")
            mc.challenge_result(1, 0)
            mc.mod_stat(iq, -1)
    print('                                                 *This Ends Chapter 1*')

def chapter_2_cutscene_mc(mc):
    """This method contains the game cutscene for Chapter 2 for the Mail Courier"""
    print('                                    *Chapter 2: On Your Journey*')
    print("You are making your way down to That street.")
    print("When you suddenly stop")
    print('                                            *SCREEECHHH!!!*')
    print('      "What is that?!"')
    print("There is a random portal that just popped up in the middle of the street!")
    print(mc._name + ': "I have to pull over to the side first ."')
    print('                                     *SCREEEEEEEEEEEECH*                                ')
    print('                                     Objective: Close the Portal')
    print(mc._name +': "Who just opens a portal in the middle of the street? This is not Harry Potter!"')
    print("You can just drive into to it, however you don't know where you are going to end up. It is better if you close the portal.")
    print("How are you going to close the portal?")
    print("You could try to push a huge boulder in it ; use a ray gun ; or press the red button.")

def chapter_2_challenge_mc(mc):
    """This method contains the game challenge for Chapter 2 for the Mail Courier"""
    op_num = ""
    while True: # Selection loop
        op_text_1 = "push a boulder" # requires 6 strength, +1 strength if 11-12, -1 strength on loss if 2-3
        op_text_2 = "use a ray gun" # requires 8 dexterity to pass, +1 dexterity if 11-12, -1 dexterity on loss if 2-3
        op_text_3 = "press the button" # requires 7 IQ to pass, +1 IQ if 11-12, -1 IQ on loss if 2-3
        op_text = ""
        print("Options:") # Displays options
        print("1 [STR]. " + op_text_1 + ".")
        print("2 [DEX]. " + op_text_2 + ".")
        print("3 [IQ]. "  + op_text_3 + ".")
        while True: # Choosing options loop
            options = input("Type in 1, 2, or 3: ")
            if op_num == "1" or op_num == "2" or op_num == "3":
                break # If user selects a valid op_num, then options loop will exit
            else:
                print("Error, invalid answer.")
        while True: #Confrim loop
            choice = input("Are you sure you want to " + op_text + "?  Yes or No: ")
            if choice == "Yes" or choice == "No":
                break # If user says Yes or No, confirm loop will exit
            else:
                print("Error, invalid answer.")
        
        if choice == "Yes":
            print("You have chosen to: " + op_text + ".")
            break # If user said yes, selection loop will exit.
    
    print("Alright, Let's start the challenge!!")
    if op_num == "1":
        print("Pushing the boulder into the Portal requires a roll of 6 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(mc._str)
        if num > 10: #11-12
            print("Critical Win! WOOWHH that bouder had no chance against you! +1 strength!")
            mc.challenge_result(2, 1)
            mc.mod_stat(str, 1)
        elif num > 5: #6-10
            print("Win! That was really heavy, but you managed to roll the boulder into the portal.")
            mc.challenge_result(2, 1)
        elif num > 3: #4-5
            print("Lose! The boulder is way too heavy. When you tried to move it, you crushed a brid. ***OUCHH**")
            mc.challenge_result(2, 0)
        else: #2-3
            print("Critical lose! You pushed the boulder into the other direction and rolled away from you. -1 strenght.")
            mc.challenge_result(2, 0)
            mc.mod_stat(str, -1)
    elif op_num == "2":
        print("Using a ray gun requires a roll of 8 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(mc._dex)
        if num > 10: #11-12
            print("Critical win! Heyy! at least now you know that you can use a ray gun, if you need to. +1 Dexterity")
            mc.challenge_result(2, 1)
            mc.mod_stat(dex, 1)
        elif num > 4: #5-10
            print("Win! At least you got the aim right.")
            mc.challenge_result(2, 1)
        elif num > 2: #3-4
            print("Lose! The portal truned into a bigger one. You pressed the wrong button.")
            mc.challenge_result(2, 0)
        else: #2
            print("Critical lose! You aimed the ray gun at someone and they truned into a portal. Great now you have 2 portals to deal with! -1 Dexterity.")
            mc.challenge_result(2, 0)
            mc.mod_stat(dex, -1)
    elif op_num == "3":
        print("Pressing the red button requires a roll of 7 to complete.")
        input("Press Enter to roll the dice.")
        num = roll_dice(mc._iq)
        if num > 10: #11-12
            print("Critical win! You pressed the red button and it was gone before you know it! +1 Intelligence")
            mc.challenge_result(2, 1)
            mc.mod_stat(iq, 1)
        elif num > 7: #8-10
            print("Win! You had trouble finding the button, but at last you got it.")
            mc.challenge_result(2, 1)
        elif num > 3: #4-7
            print("Lose! You pressed the wrong button and let out some weird creatures!")
            mc.challenge_result(2, 0)
        else: #2-3
            print("Critical lose! You pressed the yellow one instead. Back to kindergarden again!. -1 Intelligence.")
            mc.challenge_result(2, 0)
            mc.mod_stat(iq, -1)
    print('                                                 *This Ends Chapter 2*')

def chapter_3_cutscene_mc(mc):
    """This method contains the game cutscene for Chapter 3 for the Mail Courier"""
    print()

def chapter_3_challenge_mc(mc):
    """This method contains the game challenge for Chapter 3 for the Mail Courier"""
    print()

def ending_cutscene_mc(mc):
    """This method contains the ending cutscene for the Mail Courier"""
    print()