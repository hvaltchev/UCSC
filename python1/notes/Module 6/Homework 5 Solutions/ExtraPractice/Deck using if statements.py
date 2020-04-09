# Create a deck of cards - with special names for Ace, Jack, Queen, King

import random

deckList = []
# Create a list of all suits
suitList = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

# Outer loop iterates through all suits
for suit in suitList:
    # Inner loop iterates through all card numbers from 1 to 13
    # Handle 1, 11, 12, 13 by replacing the number with a special name
    # All others, just convert the number to a string version of that number
    for cardNum in range(1, 14):
        if cardNum == 1:
            numberName = 'Ace'
        elif cardNum == 11:
            numberName = 'Jack'
        elif cardNum == 12:
            numberName = 'Queen'
        elif cardNum == 13:
            numberName = 'King'
        else:  # 2 through 10
            numberName = str(cardNum)

        fullCardName = numberName + ' of ' + suit
        deckList.append(fullCardName)

for card in deckList:
    print card


##### Now Shuffle the deck
#  Approach is to loop 52 times.
#  Each time through the loop, choose a random card from the starting deckList
#  remove it from the deckList using 'pop', then add it to the suffledDeckList using append
shuffledDeckList = []
for i in range(52):
    nCardsInDeck = len(deckList)
    randomIndex = random.randrange(nCardsInDeck)
    thisCard = deckList.pop(randomIndex)
    shuffledDeckList.append(thisCard)

# Copy the shuffledDeckList back to the original deckList
deckList = shuffledDeckList[:]

print
print 'Shuffled:'
print
for card in deckList:
    print card
