import random

print("=================== Rock Paper Scissors Lizard Spock ===================")

print("\n1) rock:✊")
print("2) Paper:✋")
print("3) Scissors:✌️")
print("4) Spock:🖖")
print("5) lizard:🦎") 

player_name= str(input("\nEnter your Name: "))

player = int(input("Enter your option 1-5: "))
computer = random.randint(1, 5)


if player == 1:
  print("rock:✊")
elif player == 2:
  print ("Paper:✋")
elif player == 3:
  print ("Scissors:✌️")
elif player == 4:
  print ("Spock:🖖")
else:
  print ("lizard:🦎")   

if computer == 1:
  print(" rock✊")
elif computer == 2:
  print(" paper✋")
elif computer == 3:
  print("scissors✌️")
elif computer == 4:
  print("lizard🦎")
else:
  print("spock🖖")

if player == computer:
    print("It's a tie!")
elif (
    (player == 1 and computer in [3, 4]) or
    (player == 2 and computer in [1, 5]) or
    (player == 3 and computer in [2, 4]) or
    (player == 4 and computer in [2, 5]) or
    (player == 5 and computer in [1, 3])
):
    print("winner: ", player_name)
else:
    print("Computer wins!")