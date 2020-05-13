# Create new balls, bounce, and reverse when clicked

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Fruit import *  # bring in the Fruit class code
from Basket import * # bring in the Basket class code
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FRAMES_PER_SECOND = 60
MAX_FRUIT = 2

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oDisplay = pygwidgets.DisplayText(window, (WINDOW_WIDTH -120, 10), '', fontSize=30)

# 5 - Initialize variables
score = 0
level = 1
fruitType = ['apple', 'banana', 'cherry', 'grapes', 'pear', 'strawberry']
fruitList = []
fruitCount = [0, 0, 0, 0, 0, 0]
r = random.randint(0, 5)
oBasket = Basket(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitType[r])
oRestartButton = pygwidgets.TextButton(window, (5, 5), 'Restart')
oLevelText = pygwidgets.DisplayText(window, (440, 20), 'LEVEL 1')
oCountText = pygwidgets.DisplayText(window, (360, 980), 'apple: 0 banana: 0 cherry: 0 grapes: 0 pear: 0 strawberry: 0')

# 6 - Loop forever
while True:
    r = random.randint(0, 5)
    if pygame.time.get_ticks() % 50 == 1:
        print('TICK')
        oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitType[r])
        fruitList.append(oFruit)

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Quit Game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Restart Button
        if oRestartButton.handleEvent(event):  # ckicked on the Restart button
            print('User pressed the Restart button')
            score = 0
            window.fill(LIME)
            level = 1
            for x in range(len(fruitList)):
                fruitList[x].reset()

        # Check for user pressing left key
        keyPressedList = pygame.key.get_pressed()
        if keyPressedList[pygame.K_LEFT]:  # moving left
            print('LEFT')
            oBasket.move('left')

        # Check for user pressing right key
        if keyPressedList[pygame.K_RIGHT]:  # moving right
            print('RIGHT')
            oBasket.move('right')

   # Add "continuous mode" code here to check for left or right arrow keys
    # If you get one, tell the basket to move itself appropriately

    # 8 - Do any "per frame" actions
    # oFruit.update()  # tell each fruit to update itself

    # Get Basket Rectangle
    basketRect = oBasket.getRect()

    for x in range(len(fruitList)):
        fruitList[x].update()
        if basketRect.colliderect(fruitList[x].getRect()):
            fruitList[x].playSound()
            fruitList[x].reset()
            fruitList[x].update()
            print('Fruit has collided with the basket')
            #TODO Count each fruit and display at the bottom of the window
            # fruitCount{fruitList[x].fruitType} += 1
            score += fruitList[x].getScore()
            # Level Calculation
            if score % 1000 == 0:
                level = level + 1
                update = 'LEVEL: ' + str(level)
                oLevelText.setValue(update)
        oDisplay.setValue('Score:' + str(score))
    # 9 - Clear the screen before drawing it again
    window.fill(LIME)
    
    # 10 - Draw the screen elements
    for x in range(len(fruitList)):
        fruitList[x].draw()
    # oFruit.draw()   # tell each ball to draw itself

    oRestartButton.draw()
    oBasket.draw()
    oDisplay.draw()
    oLevelText.draw()
    oCountText.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount