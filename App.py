"""This module contains the application through which the player interacts with the game"""
from Role1 import Pizza
import Game
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
    
    if role == "1" or role == "2": #checks if role is 1 or 2
        if role == "1": #assigns role_name
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


if role == "1":
    c1 = Pizza(character_name)
elif role == "2":
    # c1 = Mail(character_name)
    print()

Game.chapter_1_cutscene(c1)
Game.chapter_1_challenge(c1)