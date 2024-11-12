

"""
In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.

### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens?
How can you handle multiple words in Python?

Test the program by entering a string value for age (e.g., "twenty"). 
What happens? How can you prevent this issue?
"""

print("Register your biography!")

# Variables
icon = ("""
⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣠⠖⠉⠉⠙⠲⣄⠀⠀
⠀⠀⠀⣠⠖⠋⠁⡠⠂⠀⢰⠁⣀⣤⣤⢤⣴⣾⣦⠀
⠀⢀⠞⠁⡄⠀⢰⠃⠀⠀⣿⠼⣿⣿⣿⠎⢿⣿⠿⡄
⢠⡟⣒⣺⣧⣴⣿⡄⣠⡀⢹⣆⣈⠉⢁⣀⣀⡄⢠⠇
⡾⠀⢻⣿⣿⡿⣼⣧⣟⣇⣸⣛⣷⣤⣀⣁⣀⣴⣿⠀
⡇⡄⢰⣿⣿⢰⣿⠿⠋⠘⠿⣿⣃⣿⡿⠉⠉⢹⣿⠀
⠳⡿⣸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⡇⠀⣠⣾⢿⠀
⠀⠀⣿⠿⣿⣶⣶⣦⢤⢤⠶⣶⣶⣿⣇⣴⣿⡇⢸⠀
⠀⠀⣿⡇⢸⣿⣿⣷⣾⣿⣷⣿⣿⣿⡟⠋⣿⡇⠸⡄
⠀⠀⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣷⠀⢣   
""")
# icon is just for novelty, created using https://lachlanarthur.github.io/Braille-ASCII-Art/

i = 0 # using for counting 


print("\n",icon)

print("!!! ALL INPUTS CAN'T BE UNDONE, PLEASE ENTER WITH CAUTION... !!!", "\n Are you sure you want to continue? (enter to continute)")
input()

print("-- Registration --") 

a = input("Enter name:") 
if a.strip() == "": # strip() will remove all spaces in the start and end
    a = "User" # force
    print("Username defaulted.")


while True: 
    try: 
        b = int(input("Enter age: ")) # only be reading integers
        break
    except ValueError: # wrong type
        print("Invalid input! Please enter a valid integer.") # return


c = input("Enter town:")
if c.strip() == "": # empty or not
    c = "N/A" # force
    print("EMPTY")


reg = 1 # old variable
if reg == 1:
    print("\nthank you for registering...")


# rename variables to their responding properties
name, age, town, = (a), (b), (c),


if reg == 1: # print this ONLY if user has input their passwords correctly
    print("------------------------------------------------------------------------------------------------------------")
    print(f"\nThank you for filling up the fourm {name}!") 
    print("\nUser Info:")
    print("\nName:",name, "\nAge:",age, "\nTown:",town) # list
else:
    print("Registration Failed. Try again next time...")


# I enjoyed creating this one, thanks with my previous experience thanks with LUA.

# Coding is Cool
