#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #4 BONUS
# 3/20/2020

#-----------------------------------------------------------------------------------------------#

import random

QUARTER_VALUE = .25
DIME_VALUE = .10 
NICKEL_VALUE = .05
PENNY_VALUE = .01


def countChange(nQuarters, nDimes, nNickels, nPennies):
    total = nQuarters * QUARTER_VALUE + nDimes * DIME_VALUE + nNickels * NICKEL_VALUE + nPennies * PENNY_VALUE
    return total

while(True):
    print('\n================================ Restart =====================================')
    name = input('What is your name (Return/Enter to quit)? ')
    if name == 'q':
        print('Bye')
        break
    else:
        nQuarters = int(input('How many quarters do you have? '))
        nDimes = int(input('How many dimes do you have? '))
        nNickels = int(input('How many nickels do you have? '))
        nPennies = int(input('How many pennies do you have? '))

        total = countChange(nQuarters, nDimes, nNickels, nPennies)
        print('\nAll counted,', name, f'has: ${total:.2f}')
        
        #RANDOM MSG
        rand = random.randint(1,3)
        if rand == 1:
            print('Wow, thats a lot of money!')
        elif rand == 2:
            print('Need to save more.')
        elif rand == 3:
            print('Time to put cash into the bank.')
