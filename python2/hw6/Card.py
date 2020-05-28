# Card Class

import pygwidgets

class Card():

    def __init__(self, window, rank, suit, value):
        # must add code here to save away parameters in instance variables
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value

        # and create two Image objects, one for the current card, one for the backOfCard
        self.oCurrent = pygwidgets.Image(self.window, (100, 200), ‘images/BackOfCard.png’)
        self.oBackOfCard = pygwidgets.Image(self.window, (100, 200), ‘images/BackOfCard.png’)

    # You can remove the print statement below
    # These are just place holders.

    def conceal(self):
        print('Must conceal the card here')
        self.oBackOfCard.draw()
        pass

    def setLoc(self, locTuple):
        print('Called setLoc method, passed in', locTuple)
        pass

    def reveal(self):
        print('Must reveal card here')
        pass

    def getName(self):
        print('Get the name of the card here')
        pass

    def getValue(self):
        print('Get the value of the card here')
        pass

    def draw(self):
        print('Draw the card here')
        pass

    def getCardNameAndValue(self):
        print("Get the card name and value here")
        return "CardName", 0