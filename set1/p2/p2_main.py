
# Name: EGIE BOY P. DELA CRUZ
# Section: IV-BSIT A
# Activity: P2
# Date: November 18, 2026

import student_utils
from student_utils import calculate_average
import datetime

print("===================================")
print("       P2 - STUDENT GRADE REPORT")
print("===================================")

print("Name: EGIE BOY P. DELA CRUZ")
print("Section: IV-BSIT A")
print("Date Generated:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("-----------------------------------")

number_of_grades = int(input("Enter number of grades: "))

grades = []

for i in range(number_of_grades):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

average = calculate_average(grades)
status = student_utils.determine_pass_fail(average)
highest = student_utils.get_highest_grade(grades)
lowest = student_utils.get_lowest_grade(grades)

print("\n========== STUDENT RESULTS ==========")
print(f"Average Grade: {average:.2f}")
print(f"Status: {status}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
print("=====================================")
