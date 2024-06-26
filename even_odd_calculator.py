while True:
    usr_input = input("Enter a number to find out if it is even or odd\n")
    if int(usr_input) % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
    usr_input = input("Would you like to try another number? (y/n)\n")
    usr_input = usr_input.lower()
    if usr_input == "n":
        break





