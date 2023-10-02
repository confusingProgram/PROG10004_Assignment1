print("Welcome to [game name], a text-based RPG adventure game!")
print("Your goal is to make a delivery to 123 Somewhere Street.")
print("The two roles are either a pizza delivery driver, or mail courier.")

role = 0
while True:
    role = input("Please enter 1 for pizza delivery driver, or 2 for mail courier.")
    
    if role.isdigit():
        role = int(role)
        if role == 1 or role == 2:
            break
        else:
            print("Error, invalid answer.")
    else:
        ("Error, invalid answer.")

if role == 1:
    print("Great! You have chosen to play as the pizza delivery driver!")
else:
    print("Great! You have chosen to play as the mail courier!")