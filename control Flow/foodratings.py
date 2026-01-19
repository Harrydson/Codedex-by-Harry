# Write code below 💖
"""Instructions
In a five-star restaurant review system (⭐️⭐️⭐️⭐️⭐️), the stars typically represent the different levels of satisfaction.

But what does each of the stars mean?

Start by creating a rating variable and set it equal to a decimal number.

Make a rating system using an if/elif/else statement:

rating greater than 4.5, print 'Extraordinary'
rating greater than 4, print 'Excellent'
rating greater than 3, print 'Good'
rating greater than 2, print 'Fair'
Everything else, print 'Poor'
Get help
Hint
For a refresher, to create a conditional statement:

if condition1:
  # some code
elif condition2:
  # some code
else:
  # some code
The solution needs to be exactly what's being asked!

For example:

Make sure it's > 4.5 instead of >= 4.5
Make sure it's 3 instead of 3.0
Ask the community
Still want help? Get live help from other learners in our Discord.

Hint
For a refresher, to create a conditional statement:

if condition1:
  # some code
elif condition2:
  # some code
else:
  # some code

The solution needs to be exactly what's being asked!

For example:

Make sure it's > 4.5 instead of >= 4.5
Make sure it's 3 instead of 3.0
"""
rating = float(input("Enter your rating:"))

if rating > 4.5: 
  print("Extraordinary")
elif rating > 4: 
  print("Excellent")
elif rating > 3: 
  print("Good")
elif rating > 2: 
  print("Fair") 
else: 
  print ("Poor")