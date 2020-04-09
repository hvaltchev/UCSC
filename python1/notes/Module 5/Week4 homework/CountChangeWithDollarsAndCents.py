import random

VALUE_OF_QUARTER = .25
VALUE_OF_DIME = .10
VALUE_OF_NICKEL = .05
VALUE_OF_PENNIES = .01

def countChange(nQuarters, nDimes, nNickels, nPennies):
    amountOfMoney = (nQuarters * VALUE_OF_QUARTER) + \
                                (nDimes * VALUE_OF_DIME) +\
                                (nNickels * VALUE_OF_NICKEL) + \
                                (nPennies * VALUE_OF_PENNIES)
    return amountOfMoney


while True:
    name = input('What is your name (Return/Enter to quit)? ')
    if name == '':
        break
        
    userQuarters = input('How many quarters do you have? ')
    userQuarters = int(userQuarters)
    userDimes = input('How many dimes do you have? ')
    userDimes = int(userDimes)
    userNickels = input('How many nickels do you have? ')
    userNickels = int(userNickels)
    userPennies = input('How many pennies do you have? ')
    userPennies = int(userPennies)

    total = countChange(userQuarters, userDimes, userNickels, userPennies)
    print()
    print('All counted,', name, 'has: $', total)
    
    # EXTRA CREDIT:
    total = int(total * 100)  # multiply by 100 to get toal as pennies - convert to integer
    nDollars = total // 100    # divide by 100 to get dollars
    nCents = total % 100    # go modulo 100 to get cents

    print('All counted,', name,  'has: ', nDollars, 'dollar(s) and', nCents, 'cents.')
    print()

    msgNumber = random.randrange(1, 4)
    if msgNumber == 1:
        print("Wow, that's a lot of money!")
    elif msgNumber == 2:
        print("Need to save more.")
    else:
        print("Time to put cash into the bank")

    print()

print('Bye')
