# Declare the variables for pennies, nickels, dimes, quarters
pennies = 0.01
nickels = 0.05
dimes = 0.1
quarters = 0.25

# The program ask the user how many of each cent they have and compute the amount in dollars
pennies = int(input())
nickels = int(input())
dimes = int(input())
quarters = int(input())
print(0.01 * pennies + 0.05 * nickels + 0.1 * dimes + 0.25 * quarters)
