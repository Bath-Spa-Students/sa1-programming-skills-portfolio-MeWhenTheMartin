

"""
In this exercise, you will create and work with integer variables, perform arithmetic operations,
and print the result to the console.


1. Declare a variable and initialize it with the integer value `8`.
2. Declare a second variable and initialize it with the integer value `10`.
3. Declare a third variable that stores the sum of first two numbers.
4. Print the value of the sum to the console.
"""

# to declare a variable it goes like this.
x = int(8)
# the variable to assign into a data type which is integer, that integer will contain a value in a bracket
# if a non integer value is assigned in a int value
'example = int("hello")'
# ValueError: invalid literal for int() with base 10: 'hello'

# same assignment for the second variable
y = int(10)

# because the first two variables have their values assigned past these lines, we can print the sum 
# of those two variables
sum = (x + y)
# we use string concatenation again for this variable

print(sum)
# the result is 18 because 8 + 10 is 18


# Coding is Cool