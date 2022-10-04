# CTI 110
# P3T2 - Ranges with if
# Emma McIntyre
# 10/4/22

grade = int(input("Enter number grade: "))

if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade < 80:
    letterGrade = "C or less"

print("\nYour letter grade is", letterGrade)
