''' Type your code here. '''
milesPerGallon = 0 #float
costPerGallon  = 0 #float in $

# Ask the user for milesPerGallon
milesPerGallon = float(input())
# Ask the user for costPerGallon
costPerGallon = float(input())

# figure out the cost to drive 20 miles
# gallons burned in 20 miles is: 20 miles / mpg
gallonsUsedIn20 = 20 / milesPerGallon
costToDrive20   = float(gallonsUsedIn20 * costPerGallon)

#cost to drive 75 miles
gallonsUsedIn75 = 75 / milesPerGallon
costToDrive75   = float(gallonsUsedIn75 * costPerGallon)

#cost to drive 500 miles
gallonsUsedIn500 = 500 / milesPerGallon
costToDrive500   = float(gallonsUsedIn500 * costPerGallon)

# print out the cost in $
print(f'{costToDrive20:.2f} {costToDrive75:.2f} {costToDrive500:.2f}')

#TODO: also do 75 and 200 miles.