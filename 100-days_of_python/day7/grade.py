#A program tha maps names to grades in a dictionary
student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Nevile" : 62,
}

student_grades = dict()

for student in student_scores:
    if 100 >= int(student_scores[student]) >= 91:
        student_grades[student] = "Outstanding"
    elif 90 >= int(student_scores[student]) >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif 80 >= int(student_scores[student]) >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)