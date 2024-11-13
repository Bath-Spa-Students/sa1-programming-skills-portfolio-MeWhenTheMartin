

"""
### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
"""

# Variables
month = {
    'January': '31', 
    'Febuary': '29',
    'March': "31",
    'April': "30",
    'May': "31",
    'June': "30",
    'July': "31",
    'August': "31",
    'September': "30",
    'October': "30",
    'November': "30",
    'December': "31",
    }

list_m = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True: 
    try: 
        item = int(input("Enter a month by number (ex: January = 1):"))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.") # return

item = list_m[item - 1] # num -> month

print(f"Month: {item}")

def y(num): # year is leap?
        if num % 4 == 0: # check if divisible by 4(leap year)
            print("It's leap year.")
            print(f"Days on this month: {month[item]}")
        else: # non-leap
            print("It's not leap year.")
            print(f"Days on this month: {month[item]}")

yoop = True

while yoop: # don't nest while true loops
    print("\nNote: 'e' To enter year manually.")
    leap = str(input("Leap year? (y/n/e):").lower())
    if leap.lower() == "y":
        if item == list_m[1]:
            print(f"Days on this month: 28")
        break
    elif leap.lower() == "n":
        y(3) # hardcoded year
        break
    else:
        if leap.lower() == "e":
            while True: 
                try: 
                    year = int(input("Enter year:"))
                    y(year)
                    yoop = False
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer.") # return
        else:
            print("Not 'y' or 'n'")

# Coding is cool