# CTI 110
# P1LAB4 - Apple Sales
# Emma McIntyre
# 9/20/22

# write a program to advertise apples
#  The salesperson's name is <use your name>, and they have 100 apples for sale. Each apple costs 25 cents.
# write a program which displays the salesperson's store name, the number of apples, price per apple, and the price to purchase all of them at once.

# Declare variables
name = "McIntyre"
numApples = 100
costPerApple = 0.25
totalCost = 0 # This is what we're calculating

# Greet the user
print("Hello, welcome to the", name, "Apple Farm.")

# Tell them the information above
print ("We have", numApples, "apples in stock.")
print("They cost $", costPerApple, "each.")

# Calculate the total cost (num apples times cost per apple)
totalCost = numApples * costPerApple

# Tell user the total cost of the apple
print("The total cost for", numApples, "apples will be: $",f"{totalCost:.2f}") # format 2 decimal points