# Adding game version 4

import random
from FileReadWrite import *  # means import everything as though it were typed here

DATA_FILE_PATH = 'AddingGameData.txt'


# Start up code
if not fileExists(DATA_FILE_PATH):
    userName = input('You must be new here, please enter your name: ')
    score = 0
    nProblems = 0
    nCorrect = 0
    
    print('To quit the game, press RETURN/ENTER and your info will be saved')
    print('OK', userName, "let's get started ...")
    print()
else:  # Found the file, read it.
    # File looks like this:
    # <score>,<userName>,<nProblems>,<nCorrect>
    savedDataString = readFile(DATA_FILE_PATH) #read the whole file into a variable
    savedDataList = savedDataString.split(',') # turn that into a list
    score = savedDataList[0]  # element zero is the score as a string
    score = int(score)
    userName = savedDataList[1]
    nProblems = int(savedDataList[2])
    nCorrect = int(savedDataList[3])
    
    print('Welcome back', userName, 'nice to see you again! ')
    print('Your current score is: ', score)
    print()

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
    nProblems = nProblems + 1

    if userAnswer == correctAnswer:
        print('Yes, you got it!')
        score = score + 2
        nCorrect = nCorrect + 1

    else:
        print('No, sorry, the correct answer was:  ', correctAnswer)
        score = score - 1
        
    print('Your score is:', score)
    print()

print('Thanks for playing')
print()
print('You have tried', nProblems, 'problems and you have correctly answered', nCorrect)   

# Create a list of strings
dataList = [str(score), userName, str(nProblems), str(nCorrect)]
# Use the join function to create a string that looks like this:
# <score>,<userName>,<nProblems>,<nCorrect>
outputText = ','.join(dataList)
# Write that string out to the file
writeFile(DATA_FILE_PATH, outputText)


