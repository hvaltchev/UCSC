# Card Class

import pygwidgets

class Card():

    def __init__(self, window, rank, suit, value):
        # must add code here to save away parameters in instance variables
        # and create two Image objects, one for the current card, one for the backOfCard
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value

        # create an image object
        self.cardImage = pygwidgets.Image(window, (100, 200), 'images/BackOfCard.png')

    def conceal(self):
        self.cardImage.replace('images/BackofCard.png')

    def setLoc(self, locTuple):
        self.cardImage.setLoc(locTuple)

    def reveal(self):
        self.cardImage.replace('images/' + self.getName() + '.png')

    def getName(self):
        return self.rank + ' of ' + self.suit

    def getValue(self):
        return self.value

    def draw(self):
        self.cardImage.draw()

    def getCardNameAndValue(self):
        return self.getName(), self.value()
