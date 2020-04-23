#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #6
# 04/02/2020

#-----------------------------------------------------------------------------------------------#

DATA_FILE_PATH = 'SlotMachineData.txt'

from FileReadWrite import *
import random
import time
import json

# User input for username
userName = input('Please enter your name: ')
nCoins = 100

# Create a dictionary which stores player name and score
playerDict = {userName: nCoins}

# Check if file exists
if True == fileExists(DATA_FILE_PATH):
    print('Existing File')
    # Open File for Reading
    handle = openFileForReading(DATA_FILE_PATH)
    line = readALine(handle)
    playerDict = line
    # Populate nCoins
    # print(line)
    try:
        nCoins = line[userName]
    except:
        playerDict.update({userName: nCoins})
        print(playerDict)
elif False == fileExists(DATA_FILE_PATH):
    print('Create a new File')
    handle = openFileForWriting(DATA_FILE_PATH)
    handle.close()

#initialize reel
reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', 
              'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries',
              'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7']
nPicturesInReel = len(reelList)

def payTable(myList):
    picture1 = myList[0]
    picture2 = myList[1]
    picture3 = myList[2]
    if myList.count(picture1) == 3:
        if picture1 == 'Lucky 7':
            nCoinsWon = 500
        elif picture1 == 'bar':
            nCoinsWon = 100
        else:
            nCoinsWon = 10
    else:
        if (picture1 == picture2) or (picture1 == picture3) or (picture2 == picture3):
            nCoinsWon = 2
        else:
            nCoinsWon = 0
    return nCoinsWon

while True:
    bet = int(input('How many coins do you want to bet (defaults to 1, enter 0 to quit): '))

    if bet == 0:
        break

    # Check for enter
    if bet == '':
        bet = 1

    # Negative number
    if bet < 0:
        print('Invalid input negative number.')
        continue
        
    # Check for enough coins
    if bet > nCoins:
        print('Sorry, you do not have that many coins, you only have:', nCoins)
        continue

    resultList = []
    for spin in range(3):
        thisReelIndex = random.randrange(0, nPicturesInReel)
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print( 'Spinning ... ')
    print()
    time.sleep(.5)
    print('     ', resultList[0])
    time.sleep(.5)
    print('     ', resultList[1])
    time.sleep(.5)
    print('     ', resultList[2])
    print()
        
    nCoins = nCoins - bet

    payOut = bet * payTable(resultList)
    
    if payOut == 0:
        print('Sorry - you lose.')
    else:
        print('You won', payOut, 'coins. Cha-ching!')
        if payOut > 50:
            print('WOOOOO HOOOOOOOOOOO!!!!')
            
    nCoins = nCoins + payOut

    print('You now have', nCoins, 'coins.')
    print()

print(userName, 'sorry to see you go. You currently have', nCoins, 'coins.')
playerDict[userName] = nCoins

# Cleanup
print(playerDict)
handle = openFileForWriting(DATA_FILE_PATH)
json.dump(playerDict, handle)
handle.close()