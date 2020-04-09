# Create a deck of cards - with special names for Ace, Jack, Queen, King

import random

deckList = []
# Create a list of all card suits
suitList = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
# Create a list of all card names
cardNameList = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Outer loop iterates through all suits
for suit in suitList:
    # Inner loop iterates through all card names
    for cardName in cardNameList:
        fullCardName = cardName + ' of ' + suit
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
