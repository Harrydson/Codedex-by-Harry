# Write code below 💖
#while condition:
  # code inside  
guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  # update tries
  tries = tries + 1

if guess != 6:
  print('You run out tries')
else:
  print('You got it')