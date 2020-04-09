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
print
print 'Shuffled:'
print

# Use the built-in call to 'shuffle' to do all the work!

random.shuffle(deckList)
for card in deckList:
    print card
