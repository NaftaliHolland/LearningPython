#This is a tip calculator

print("Welcome to the tip calculator.\n")
total_bill = input("What is the total bill? $")
percentage_tip = input("What percentage tip would youlike to give? 10, 12 or 15? ")
people = input("How many people are spliting this bill? ")

total_amount_paid = float(total_bill) + (float(total_bill) * (float(percentage_tip) / 100))
paid_per_person = total_amount_paid / int(people)

print("Each person should pay: ${:.2f}".format(paid_per_person))

