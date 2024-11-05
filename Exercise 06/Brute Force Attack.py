

"""
Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""


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