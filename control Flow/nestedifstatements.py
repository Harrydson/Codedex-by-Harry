"""

# Syntax
As our program gets longer and more complex, so does the decision-making of our code. You might've already run into situations where you want to check for another condition after a condition is true.

You know what else we can do with if/elif/else statements?

We can nest them inside one another! 🪹

A nested if statement is an if statement inside another if statement.

Suppose we have a simple if/else statement:

if age >= 18:
  print('You are old enough to apply for a loan.')
else:
  print('You are too young to apply for a loan.')

if age >= 18:
  if income >= 20000:
    print('You are eligible for a loan.')
  else:
    print('Your income is too low to be eligible for a loan.')
else:
  print('You are too young to apply for a loan.')
"""
#example of nested if statements
weather = 'Sunny'
humidity = 35

if weather == 'Sunny':
  if humidity < 60:
    print('Let’s go to the beach! 🏖️')
  else:
    print('Hmmm, it’s a little humid for a beach day.')
else:
  print('It’s not sunny today... let’s try for another day.')