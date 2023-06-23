#This program tells you how many days weeks and months you have left to reach 90 based on your current age
#It also assumes that the user will input a valid number :)
current_age = input("How old are you: ")
remaining_years = 90 - (int(current_age))
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

print("You have {} days, {} weeks and {} months left.".format(remaining_days, remaining_weeks, remaining_months))
