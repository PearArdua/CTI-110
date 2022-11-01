# CTI 110
# P4HW1 - Grade List
# Emma McIntyre
# 11/1/22

# Ask the user for 6 grades for the 6 modules.
# Add them to a list.

grades = []
for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)
    
print(grades)
