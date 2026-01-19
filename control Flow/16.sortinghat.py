# Write code below 💖
"""
16.sortinghat.py
by:harrydson zambrano
date: 1-16-2026
# Congrats!
Here's a recap of everything we learned so far:

Control flow is the order in which the program's code executes.
if statement tests a condition for truth and executes the code if it's True.
elif clause can be added between if and else.
else executes the code if none of the above is True.
Relational operators are used to compare two values: ==, !=, >, >=, <, <=.
Logical operators are used to combine two or more conditions: and, or, not.
Here's an if/elif/else statement in action just in case:

if review >= 4.5:
  print('Extraordinary')
elif review >= 4:
  print('Excellent')
elif review >= 3:
  print('Good')
else:
  print('Eh')"""

gryffindor = 0
ravenclaw = 0 
hufflepuff = 0 
slytherin = 0


print ("============Sorting Hat===========")

#1st question:
print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
answer = int(input("Enter your answer (1-2): "))

if answer == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif answer == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print("Wrong input.")

#2nd question:

print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer = int(input("Enter your answer (1-4): "))

if answer == 1: 
  hufflepuff = hufflepuff + 2
elif answer == 2:
  slytherin = slytherin + 2
elif answer == 3: 
  ravenclaw = ravenclaw + 2
elif answer == 4: 
  gryffindor = gryffindor + 2
else:
  print("Wrong input.")

#3rd question:

print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer = int(input("Enter your answer (1-4): "))

if answer == 1:
  slytherin = slytherin + 4
elif answer == 2:
  hufflepuff = hufflepuff + 4
elif answer == 3: 
  ravenclaw = ravenclaw + 4
elif answer == 4: 
  gryffindor = gryffindor + 4
else:
  print("Wrong input.")

print("gryffindor: ", gryffindor)
print("ravenclaw: ", ravenclaw)
print("hufflepuff: ", hufflepuff)
print("slytherin: ", slytherin)


if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print("gryffindor!")
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print("ravenclaw!")
elif hufflepuff >= slytherin:
  print("hufflepuff!")
else:
  print("slytherin!")