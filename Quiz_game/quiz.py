print("Welcome to my game")

playing = input("Do you want to play? ")

playing = playing.lower()

if playing in ['n', 'no']:
    quit()
#    print("Why")
elif playing in ['y', 'yes']:
    print("Nice, let's play")
    answer = input("What does cpu stand for \n")
    if answer == "central processing unit":
        print("You are smart :)")

else:
    print("It's a yes or no question")
