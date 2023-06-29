import random
from os import system, name

words = ["Hello", "Mouce", "Getting", "Breath"]

word = (random.choice(words)).lower()

blanks = []
index = []

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("clear")

def get_blanks(n):
    for i in range(n):
        blanks.append("_")
    print(blanks)

get_blanks(len(word))

def wrong():
    clear_screen()
    for i in range(len(word)):
        if blanks[i] == "_":
            blanks[i] = word[i]
            break
    print(blanks)
    print("Wrong ")

def get_index(guess):
    for em, i in enumerate(word):
        if guess == i:
            index.append(em)

def correct(guess):
    clear_screen()
    get_index(guess)
    for i in index:
        if blanks[i] == "_":
            blanks[i] = guess
            print(blanks)
            print("correct")
            print(index)
            break


for i in range(len(word)):
    guess = input("Guess a letter ")
    if guess in word:
        correct(guess)
    else:
        wrong()