import pygame
import pygwidgets
import random

class Dinosaur():
    def __init__(self, window, loc):
        self.image = pygwidgets.ImageCollection(window, loc, {'image1':'images/Dino/f1.png',
                                                              'image2':'images/Dino/f2.png',
                                                              'image3':'images/Dino/f3.png',
                                                              'image4':'images/Dino/f4.png',
                                                              'image5':'images/Dino/f5.png',
                                                              'image6':'images/Dino/f6.png',
                                                              'image7':'images/Dino/f7.png',
                                                              'image8':'images/Dino/f8.png',
                                                              'image9':'images/Dino/f9.png',
                                                              'image10':'images/Dino/f10.png',
                                                              'image11':'images/Dino/f11.png',
                                                              'image12':'images/Dino/f12.png',
                                                              'image13':'images/Dino/f13.png',
                                                              'image14':'images/Dino/f14.png',
                                                              'image15':'images/Dino/f15.png',
                                                              'image16':'images/Dino/f16.png',
                                                              'image17':'images/Dino/f17.png'}, 'image1')

        self.rect = self.image.getRect()
        self.animating = False

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.image.replace('image2')
            self.nFrames = 10
            self.animating = True

    def update(self):
        if not self.animating:
            return

        self.nFrames = self.nFrames - 1
        if self.nFrames == 0:
            self.animating = False
            self.rect = self.image.getRect()
            self.image.replace('image2')
            self.image.replace('image3')
            self.image.replace('image4')
            self.image.replace('image5')
            self.image.replace('image6')
            self.image.replace('image7')
            self.image.replace('image8')
            self.image.replace('image9')
            self.image.replace('image10')
            self.image.replace('image11')
            self.image.replace('image12')
            self.image.replace('image13')
            self.image.replace('image14')
            self.image.replace('image15')
            self.image.replace('image16')
            self.image.replace('image17')


    def draw(self):
        self.image.draw()
