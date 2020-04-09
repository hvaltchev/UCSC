# Irv's Restaurant
#
# Function to calculate a single bill
# Allows the caller to pass in three values

def calculateBill(nHamburgers, nHotDogs, nMilkShakes):
    
    # Calculate a subtotal by multiplying the number of each type of food
    # by the price of each, and adding those together
    subTotal = (nHamburgers * 3.00) + \
               (nHotDogs * 2.00) + (nMilkShakes * 3.00)

    # Calculate the tax
    tax = .1 * subTotal

    # Add subtotal and tax to give total
    total = subTotal + tax

    # return the resulting total to the caller
    return total


# Calls to the above function

bill1 = calculateBill(3, 2, 1)
print 'The bill for order number 1 is $', bill1
bill2 = calculateBill(8, 8, 8)
print 'The bill for order number 2 is $', bill2

userBurgers = raw_input('How many burgers do you want to order? ')
userBurgers = int(userBurgers)
userDogs = raw_input('How many hot dogs do you want to order? ')
userDogs = int(userDogs)
userShakes = raw_input('How many milk shakes do you want to order? ')
userShakes = int(userShakes)
bill3 = calculateBill(userBurgers, userDogs, userShakes)
print 'The bill for order number 3 is $', bill3

allBills = bill1 + bill2 + bill3
print 'The sum of all bills is:', allBills
