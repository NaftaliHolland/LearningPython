import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
while True:
    computer = random.choice(game)
    user = int(input("What is your answer 0 for rock 1 for paper and 2 for scissors: "))
    if user not in [0, 1, 2]:
        print("Enter valid answer 0 for rock 1 for paper 2 for scissors")
    else:
        break

print("computer chose \n{}".format(computer))
print("You chose \n{}".format(game[user]))
    
if computer == rock and user == 2:
    print("Computer wins")
elif computer == scissors and user == 1:
    print("computer wins")
elif computer == paper and user == 0:
    print("Computer wins")
elif computer == game[user]:
    print("Draw")
else:
    print("You win")