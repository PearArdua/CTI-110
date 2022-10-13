# CTI 110
# P3LAB - Leap Year
# Emma McIntyre
# 10/13/22

"""
1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.),
he year must be evenly divisible by 400

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines
whether that year is a leap year.
"""

print("This program will tell you if a year is a leap year or not.")
year = int(input("Enter Year: "))
isLeap = False # unless we find it is

# Let's rule out years first

if year % 4 != 0:
    isLeap = False
else:
    isLeap = True
# This covers all the cases except for the '00 dates
if year % 100 == 0: # it's a century
    # must be divisible by 400 or not leap year
    if year % 400 == 0:
        isLeap = True
    else:
        isLeap = False
 
# Print the answer at the end
if isLeap == True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
