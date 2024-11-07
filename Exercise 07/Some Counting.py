

"""
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*
"""

num = 0

while True:
    if num < 51:
        print(num)
        num += 1 # increment/decrement
    else:
        print("end of loop")
        break

num = 50

while True:
    if num > -1:
        print(num)
        num += -1 # increment/decrement
    else:
        print("end of loop")
        break

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

num = 30

while True:
    if num < 51:
        print(num)
        num += 1 # increment/decrement
    else:
        print("end of loop")
        break

num = 50

while True:
    if num > 9:
        print(num)
        num += -2 # increment/decrement
    else:
        print("end of loop")
        break

num = 100

while True:
    if num < 201:
        print(num)
        num += 5 # increment/decrement
    else:
        print("end of loop")
        break