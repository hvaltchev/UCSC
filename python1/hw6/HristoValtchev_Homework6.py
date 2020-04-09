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

#init new player
userName = input('Please enter your name:')
nCoins = 100

#if not fileExists(DATA_FILE_PATH):
#    #print('You have', nCoins, 'coins to start.  Good luck.')
#    print('No existing players.')
#else:
myFileData = readFile(DATA_FILE_PATH)
print(myFileData)
    
myFileList = myFileData.split(',')
print(myFileList)
    
    #search list for name and assign name and score to nCoins and userName
    #player already existis

print(myFileList.count(userName))
if myFileList.count(userName) == 1:
    print('Existing Player')
    index = myFileList.index(userName)
    print(index)
    score = myFileList[index - 1]
    print(score)
    nCoins = int(score)
    userName = myFileList[index]
    print('Welcome back', userName)
    print('Your previous score was:', nCoins)
    #player is new
#else:
#        print('New Player') 
print()

#initialize reel
reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', 
              'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries',
              'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7']
nPicturesInReel = len(reelList)

#initial number of coins
#nCoins = 100

#Game is being initialized
#print()
#print('You have', nCoins, 'coins to start.  Good luck.')
#print()

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

    bet = input('How many coins do you want to bet (defaults to 1, enter 0 to quit): ')

    #check for enter 
    if bet == '':
        bet = 1
    
    #check for int
    try:
        bet = int(bet)
        #exit condition
        if bet == 0:
            #save name and score to a file
            print('TIME TO WRITE TO A FILE')
            #prep line to write
            writeString = str(nCoins) + ',' + userName + ','  
            #check if it exits
            #------------------#
                

            #write to file
            writeFile(DATA_FILE_PATH, writeString)

            break
        
        #negative number
        if bet < 0:
            print('Invalid input negative number.')
            continue
        
        #check for enough coins 
        if bet > nCoins:
            print('Sorry, you do not have that many coins, you only have:', nCoins)
            continue

    except ValueError:
        print('Invalid input. You entered a invalid number or string.')
        continue

    resultList = []
    for spin in range(3):
        thisReelIndex = random.randrange(0, nPicturesInReel)
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print( 'Spinning ... ')
    print()
    time.sleep(.5)
    print( '     ', resultList[0])
    time.sleep(.5)
    print( '     ', resultList[1])
    time.sleep(.5)
    print( '     ', resultList[2])
    print( )
        
    nCoins = nCoins - bet

    payOut = bet * payTable(resultList)
    
    if payOut  == 0:
        print( 'Sorry - you lose.')
    else:
        print( 'You won', payOut, 'coins. Cha-ching!')
        if payOut > 50:
            print( 'WOOOOO HOOOOOOOOOOO!!!!')
            
    nCoins = nCoins + payOut

    print( 'You now have', nCoins, 'coins.')
    print()

print( 'Sorry to see you go. Come back again soon.')
    
