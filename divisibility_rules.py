# Divisibility rules app
# This app will take a number from the user and return a list of numbers that the input number is divisible by
# Example:
'''Enter a number to find out which numbers it is divisible by
2
2 is divisible by [1, 2]'''
# Enter a number to find out which numbers it is divisible by
while True:
    divis_nums = []
    usr_input = input("Enter a number to find out which numbers it is divisible by\n")
    if not usr_input.isdigit():
        print("Please enter a valid number")
        continue
    for i in range(1, int(usr_input) + 1):
        if int(usr_input) % i == 0:
            divis_nums.append(i)
    print(f"{usr_input} is divisible by {divis_nums}")
    usr_input = input("Would you like to try another number? (y/n)\n")
    usr_input = usr_input.lower()
    if usr_input == "n":
        break

