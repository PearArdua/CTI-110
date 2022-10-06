# CTI 110
# P3T3 - Nested If Statements
# Emma McIntyre
# 10/6/22

"""
To qualify:
    - must have salary > 30 000
    - must have worked current job 2+ years

Ask user for salary and time worked at job
Check if salary qualifies
    If it does...
    Check if years_worked >= 2
         If both are true, they qualify
"""

# List Variables
salary = 0
yearsWorked = 0

# Ask the user for salary
salary = int(input("Enter salary: "))

# Ask the user for yearsWorked
yearsWorked = int(input("Enter years worked at current job: "))

# Process information & provide output

if salary < 30000:
    print("Not Qualified - Salary too low.")
else:
    if yearsWorked < 2:
        print("Not Qualified - Not held job long enough.")
    else:
        print("Congratulations, you qualify!")
