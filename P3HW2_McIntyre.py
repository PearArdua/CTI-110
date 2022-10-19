# CTI 110
# P3HW2 - Salary Calculator
# Emma McIntyre
# 10/18/22
"""
    Asks the user to name of employee
    Ask user to enter number of hours the employee worked this month
    Ask user to enter employee's pay rate
    Evaluate if employee has worked overtime.
    Calculate amount employee shoud be paid for regular hours worked.
    Display base pay (total amount that should be paid to employee before overtime)
    Display whether or not overtime pay is owed. (For Bronze, you don't have to calculate the amount owed.)
"""

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
otRate = 0
otPay = 0
overtime = 0
isOvertime = False
pay = 0
grossPay = 0

if hours <= 40:
    isOvertime = False
    pay = rate * hours
    overtime = "N/A"
    otRate = "N/A"
    otPay = "N/A"
    grossPay = pay    
else:
    isOvertime = True
    overtime = hours - 40
    pay = rate * 40
    otRate = rate * 1.5
    otPay = overtime * otRate
    grossPay = otPay + pay
    otPay = "$" + str(otPay)
pay = "$" + str(pay)
grossPay = "$" + str(grossPay)
rate = "$" + str(rate)


#alignment struggles
first = ["Hours Worked", "---------------", hours]
second = ["Pay Rate", "----------", rate]
third = ["OverTime", "----------", overtime]
fourth = ["OverTime Pay", "---------------", otPay]
fifth = ["RegHour Pay", "---------------", pay]
sixth = ["Gross Pay", "---------------", grossPay]

print("-"*35)
print("Employee name:  ", name, "\n")
for i in range(0, 3):
    print(f"{first[i] : <15}{second[i] : <10}{third[i] : <10}{fourth[i] : <15}{fifth[i] : <15}{sixth[i] : <15}")
    
