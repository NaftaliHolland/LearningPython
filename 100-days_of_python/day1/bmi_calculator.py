#This program calculates the Body Mass Ratio of someone
weight = input("Enter your weight in kgs: ")
height = input("Enter your height in Meters: ")

bmi = (float(weight) / (float(height)) ** 2)

print(int(bmi))
