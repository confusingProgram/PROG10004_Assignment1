print("Welcome to [game name], a text-based RPG adventure game!")
print("Your goal is to make a delivery to 123 Somewhere Street.")
print("The two roles are either a pizza delivery driver, or mail courier.")

role = 0
name = ""
choice = ""
while True:
    role = input("Please enter 1 for pizza delivery driver, or 2 for mail courier: ")
    
    if role.isdigit(): #checks if role is a number
        role = int(role)
        if role == 1 or role == 2: #checks if role is 1 or 2
            if role == 1: #assigns name
                name = "pizza delivery driver"
            else:
                name = "mail courier"
            
            while True:
                choice = input("Are you sure you want to play as " +name + "? Yes or No: ")
                if choice == "Yes" or choice == "No":
                    break #exits the confirmation loop
                else:
                    print("Error, invalid answer.")

            if choice == "Yes":
                print("Great! You have chosen to play as the " +name +"!")
                break #exits the role selection loop. Will only activate if role 1 or 2 is selected and "Yes" is selected
        else:
            print("Error, invalid answer.")
    else:
        print("Error, invalid answer.")

print("Let's begin your journey!")#