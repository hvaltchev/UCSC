# Irv's Restaurant
#

#Constants:
COST_PER_HAMBURGER = 3.00
COST_PER_HOT_DOG = 2.00
COST_PER_MILK_SHAKE = 3.00
TAX_RATE = .10

# Function to calculate a single bill
# Allows the caller to pass in three values

def calculateBill(nHamburgers, nHotDogs, nMilkShakes):
    
    # Calculate a subtotal by multiplying the number of each type of food
    # By the price of each, and adding those together
    subTotal = (nHamburgers * COST_PER_HAMBURGER) + \
               (nHotDogs * COST_PER_HOT_DOG) + \
               (nMilkShakes * COST_PER_MILK_SHAKE)

    # Calculate the tax
    tax = TAX_RATE * subTotal

    # Add subtotal and tax to give total
    total = subTotal + tax

    # Return the resulting total
    return total


# Calls to the above function

bill1 = calculateBill(3, 2, 1)
print('The bill for order number 1 is $', bill1)
bill2 = calculateBill(8, 8, 8)
print('The bill for order number 2 is $', bill2)

userBurgers = input('How many burgers do you want to order? ')
userBurgers = int(userBurgers)
userDogs = input('How many hot dogs do you want to order? ')
userDogs = int(userDogs)
userShakes = input('How many milk shakes do you want to order? ')
userShakes = int(userShakes)
bill3 = calculateBill(userBurgers, userDogs, userShakes)
print('The bill for order number 3 is $', bill3)

allBills = bill1 + bill2 + bill3
print('The sum of all bills is:', allBills)
