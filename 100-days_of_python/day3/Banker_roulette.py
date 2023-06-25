import random

names = input("Give me names separated by a comma and a space :")

names = names.split(", ")

random_number = random.randint(0, len(names))

print("{} is going to pay the bill today".format(names[random_number]))