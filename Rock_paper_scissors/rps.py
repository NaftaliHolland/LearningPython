import random

user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]
while True:
    user_input = input(" Type R for Rock/P for paper /S for Scissors or q to exit \n")
    user_input = user_input.lower()

    if user_input == "q":
        print("Good bye!!")
        break
    elif user_input not in options:
        continue
    
    random_number = random.randint(0, 2) #0 : rock , 1: paper, 2: Scissors

    computer_pick = options[random_number]

    if user_input == "r" and computer_pick == "s":
        print("You Won")
        user_wins += 1
    elif user_input == "p" and computer_pick == "r":
        print("You won")
        user_wins += 1

    elif user_input == "s" and computer_pick == "p":
        print("You won")
        user_wins += 1

    else:
        print("You lost")
        computer_wins += 1

print(f"The computer won {computer_wins} times and you won {user_wins}")
print("Good bye!!")