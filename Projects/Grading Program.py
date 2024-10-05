student_scores={
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    grade = student_scores[key]
    if grade >= 91:
        grade = "Outstanding"
    elif grade >= 81:
        grade = "Exceeds Expectations"
    elif grade >= 71:
        grade = "Acceptable"   
    else:
        grade = "Fail" 
    
    student_grades[key]=grade
print(student_grades)
