#-----------------------------------------------------------------------------------------------#

# Hristo Valtchev
# Homework #1
# 4/20/2020

#-----------------------------------------------------------------------------------------------#


#  HigherOrLower

import random

### DECK
SUIT_TUPLE = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

def getCard(deckListIn):
    if len(deckListIn) == 0:
        return 'no more cards'
    thisCard = deckListIn.pop() # pops one card off of the top of the deck and returns it
    return thisCard

    
def shuffle(deckListIn):
    # Make a copy of the starting deck to use as the working deck
    deckListOut = deckListIn[:]  
    random.shuffle(deckListOut)
    return deckListOut


#  Main code
print('Welcome to Higher Or Lower')
print('You have to choose if the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points, get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

# Build a full deck of 52 cards
# Each card is a dictionary made up of a rank, a suit, and a value
# For example:  {'rank':'Ace', 'suit':'Spades', 'value': 1}
startingDeckList = []
for thisValue, rank in enumerate(RANK_TUPLE):
    for suit in SUIT_TUPLE:
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

# Add two Jokers
joker1 = {'rank': 'Joker', 'suit': 'Spades', 'value': 14}
joker2 = {'rank': 'Joker', 'suit': 'Hearts', 'value': 14}
startingDeckList.append(joker1)
startingDeckList.append(joker2)

score = 50

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):   # play one game of this many card
        while True:
            userAnswer = input('Will the next card be higher or lower than a/an ' + \
                       currentCardRank + '?  (enter h or l): ')
            userAnswer = userAnswer.lower()
            if userAnswer in ('h', 'l'):  # valid answers
                break
            print('Please give an answer of "h" for higher or "l" for lower.')
            continue   # ask again
        
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if nextCardValue > currentCardValue:
            correctAnswer = 'h'

        elif nextCardValue == currentCardValue:
            # Make 'correct answer" to be opposite of what the user chose
            # this ensures that the check below will fail

            # Compare rank based on index of SUIT_TUPLE
            curRank = SUIT_TUPLE.index(currentCardSuit)
            nextRank = SUIT_TUPLE.index(nextCardSuit)
            print(curRank)
            print(nextRank)

            if userAnswer == 'l':
                if nextRank < curRank:
                    correctAnswer = 'h'
                if nextRank > curRank:
                    correctAnswer = 'l'
            if userAnswer == 'h':
                if nextRank < curRank:
                    correctAnswer = 'h'
                if nextRank > curRank:
                    correctAnswer = 'l'

        else:  # nextCardValue must be lower
            correctAnswer = 'l'
        
        if userAnswer == correctAnswer:
            print('You got it right!')
            score = score + 20
        else:
            print('Sorry')
            score = score - 15

        print()
        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit


    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')


    
    



         

    
