# Create new balls, bounce, and reverse when clicked

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Fruit import *  # bring in the Fruit class code
from Basket import * # bring in the Baske class code
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oDisplay = pygwidgets.DisplayText(window, (WINDOW_WIDTH -120, 10), '', fontSize=30)

# 5 - Initialize variables
fruitType = ['apple', 'banana', 'cherry', 'grapes', 'pear', 'strawberry']
fruitList = []
fruitRectList = []
r = random.randint(0, 5)
oBasket = Basket(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitType[r])
oRestartButton = pygwidgets.TextButton(window, (5, 5), 'Restart')
score = 0
level = 1

# 6 - Loop forever
while True:
    r = random.randint(0, 5)
    oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitType[r])
    oFruit.reset()
    fruitList.append(oFruit)
    # if pygame.time.get_ticks() % 10 == 1:
    #     print('TICK')
    #     oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, fruitType[r])
    #     fruitList.append(oFruit)

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):  # ckicked on the Restart button
            print('User pressed the Restart button')
            score = 0

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
    basketRect = oBasket.getRect()

    for x in range(len(fruitList)):
        fruitList[x].update()
        fruitRect = fruitList[x].getRect()
        fruitRectList.append(fruitRect)

    # basketRect = oBasket.getRect()

    # fruitRect = oFruit.getRect()
    for y in range(len(fruitRectList)):
        if basketRect.colliderect(fruitRectList[y]):
            fruitList[y].reset()
            # fruitList[].update()
            print('Fruit has collided with the basket')
            score += oFruit.getScore()
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

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


