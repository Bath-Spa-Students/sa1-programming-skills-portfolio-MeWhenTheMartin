

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


# Welcomes user by displaying a hardcoded welcome message
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

i = 0 # this is my go to variable name when using for counting 


print("\n",icon)
# [\n] stands for "New Line", where if printed will move over the next line and display the value
# down is a better example to visualize it

print("!!! ALL INPUTS CAN'T BE UNDONE, PLEASE ENTER WITH CAUTION... !!!", "\n Are you sure you want to continue? (enter to continute)")
input() # illusion of confirming warning, you can still input anything but nothing will be stored

print("-- Registration --") 

a = input("Enter name:") # variable will take keyboard input from user then print said input
if a.strip() == "": # strip() will remove all spaces in the start and end, so no matter what if there's no value it will always equal to ""
    a = "User" # force variable to User
    print("Username defaulted.") # when there's no input written (exception of space) will always print out an EMPTY message


# this part will be asking the user for their age, because age is a number we should only accept integers/numbers
while True: # a while loop is used, because when user inputs a non-integer it needs to repeat otherwise user will be stuck with an error
    try: # try & except statement
        b = int(input("Enter age: ")) # input will only be reading integers, if failed to read int then it will proceed to ValueError
        break # when input is integer, this will stop the loop and move on the next lines
    except ValueError: # ValueError is when input has the wrong type Example: inputting a string on an integer assignment
        print("Invalid input! Please enter a valid integer.") # display the error message and return from the loop

# user can freely input anything, same concept as getting user's name code
c = input("Enter town:")
if c.strip() == "": # check if input is empty or not
    c = "N/A" # force variable to N/A
    print("EMPTY") # a feedback for user's empty response

ispassw = 0 # a variable that serves as a boolean when a password is given or not, will be used to continue or skip the password input

# same concept as the earlier code
d = input("Enter pasword:")
if d.strip() == "": 
    ispassw = 0 # password is not given my the user
    print("EMPTY")
else:
    ispassw = 1 # password is given by the user, then procceds to the next code

print(ispassw) # check if password was created or not [0=False : 1=True]
# as the Confirm password must match with the Password, we need to run a while true loop again

attempt = 0 # check how many attempts password was written wrong (this is to avoid softlocking on the terminal)
reg = 1 # if password is confirmed, print out the complete registration

while True:
    if ispassw == 0: # check if there's password or not, if none then skip this loop
        break # end loop if no password given
    e = input("Confirm password:")
    if e == d:
        print(e)
        break # end loop when inputted correctly
    else:
        if attempt < 10:
            print("Invalid input! This does not match with password.") # return to prompt 
            print(f"Failed attempts:{attempt}")
            attempt += 1 # count for each failed attempt, this was done to avoid softlocking where user can't exit out of failed attempts
            if attempt == 11: # once this variable reaches the limit (which is 10 attempts), execute this code below
                reg = 0 # variable set to 0, this is a boolead to print out the complete registry or not (in this case don't print)
                print("Maximum attempts reached...") # tell user 
                break # end the loop once max attempts are reached

if reg == 1: # print this ONLY if user has input their passwords correctly
    print("\nthank you for registering...") # end of collecting user inputs

# rename variables to their responding properties
name, age, town, passw = (a), (b), (c), (d) # multiple variables can be assigned in one line
# the variable and value must be corresponed accoring to their order, example: the 3rd variable will be assigned the 3rd value on the list

if reg == 1: # print this ONLY if user has input their passwords correctly
    print("------------------------------------------------------------------------------------------------------------")
    print(f"\nThank you for filling up the fourm {name}!") # f-string to make the message look neat
    print("\nUser Info:")
    print("\nName:",name, "\nAge:",age, "\nTown:",town, "\nPassword:",passw) # print a list of variables on a list, each with their own line
else:
    print("Registration Failed. Try again next time...") # display this ONLY if user did not provide their password or failed to confirm


# I enjoyed creating this one, thanks with my previous experience thanks with LUA.

# Coding is Cool
