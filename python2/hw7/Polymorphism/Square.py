# Frisbee Class

import pygame
import pygwidgets
import random

class Square():
    def __init__(self, window, loc):
        self.window = window
        self.widthAndHeight = random.randrange(10, 100)
        self.color = random.range(0, 255)
        self.x = 500
        self.y = 200
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight, self.widthAndHeight)
        self.type = 'Square'
        self.animate = False

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.animate = True
            self.nFrames = 30

    def update(self):
        if not self.animate:
            return

        self.nFrames = self.nFrames - 1
        if self.nFrames == 0:
            self.spinning = False

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))

