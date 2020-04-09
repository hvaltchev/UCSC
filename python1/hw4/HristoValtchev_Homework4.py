#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #4
# 3/19/2020

#-----------------------------------------------------------------------------------------------#

import random

#Function that returns the number of tries to get a 6
def isSix():
    rolls = 1
    while(True):
        if(random.randint(1,6) % 6 != 0):
            rolls = rolls + 1
        else:
            return rolls    

roundNumber = 1
average = 0 

while(True):
    #get 1st die roll
    die1Rolls = isSix()
    #get 2nd die roll
    die2Rolls = isSix()
    #total number of rolls total per round to get a 6
    totalRoundRolls = die1Rolls + die2Rolls
    average += totalRoundRolls
    #update the round number
    roundNumer = roundNumber + 1
    
    print('Round #', roundNumber, 'took', totalRoundRolls, 'rolls')
    choice = input('Press Enter to go again, or q to quit:')
    
    if(choice == 'q'):
        print('On average, it took', average / roundNumber , 'rolls to get box cars.')
        break

    roundNumber = roundNumber + 1
