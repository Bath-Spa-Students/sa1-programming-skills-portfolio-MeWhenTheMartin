# this is a comment
print("Martin begins his first python scripts")

# information about me and my experiences
print("\nAbout me:")
# \n and \t are to make spaces when printing, \n to print in a new line, \t for horizontal tab

# using triple quotaion marks, you can print multiple lines at once without having to print over and over
print("""I have scripting experience on Scratch, Lua & C++.
Crativity is my passion, as I do most things myself
which includes making music, art, story and designs.
""")

print("vv scripting excersises vv")

# print out when the if statement is true
if 5 > 2:
    print("5 is a greater number than 2!")

# below is a variable which stores values
i = 2

# this while loop repeats 6 times
print("counting from 2 till 5...")
while i < 6:
    print(i)
    i += 1
print("loop ends...")

### Exercise 1 | Creating 3 poems

i = 1
# Poem 1
print("Poem #",i,"...")

print("""
The studs of a tree
branches greeting far
it gives our world a treat
never cut all deal
for all are thrown
were only left with frowns
""")

i += 1
# Poem 2
print("Poem #",i,"...")

print("""
When the skies gloom
greatness are to blame
with the flowers bloom
greatness comes to fame
""")

i += 1
# Poem 3
print("Poem #",i,"...")

print("""
Might
Night
Flight
Fight
""")

i += 1

""" this is a multi-
line comment, it serves the same purpose as a comment but with
multiple
lines """

# integer - Numbers (10)
# Float - Decimal (1.0235)
# String - Letters ("String")
# Boolean - True/False (True)

# list of variables
a = "hello!"
b = "did you know"
c = "you can print"
d = "multiple variables"
e = "at once?"

# print all at once using "," to separate the values
print(a,b,c,d,e)

# we can utilize printing multiple variables like this

# redefine old variables
a = 2
b = 1
# the sum
c = a+b
# the difference
d = a-b
print(a,"+",b,"=",c)
print(a,"-",b,"=",d)

### String Concatenation
Test1 = """
woah! """ + "it's bleh"
print(Test1)

print("writing a " + "string like this works " + "however it is really unessesary.")

print("empty quotations also" + " " + "spaces out strings")

# f-string as in (formatting), when you put in {} brackets it automatically takes the variable in said bracket

age = 60
print(f"You are {age} years old.")

# Arrays
array = ["one","two","three"]

# BODMAS & More print functions

# a delimiter is to take the second print statement into the first shown on lin 122
print("9/2 + (2+2) would be:", end=' ')
# Calculations follow the BODMAS rule, [Brackets, Powers/Roots, Division, Multiplication, Addition, Subtraction]
print(9/2 + (2+2))

# More Print Functions

September = 999
print("September Day:")
print(September )

### elif

cirno = 300
clownpeice = 200
a = cirno
b = clownpeice
if b > a:
    print("clownpeice's the strongest!")
elif a == b:
    print("tied in strength!")
else:
    print("cirno's the strongest!")

### Lists

# Homogenus
Homo =["Sunny Milk", "Luna Child", "Star Saphhire"]
print(Homo)
# Heterogenus
Hetero =["ZUN", 60, 3.74]
print(Hetero)

### Loops
count = 0
goop = True

while goop:
    if count < 9:
        count += 1
    else:
        goop = False
        break

### Function

def get_message():
    message = "Hallo"
    print(message)

get_message()