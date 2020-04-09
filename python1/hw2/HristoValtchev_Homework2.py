#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #2 
# 3/6/2020

#-----------------------------------------------------------------------------------------------#

# Hamburger - $3 each
# Hot Dog - $2 each 
# Milk Shake - $3 each
# Write a function called 'calculateBill'
# Three parameters (nHamburgers, nHotdogs, nMilkshakes
# Calculate subtotal
# Add 10% tax
# Return total ammount of purchase
# Do not print in function
# Write three calls to the function 
# Test with input1: 3 hamburgers, 2 hotdogs, 1 milkshake = 16.00 + 1.60tax = 17.60
# Test with input2: 8 hamburgers, 8 hotdogs, 8 milkshake = 70.40
# Test with input3: User input for all 3 
# After each call of function add a print statement "Your bill is: $123.45"
# BONUS - Add up all three bills and print

def calculateBill(nHamburgers, nHotdogs, nMilkshakes):
    total = (3 * nHamburgers) + (2 * nHotdogs) + (3 * nMilkshakes)
    total = total + total * .10
    return total    
    
test1 = calculateBill(3, 2, 1) 
print(f"Your bill is: ${test1:.2f}")

test2 = calculateBill(8, 8, 8)    
print(f"Your bill is: ${test2:.2f}")

nHamburgers = int(input('Enter the number of Hamburgers: '))
nHotdogs = int(input('Enter the number of Hot Dogs: '))
nMilkshakes = int(input('Enter the number of Milk Shakes: '))

test3 = calculateBill(nHamburgers, nHotdogs, nMilkshakes)
print(f"Your bill is: ${test3:.2f}")

#Bonus
bonus = test1 + test2 + test3
print(f"The sum of all bills is: ${bonus:.2f}")  
