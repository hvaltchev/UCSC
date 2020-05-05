#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #3
# 4/27/2020
# Square
#-----------------------------------------------------------------------------------------------#

# Dice - count totals in user-defined number of rounds

import random
import math

class Bin():
    def __init__(self, binIdentifier):
        # This method runs whenever you create a Bin object
        self.binIndentifier = binIdentifier
        self.count = 0

    def reset(self):
        # This is called when you start or restart
        self.count = 0

    def increment(self):
        # Called when the roll total is the value of the binIdentifier
        self.count = self.count + 1

    def show(self, nRoundsDone):
        # Called at the end to show the contents of this bin
        if self.binIndentifier > 1:
            percent = math.floor((self.count / nRoundsDone) * 100)
            # print(self.binIndentifier, ': count is', self.count, 'or', '{:.0%}'.format(self.count / nRoundsDone))
            print(self.binIndentifier, ':', '*' * percent, '{:.0%}'.format(self.count / nRoundsDone), '(', self.count, ')')


            # print('-' * percent)

# Build a list of Bin objects            
binList = []  # start off as the empty list
# Here, you need to write a loop that runs 13 times (0 to 12)
# In the loop create a Bin object, and store the object in the list of Bins
# (We won't use binList[0] or binList[1])

for x in range(0, 13):
    newBin = Bin(x)
    binList.insert(x, newBin)

while True:
    nRounds = input('How many rounds do you want to do? (or Enter to exit): ')
    if nRounds == '':
        break
    nRounds = int(nRounds)

    # Tell each bin object to reset itself
    for oBin in binList:
        oBin.reset()
        
    # For each round (build a loop):
    for n in range(0, nRounds):
        # roll two dice
        d1 = random.randrange(1, 7)
        d2 = random.randrange(1, 7)
        # calculate the total
        total = d1 + d2
        # and tell the appropriate bin object to increment itself
        binList[total].increment()

    print()
    print('After', nRounds, 'rounds:')
    # Tell each bin to show itself
    for oBin in binList:
        oBin.show(nRounds)
    print()

print('OK bye')
