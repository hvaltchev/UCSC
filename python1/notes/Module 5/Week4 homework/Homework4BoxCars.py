# Roll Box cars

import random

def rollBoxCars():
    nRolls = 0
    while True:
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        nRolls = nRolls + 1
        if (die1 == 6) and (die2 == 6):
        # or, if (die1 + die2) == 12:
            break
    return nRolls

# Main code
roundCounter = 0
totalRolls = 0
while True:
    howManyThisRound = rollBoxCars()
    roundCounter = roundCounter + 1
    totalRolls = totalRolls + howManyThisRound
    print('Round #', roundCounter, 'took', howManyThisRound, 'rolls')

    goAgain = input('Press Enter to go again, or q to quit: ')
    if goAgain == 'q':
        break
    print()

average = totalRolls / roundCounter
print()
print('On average, it took', average, 'to rolls to get box cars.')
    
