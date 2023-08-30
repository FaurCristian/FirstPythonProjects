student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for grades in student_scores:
    scores = student_scores[grades]
    if scores >= 91 and scores <= 100:
        student_grades[grades] = "Outstanding"
    elif scores >= 81 and scores <= 90:
        student_grades[grades] = "Exceeds Expectations"
    elif scores >= 71 and scores <= 80:
        student_grades[grades] = "Acceptable"
    elif scores < 70:
        student_grades[grades] = "Fail"

print(student_grades)
