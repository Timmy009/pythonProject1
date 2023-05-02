course1 = input("Enter the name of the first course: ")
course_grade1 = int(input("Enter the grade: "))
course2 = input("Enter the name of the second course: ")
course_grade2 = int(input("Enter the grade: "))
course3 = input("Enter the name of the third course: ")
course_grade3 = int(input("Enter the grade: "))

average = course_grade1 + course_grade2 + course_grade3 / 3

print(f"The average is of the three scores which are {course1} {course2} {course3} is  {average}")


smallest_grade = course_grade1

id(smallest_grade)
if course_grade2 < smallest_grade:
    smallest_grade = course_grade2

if course_grade3 < smallest_grade:
    smallest_grade = course_grade3

print("The smallest grade is ", smallest_grade)

largest_grade = course_grade3
if course_grade2 > largest_grade:
    largest_grade = course_grade2

if course_grade1 > largest_grade:
    largest_grade = course_grade1

print(f"The largest grade is {largest_grade}")
