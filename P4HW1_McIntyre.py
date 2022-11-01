# CTI 110
# P4HW1 - Grade List
# Emma McIntyre
# 11/1/22

# Ask the user for 6 grades for the 6 modules.
# Add them to a list.

grades = []

for grade in range(6):
    grade = float(input("Enter grade: "))
    grades.append(grade)

print("-"*10, "Results", "-"*10, sep="")
print("The grades are: ", grades)
# max(grades) and min (grades)
# to show lowest and highest in the list
print("Lowest Grade:    ", min(grades))
print("Highest Grade:   ", max(grades))
print("Sum of Grades:   ", sum(grades))
print("Average:         ", f"{(sum(grades) / 6):.2f}")
print("-"*30)
