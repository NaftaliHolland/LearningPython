#password generator project

import random

#list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#list of numbers

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#list of symbols

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
nr_letters = int(input("how many letters do you want in your password? "))
nr_numbers = int(input("How many numbers do you want in your password? "))
nr_symbols = int(input("How many symbols do you want in your password? "))
i = 0
#loop for generating random characters
#for em, letter in enumerate(letters):
while i < nr_letters:
    #if em == nr_letters:
     #   break
    password += random.choice(letters)
    i += 1
i = 0
#loop for generating random numbers
#for em, number in enumerate(numbers):
    #if em == nr_numbers:
        #break
while i < nr_numbers:
    password += random.choice(numbers)
    i += 1

i = 0
#loop for generating random symbols
#for em, symbol in enumerate(symbols):
 #   if em == nr_symbols:
  #      break
while i < nr_symbols:
    password += random.choice(symbols)
    i += 1

print(password)