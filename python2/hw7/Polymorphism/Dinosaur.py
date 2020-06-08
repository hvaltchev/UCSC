# Frisbee Class

import pygame
import pygwidgets

class Dinosaur():
    def __init__(self, window, loc):
        self.image = pygwidgets.Image(window, loc, 'images/dino/f1.png')

        self.rect = self.image.getRect()
        self.animate = False

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.animate = True
            self.nFrames = 30

    def update(self):
        if not self.animate:
            return

        x = 1
        while x in range(1, 16):
            self.image.replace('/images/dino/f' + str(x) + '.png')

        self.nFrames = self.nFrames - 1
        if self.nFrames == 0:
            self.animate = False

    def draw(self):
        self.image.draw()
