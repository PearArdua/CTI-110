# Calculating Travel Expenses
# 9/29/2022
# P1HW2_Using IDLE_TravelExpense
# Emma McIntyre
#

"""
This program is designed to recieve budget information and calculate.
User will be asked to provide budget, destination, fuel cost, hotel cost, and food cost.
The code will that the information, add up the expenses, and subtract the total from the budget.
Then it will print out the initial budget and destination, totals for the user to see, and at the end display how much from the budget will be left.
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
print("\n","-"*12,"Travel Expenses","-"*12,sep="")
print("Location:", userDestination)
print("Initial Budget:", userBudget)
print("\nFuel:", gasCost)
print("Accomodation:", hotelCost)
print("Food:", foodCost)
print("\nRemaining Balance:", finalBalance)


