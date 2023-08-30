student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


all_heights = 0

for height in student_heights:
    all_heights += height

number_students = 0

for number in student_heights:
    number_students += 1

average_height = round(all_heights / number_students)

print(average_height)
