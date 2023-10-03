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
name = ""
while True:
    role = input("Please enter 1 for pizza driver, or 2 for mail courier: ")
    
    if role.isdigit(): #checks if role is a number
        role = int(role)
        if role == 1 or role == 2: #checks if role is 1 or 2
            if role == 1: #assigns name
                name = "pizza driver"
            else:
                name = "mail courier"
            print("Great! You have chosen to play as the " +name +"!")
            break
        else:
            print("Error, invalid answer.")
    else:
        print("Error, invalid answer.")

print("Let's begin your journey!")