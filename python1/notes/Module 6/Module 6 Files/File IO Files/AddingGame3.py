# Adding game version 3

import random
from FileReadWrite import *  # means import everything as though it were typed here

DATA_FILE_PATH = 'GameData.txt'


# Start up code
if not fileExists(DATA_FILE_PATH):
    score = 0
    print('Hi, and welcome to my adding game!')
else:  # Found the file, read it.
    score = readFile(DATA_FILE_PATH)
    score = int(score)
    print('Welcome back.  Your saved score was:', score)

# Main loop

while True:
    firstNumber = random.randrange(0, 11)
    secondNumber = random.randrange(0, 11)
    correctAnswer = firstNumber + secondNumber
    
    question = 'What is: ' + str(firstNumber) + ' + ' + str(secondNumber) + '?  '
    userAnswer = input(question)
    if userAnswer == '':    
        break  # exits the loop
    userAnswer = int(userAnswer)

    if userAnswer == correctAnswer:
        print('Yes, you got it!')
        score = score + 2

    else:
        print('No, sorry, the correct answer was:  ', correctAnswer)
        score = score - 1
        
    print('Your score is:', score)
    print()

writeFile(DATA_FILE_PATH, str(score))
print('Thanks for playing')

