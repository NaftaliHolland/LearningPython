print(""" _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \\ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___| 
  _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|
 
 """)
while True:
    print("Welcome to treasure Island Your Mission is to find the treasure.\n Good luck (press q at any point of the game to quit)")

    while True:
        crossRoad = input("You are at a cross road , where do you want to go? right or left . Enter q to quit ").lower()
        if crossRoad not in ["right", "left", "q"]:
            print ("ENTER RIGHT OR LEFT")
        else:
            break

    if crossRoad == "q":
        print("Good bye!!\n")
        quit()

    elif crossRoad == "right":
        print("You Fell into a hole\n GAME OVER")
        quit()

    while True:
        river = input("You are at a lake.There is an Island in the midle of the lake. Will you wait for a boat or swim ").lower()
        if river not in ["wait", "swim", "q"]:
            print("Will you swim or wait? ")
        else:
            break
    if river == "q":
        print("Good bye!!\n")
        quit()
    elif river == "swim":
        print("GAME OVER !! \n You were attacked by a trout and died \n BE PATIENT NEXT TIME AND WAIT FOR THE BOAT")
        quit()

    while True:
        door = input("Good job. You arrive to the island unharmed , there is a house with three doors one red, one yellow and one blue\n Which door will get in ").lower()
        if door not in ["red", "blue", "yellow", "0q"]:
            print("Enter a valid choice red, blue, yellow or q to quit")
        else:
            break
    if door == "q":
        print("Good bye!!\n")
        quit()

    elif door == "red":
        print("GAME OVER!!\n You were burnet by fire . Better luck next time")
        quit()

    elif door == "blue":
        print("GAME OVER!!\n You were eaten by beasts : Better luck next time\n")
        quit()
    print("You found the treasure, GOOD JOB!!\n What do you plan to do with this now that you are this rich\n (You don't have to answer that , don't always tell everyone your plans :)")
    while True:
        playon = input("Do you still want to play? yes or no ").lower()
        if playon not in ["yes", "no", "q"]:
            print("Enter a valid input yes , no or q to quit ")
        else:
            break
    if door in ["no", "q"]:
        print("Good bye!!\n")
        quit()

