# Write code below 💖
"""Instructions
Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do is call!

Ask the user the month number using the input() function.

Check for the four seasons using an if/elif/else statement and logical operators:

month is 1, 2, 3, print 'Winter 🌨️'
month is 4, 5, 6, print 'Spring 🌱'
month is 7, 8, 9, print 'Summer 🌻'
month is 10, 11, 12, print 'Autumn 🍂'
Everything else is 'Invalid'
Logical operators in Python include the and and or keywords. Which one should you use?

Hint
To use the or logical operator:

if condition1 or condition2 or condition3:
  # some code

To use the and logical operator:

if condition1 and condition2 and condition3:
  # some code

Remember that if hour == 1 or 2 or 3: is not correct. This is a common error, but Python won't treat those as real comparisons. The correct way to write it is if hour == 1 or hour == 2 or hour == 3:.

Make sure it's 🌨️ not 🌧️!

"""
#seasons of the year
month = int(input("Enter your month number:"))
if month == 1 or month == 2 or month == 3 :
  print ('Winter 🌨️')
elif month == 4 or month == 5 or month == 6 :
  print ('Spring 🌱')
elif month == 7 or month == 8 or month == 9 : 
  print('Summer 🌻')
elif month == 10 or month == 11 or month == 12 : 
  print ('Autumn 🍂')
else:
  print('Invalid')  