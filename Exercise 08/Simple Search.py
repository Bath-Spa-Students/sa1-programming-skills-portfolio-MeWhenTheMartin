

"""
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
"""

list = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
target = "Sam"

for i in list: # search all item in list
    if i == target: # found?
        print(f"Found Sam!")
        break
    else:
        print("Sam is not on the list...")
        break