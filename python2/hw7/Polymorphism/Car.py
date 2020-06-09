# Frisbee Class

import pygame
import pygwidgets
import time

class Car():
    def __init__(self, window, loc):
        self.image = pygwidgets.Image(window, loc, 'images/car.png')
        self.rect = self.image.getRect()
        self.animate = False
        self.size = 100

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.animate = True
            self.nFrames = 30

    def update(self):
        if not self.animate:
            self.image.scale(self.size - 10)
            return

        self.image.scale(self.size + 100)
        self.animate = False

        self.nFrames = self.nFrames - 1
        if self.nFrames == 0:
            self.animate = False

    def draw(self):
        self.image.draw()
