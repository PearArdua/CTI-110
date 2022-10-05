# Adjusting Output Alignment for Travel Expenses
# 10/4/2022
# CTI-110 P2HW1 - Travel
# Emma McIntyre
#

"""
This program is designed to recieve budget information and calculate.
User will be asked to provide budget, destination, fuel cost, hotel cost, and food cost.
The code will that the information, add up the expenses, and subtract the total from the budget.
Then it will print out the initial budget and destination, totals for the user to see, and at the end display how much from the budget will be left.
All exactly the same as the previous travel budget project, but this time with nice output alignment.
"""

# Introduce program to user
print("This program calculates and displays travel expenses")

# Ask user to enter their budget
userBudget = float(input("\nEnter Budget: "))

# Ask user to enter travel destination
userDestination = input("\nEnter your travel destination: ")

# Ask user for amount they will spend on gas
gasCost = float(input("\nHow much do you think you will spend on gas? "))

# Ask user for amount they will spend on accomodation
hotelCost = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

# Ask user for amount they will spend on food
foodCost = float(input("\nLast, how much do you need for food? "))

# Add expenses
finalCosts = gasCost + hotelCost + foodCost

# Subtract expenses from budget
finalBalance = userBudget - finalCosts

# Display results
print("\n","-"*12,"Travel Expenses","-"*12,sep='')
print("Location:          ", userDestination)
print("Initial Budget:     $", userBudget, sep='')
print("Fuel:               $", gasCost, sep='')
print("Accomodation:       $", hotelCost, sep='')
print("Food:               $", foodCost, sep='')
print("-"*40)
print("\nRemaining Balance:  $", finalBalance, sep='')


