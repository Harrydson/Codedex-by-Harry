# Write code below 💖
"""Instructions
U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨

First, ask the user to enter their grade as an integer.

Create a four-year high school grade system using an if/elif/else statement:

grade is 9, print 'Freshman'
grade is 10, print 'Sophomore'
grade is 11, print 'Junior'
grade is 12, print 'Senior'
Everything else is 'TBD'
Get help
Hint
You can ask the user for a grade integer by:

grade = int(input('Enter your grade level: '))

To check if grade is equal to 9:

if grade == 9:
  print('Freshman')

Now what else should go underneath to turn the if statement into an if/elif/else statement?

Ask the community
Still want help? Get live help from other learners in our Discord.

Hint
You can ask the user for a grade integer by:

grade = int(input('Enter your grade level: '))

To check if grade is equal to 9:

if grade == 9:
  print('Freshman')

Now what else should go underneath to turn the if statement into an if/elif/else statement?
"""
# Highschool grade program
grade = int(input("Enter your grade:"))

if grade == 9: 
  print ('Freshman')
elif grade == 10: 
  print ('Sophomore')
elif grade == 11: 
  print ('Junior')
elif grade == 12: 
  print ('Senior')
else: 
  print('TBD')
