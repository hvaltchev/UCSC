# Dice - count doubles in user-defined number of rounds

import random

# simulate rolling a six-sided die and return its value
def rollADie():    
    # generate a random numbers between 1 and 6
    roll = random.randrange(1, 7)
    return roll

nDoubles = 0

maxRounds = input('How many rounds do you want to do? ')
maxRounds = int(maxRounds)

for roundNumber in range(0, maxRounds):
    die1 = rollADie()
    die2 = rollADie()
    
    if die1 == die2:
        nDoubles = nDoubles + 1
        
percent = (nDoubles * 100.0) / maxRounds
print('Out of', maxRounds, 'you rolled', nDoubles, 'doubles, or', percent, '%')
