import random

top_of_range = input("Type a number that will be the top of you range ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("The number has to be greater than 0")
        quit()

else:
    print("Input a number next time")
    quit()
random_number = random.randrange(0, top_of_range)
guesses = 0

while True: #will keep asking until user gets the answer
    guesses += 1 #keeps track of the number of gueses made
    user_guess = input("What is your guess ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess == random_number:
            print("You got it champ")
            break
        elif user_guess < random_number:
            print("try again that was less than the answer\n")
        else:
            print("Try again, that was greater than the number\n")
    else:
        print("Enter a number!! ")
        continue
print(f"You got it in {guesses} guesses")
print(random_number)