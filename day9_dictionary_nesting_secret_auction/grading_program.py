student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
'''
This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
'''
#TODO-2: Write your code below to add the grades to student_grades.👇
for s_key in student_scores:
    if 91 <= student_scores[s_key] <= 100:
        student_grades[s_key] = "Outstanding"
    elif 81 <= student_scores[s_key] <= 90:
        student_grades[s_key] = "Exceeds Expectations"
    elif 71 <= student_scores[s_key] <= 80:
        student_grades[s_key] = "Acceptable"
    else:
        student_grades[s_key] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)