"""
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.
"""


def even():
    x = input("Is this num odd/even?:")
    if int(x) & 1: # Divisable by 2?
        print(f"{x} is NOT even.")
    else:
        print(f"{x} is even.")

even()
