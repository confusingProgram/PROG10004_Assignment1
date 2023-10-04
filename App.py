"""This module contains the application through which the player interacts with the game"""
from Role1 import Pizza
# from Role2 import Mail

print("Welcome to [game name], a text-based RPG adventure game!")
print("Your goal is to make a delivery to 123 Somewhere Street.")
print("The way the game is played is through a dice roll, in which the game")
print("game will roll two (2) standard six-sided dice, with a 1 face, 2, 3, 4, 5, and 6.")
print("You will also be given the choice of what stat to use when completing a challenge,")
print("but you won't know the requirement for each stat until you finalize your choice. Choose wisely!")
print("The two roles also have distinct stat distributions, ranging between -2, and +2.")
print("This will either hinder, or improve your chances of completing each challenge.")
print("")
print("Speaking of which, the two roles are the pizza driver, and mail courier.")
print("The pizza driver has 0 Strength, 0 Dexterity, and 1 Charisma.")
print("The mail courier has 1 Strength, -1 Dexterity, and 1 Intelligence.")
print("It's time for you to choose who to play as!")
print("")

role = 0
role_name = ""
choice = ""
while True:
    role = input("Please enter 1 for pizza driver, or 2 for mail courier: ")
    
    if role.isdigit(): #checks if role is a number
        role = int(role)
        if role == 1 or role == 2: #checks if role is 1 or 2
            if role == 1: #assigns role_name
                role_name = "pizza driver"
            else:
                role_name = "mail courier"
            
            while True:
                choice = input("Are you sure you want to play as " +role_name + "? Yes or No: ")
                if choice == "Yes" or choice == "No":
                    break #exits the confirmation loop
                else:
                    print("Error, invalid answer.")

            if choice == "Yes":
                print("Great! You have chosen to play as the " +role_name +"!")
                break #exits the role selection loop. Will only activate if role 1 or 2 is selected and "Yes" is selected
        else:
            print("Error, invalid answer.")
    else:
        print("Error, invalid answer.")

character_name = ""
while True:
    character_name = input("And what's the name of the " + role_name + ": ")
    while True:
                choice = input("Their name is: " + character_name + "? Yes or No: ")
                if choice == "Yes" or choice == "No":
                    break #exits the confirmation loop
                else:
                    print("Error, invalid answer.")
    if choice == "Yes":
        print(character_name + "! What a splendid name!")
        break #exits the character_name loop. "Yes" is selected
    
print("Let's begin the journey!")
print("")


if role == 1:
    c1 = Pizza(character_name)
else:
    c2 = ()

#Challenge 1, Pizza Driver
if c1._role == "pd":
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
    
#Challenge 1, Mail Courier 
if c2._role == "mc":
    print('                                        Chapter 1: Canada Post')
print( '                                    * Mail Courier arrives at Canada Post*'          )
print('mail: Good morning! Have you got any mail for me  ')