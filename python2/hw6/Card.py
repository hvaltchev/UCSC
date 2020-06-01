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

        # create two image objects
        self.cardImage = pygwidgets.Image(window, (100, 200), "images/BackOfCard.png")
        self.backImage = pygwidgets.Image(window, (100, 200), "images/BackOfCard.png")

    def conceal(self):
        print('Must conceal the card here')
        self.backImage.draw()

    def setLoc(self, locTuple):
        print('Called setLoc method, passed in', locTuple)

        pass

    def reveal(self):
        print('Must reveal card here')
        self.cardImage.draw()

    def getName(self):
        print('Get the name of the card here')
        return self.rank + ' of ' + self.suit

    def getValue(self):
        print('Get the value of the card here')
        return self.value

    def draw(self):
        print('Draw the card here')
        self.cardImage.replace('images/' + self.getName() + '.png')
        self.cardImage.draw()

    def getCardNameAndValue(self):
        print("Get the card name and value here")
        name = self.getName()
        value = self.value()
        return name, value
