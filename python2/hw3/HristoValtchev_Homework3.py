#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #3
# 4/27/2020
# Square
#-----------------------------------------------------------------------------------------------#

# Dice - count totals in user-defined number of rounds

import random

class Bin():
    def __init__(self, binIdentifier):
        # This method runs whenever you create a Bin object
        pass

    def reset(self):
        # This is called when you start or restart
        pass

    def increment(self):
        # Called when the roll total is the value of the binIdentifier
        pass

    def show(self, nRoundsDone):
        # Called at the end to show the contents of this bin
        pass


# Build a list of Bin objects            
binList = [ ]  # start off as the empty list
# Here, you need to write a loop that runs 13 times (0 to 12)
# In the loop create a Bin object, and store the object in the list of Bins
# (We won't use binList[0] or binList[1])

    
while True:
    nRounds = input('How many rounds do you want to do? (or Enter to exit): ')
    if nRounds == '':
        break
    nRounds = int(nRounds)

    # Tell each bin object to reset itself
    for oBin in binList:
        oBin.reset()
        
    # For each round (build a loop):
    #     roll two dice
    #     calculate the total
    #     and tell the appropriate bin object to increment itself


    print()
    print('After', nRounds, 'rounds:')
    # Tell each bin to show itself
    for oBin in binList:
        oBin.show(nRounds)
    print()

print('OK bye')
