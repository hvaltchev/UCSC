import pygame
from pygame.locals import *
import random
import pygwidgets

# Fruit class
class Fruit():

    def __init__(self, window, windowWidth, windowHeight, fruitType):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.fruitType = fruitType
        self.image = pygwidgets.Image(window, (0, 0), 'images/' + fruitType + '.png')
        self.points = 15
        # A rect is made up of [x, y, width, height]
        startingRect = self.image.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        # Choose a random speed in the y direction
        self.ySpeed = random.randrange(5, 9)
        self.maxX = self.windowWidth - self.width
        self.reset()

    def reset(self):
        # Pick a random starting position
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(-450, -self.height)
        self.image.setLoc((self.x, self.y))

    def update(self):
        # check for going off screen, move to above the windows
        if self.y > self.windowHeight:
            self.reset()
        # move location
        self.y = self.y + self.ySpeed
        self.image.setLoc((self.x, self.y))

    def getRect(self):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return myRect

    def getScore(self):
        if self.fruitType != 'pear':
            self.points = 15
            #play good sound
        else:
            self.points = -100
            #play bad sound
        return self.points

    def levelUp(self):
        self.ySpeed = self.ySpeed * 2

    def playSound(self):
        if self.fruitType != 'pear':
            #load good sound
            pygame.mixer.music.load('audio/brick-1.wav')
            pygame.mixer.music.play()
        else:
            self.points = -100
            #load bad sound
            pygame.mixer.music.load('audio/brick-2.wav')
            pygame.mixer.music.play()

    def draw(self):
        self.image.draw()


