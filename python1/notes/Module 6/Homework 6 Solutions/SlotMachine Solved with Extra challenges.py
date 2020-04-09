import random
import time


#  Added quote in line below
reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', \
              'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries', \
              'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7']
# added a call to len below
nPicturesInReel = len(reelList)

nCoins = 100
print('You have', nCoins, 'coins to start.  Good luck.')
print()



#changed below from function to def
def payTable(myList):
    picture1 = myList[0]
    picture2 = myList[1]
    picture3 = myList[2]
    if myList.count(picture1) == 3:
        if picture1== 'Lucky 7':
            nCoinsWon = 500
        elif picture1== 'bar':
            nCoinsWon = 100
        else:
            nCoinsWon = 10

    else:
        # changed to check for picture2 == picture3
        if (picture1 == picture2) or (picture2 == picture3) or (picture1 == picture3):
            nCoinsWon = 2
        else:
            nCoinsWon = 0

    return nCoinsWon  #added nCoinsWon
        

while True:

    bet = input('How many coins do you want to bet (defaults to 1, enter 0 to quit): ')
    if bet == '0':  # checked for '0'
        break

    if bet == '':
        bet = 1

    #New code to ensure that the user entered an integer    
    try:
        bet = int(bet)   # added to convert to integer
    except:
        print('Please enter a valid number of coins to bet.')
        print()
        continue  

    #New code to ensure that the user entered a valid bet amount
    if bet < 0:
        print('Negative numbers of coins are not allowed.')
        print()
        continue
        
    if bet > nCoins:
        print('Sorry, you do not have that many coins, you only have:', nCoins)
        print()
        continue

    resultList = []
    for spin in range(3):
        thisReelIndex = random.randrange(0, nPicturesInReel)
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print('Spinning ... ')
    print
    time.sleep(.5)
    print('     ', resultList[0])
    time.sleep(.5)
    print('     ', resultList[1])
    time.sleep(.5)
    print('     ', resultList[2])
    print()
        
    nCoins = nCoins - bet  # changed to subtract bet amount
    payOut = bet * payTable(resultList)

    if payOut == 0:  # changed to double equals
        print('Sorry - you lose.')
    else:
        print('You won', payOut, 'coins.  Cha-ching!')
        if payOut > 50:
            print('                         WOOOOO  HOOOOOOOOOOO!!!!')
            
    nCoins = nCoins + payOut

    print('You now have', nCoins, 'coins.')  #changed to use commas
    print()

    if nCoins == 0:
        print('Come back when you have more money!  Bye.')
        break

print('Sorry to see you go.  Come back again soon.')
    

