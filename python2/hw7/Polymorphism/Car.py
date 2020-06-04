# Frisbee Class

import pygame
import pygwidgets

class Car():
    def __init__(self, window, loc):
        self.image = pygwidgets.Image(window, loc, 'images/car.png')

        self.rect = self.image.getRect()
        self.spinning = False

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.spinning = True
            self.nFrames = 30

    def update(self):
        if not self.spinning:
            return

        self.image.rotate(15)
        self.nFrames = self.nFrames - 1
        if self.nFrames == 0:
            self.spinning = False

    def draw(self):
        self.image.draw()
