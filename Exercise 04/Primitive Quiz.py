

"""
In this exercise, you'll create a simple program that asks the user a question, 
evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization 
(e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. 
Provide feedback for each question.
"""
# Variables
Item = 0 # This is used for counting the item on the list
Points = 0
Q = "What is the capital of"

country = ["France", "Italy", "Russia", "Germany", "Spain", "Poland", "Sweden", "Switserland", "Portugal", "Czechia"]
city =    ["paris",  "rome",  "moscow", "berlin",  "madrid", "warsaw", "stockholm", "bern",  "lisbon", "prague"]

# for x in country: # This goes through every item on the list of countries
#    print(x)

while True:
   if Item < len(country): # Loop this when all the countries have not been covered yet. 
    print(Q, country[Item] + "?")
    answer = input().lower()
    if answer == city[Item]:
      print("Correct answer!")
      Points += 1 # give pointc if user gets a correct answer
    else:
      print("Incorrect answer...")
    Item += 1 # this rotates over the next question
    print(f"Current Points:{Points}")
   else: # if there are no more questions stop the loop
    print(f"Quiz completed! You've scored {Points}/{len(country)}")
    break


# Coding is Cool