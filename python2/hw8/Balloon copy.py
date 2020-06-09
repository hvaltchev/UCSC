#  Balloon class

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *

#
#  Balloon class
#

class Balloon():

    balloonImageSmall = pygame.image.load('images/redBalloonSmall.png')
    balloonImageMedium = pygame.image.load('images/redBalloonMedium.png')
    balloonImageLarge = pygame.image.load('images/redBalloonLarge.png')
    popSound = pygame.mixer.Sound('sounds/balloonPop.wav')

    def __init__(self, window, maxWidth, maxHeight, ID):
        self.window = window
        self.ID = ID
        size = random.randrange(0, 3)
        if size == 0:  # small
            self.balloonImage = Balloon.balloonImageSmall
            self.nPoints = 30
            self.speed = 3.1
            self.y = maxHeight + random.randrange(0, maxHeight)
        elif size == 1:  # medium
            self.balloonImage = Balloon.balloonImageMedium
            self.nPoints = 20
            self.speed = 2.2
            self.y = maxHeight + random.randrange(0, maxHeight / 2)
        else:  # large
            self.balloonImage = Balloon.balloonImageLarge
            self.nPoints = 10
            self.speed = 1.5
            self.y = maxHeight + random.randrange(0, maxHeight / 3)

        balloonRect = self.balloonImage.get_rect()
        self.width = balloonRect.width
        self.height = balloonRect.height
        # Position so that entire balloon is within the window
        self.x = random.randrange(maxWidth - self.width)

    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return self.nPoints
        else:
            return 0

    def update(self):
        self.y = self.y - self.speed   # update y position based on our speed
        if self.y < -self.height:     # Off the top of the window
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.window.blit(self.balloonImage, (self.x, self.y))

    def __del__(self):
        print('Balloon', self.ID, 'is going away')


