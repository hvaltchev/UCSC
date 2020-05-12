# pygame demo using Ball class, bounce many balls

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code
from Drop import *  # bring in the Drop class code
from SimpleButton import *  # bring in the SimpleButton code
from SimpleText import *  # bring in the SimpleText code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 0
N_DROPS = 0
MOUSE_X = 0
MOUSE_Y = 0
CLICKED = 0

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oNewBallButton = SimpleButton(window, (2, 2), 'images/newBallUp.png', 'images/newBallDown.png')
oNewDropButton = SimpleButton(window, (485, 2), 'images/newDropUp.png', 'images/newDropDown.png')
oCountBall = SimpleText(window, (200, 450), str(N_BALLS), (255, 255, 255))
strAnd = SimpleText(window, (300, 450), 'and', (255, 255, 255))
oCountDrop = SimpleText(window, (250, 450), str(N_DROPS), (255, 255, 255))

# 5 - Initialize variables
ballList = []
dropList = []

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oNewBallButton.handleEvent(event):  # ckicked on the "NewBall" button
            # Change this create a new ball object
            print('Clicked on the new ball button')
            N_BALLS = N_BALLS + 1
            oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
            ballList.append(oBall)  # append the new ball to the list of balls


        if oNewDropButton.handleEvent(event):  # ckicked on the "NewDrop" button
            # Change this create a new drop object
            print('Clicked on the new drop button')
            N_DROPS = N_DROPS + 1
            oDrop = Drop(window, WINDOW_WIDTH, WINDOW_HEIGHT)
            dropList.append(oDrop)  # append the new ball to the list of balls

        if pygame.mouse.get_pressed() == (1, 0, 0):
            MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
            CLICKED = 1

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        if oBall.x <= MOUSE_X <= oBall.x + oBall.width and oBall.y <= MOUSE_Y <= oBall.y + oBall.height and oBall.xSpeed != 0 and oBall.ySpeed != 0 and CLICKED == 1:
            oBall.update(1) # reverse direction
        else:
            oBall.update(0)  # tell each ball to update itself


    for oDrop in dropList:
        oDrop.update()  # tell each drop to update itself

   # 9 - Clear the screen before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the screen elements
    for oBall in ballList:
        oBall.draw()   # tell each ball to draw itself
        oCountBall = SimpleText(window, (170, 450), str(N_BALLS), (255, 255, 255))
        strBalls = SimpleText(window, (200, 450), 'balls', (255, 255, 255))
        oCountBall.draw()
        strBalls.draw()

    for oDrop in dropList:
        oDrop.draw()   # tell each drop to draw itself
        oCountDrop = SimpleText(window, (390, 450), str(N_DROPS), (255, 255, 255))
        strDrops = SimpleText(window, (420, 450), 'drops', (255, 255, 255))
        strAnd.draw()
        oCountDrop.draw()
        strDrops.draw()

    oNewBallButton.draw()
    oNewDropButton.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


