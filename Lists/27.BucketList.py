# Write code below 💖
"""Here's a recap of the chapter:

Lists are used to store different items in a single variable.
An index is an item's position in a list. Python lists are 0-indexed.
Slicing can access certain parts of a list with name[start:end].
Python has built-in functions like len(), max(), min().
Lists have built-in methods like .append(), .insert(), .remove(), .pop().
We can iterate over a list using for-in.
"""

things_to_do = [
  '🚀 Create the dopest learn to code platform ever.',
  '⛰️ Hike the Pacific Crest Trail.',
  '🏡 Build an A-frame house and raise some goats.',
  '🌏 Live somewhere in Asia for a year.',
  '🎸 Release an album.',
  '📝 Write a book.',
  '🏆 Reach 100k subscribers on YouTube.',
  '🚐 Road trip with the fam.',
  '🍳 Open a cozy diner upstate.',
  '👴🏻 Grow old with no regrets.'
]
print(things_to_do)
for i in range(len(things_to_do)):
  print(things_to_do[i])