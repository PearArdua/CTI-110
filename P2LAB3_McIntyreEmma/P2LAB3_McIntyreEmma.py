# CTI 110
# P2LAB3 - Food Receipt Pt 1
# Emma McIntyre
# 9/29/2022


# Food name
foodName = str(input("Enter food item name:\n"))

# Food price
foodPrice = float(input("Enter item price:\n"))

# Food quantity
foodAmount = int(input("Enter item quantity:\n"))

# Calculate first cost
totalCost = foodPrice * foodAmount

# Print Receipt
print("\nRECEIPT")
print(foodAmount, " ", foodName, " @ $", f'{foodPrice:.2f}'," = $", f'{totalCost:.2f}',sep="")
print("Total cost: $",f'{totalCost:.2f}',sep="")

