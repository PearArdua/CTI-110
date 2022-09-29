# CTI 110
# P2LAB2 Driving Costs, Fixed
# Emma McIntyre
# 9/27/2022

# Convert from dog years to human years
"""
# Ask for dog age
dogs_age = int(input("Enter your dog's age: "))

# Convert to human age
human_age = dogs_age * 7

# Print the answer
#print(human_age)
print("If your dog is",
      dogs_age,
      ", that is",
      human_age,
      "in human years.")
"""
# Driving Costs Part 2

# 1. Ask for miles per gallon, cost per gallon
milesPerGallon = float(input("Enter Miles per Gallon: "))
costPerGallon = float(input("Enter Cost per Gallon: $ "))

# 2. Calculate cost per mile
costPerMile = costPerGallon / milesPerGallon

# 3. Multiply by number of miles
print("Cost to drive: " )
print("20 miles: $", costPerMile * 20)
print("75 miles: $", costPerMile * 75)
print("500 miles: $", costPerMile * 500)
