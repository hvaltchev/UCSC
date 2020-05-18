import pygame
from pygame.locals import *
import random
import pygwidgets

# Basket class
class Basket():

    def __init__(self, window, windowWidth, windowHeight, ):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygwidgets.Image(window, (0, 0), 'images/basket.png')

        # A rect is made up of [x, y, width, height]
        startingRect = self.image.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        self.halfHeight = self.height / 2
        self.halfWidth = self.width / 2

        self.x = self.windowWidth / 2
        self.y = windowHeight - self.height - 20
        self.maxX = self.windowWidth - self.width
        self.image.setLoc((self.x, self.y))

        # Choose speed in the x direction
        self.xSpeed = 12

    def move(self, leftOrRight):
        # add code here to move the basket and restrict it to stay in the window
        if leftOrRight == 'left' and self.x > 0 + self.halfWidth:
            self.x = self.x - self.width

        if leftOrRight == 'right' and self.x + self.width + self.halfWidth < self.windowWidth:
            self.x = self.x + self.width

        self.image.setLoc((self.x, self.y))

    def getRect(self):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return myRect

    def draw(self):
        self.image.draw()


