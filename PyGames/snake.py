import pygame as pg
import sys
import random as rd
from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (400, 300)
# sets color
purple = (100,0,100)
green = (0,155,0)

# read images
#Start = pg.image.load()
Start = True

window = pg.display.set_mode(winSize)
cellSize = 20
# title
pg.display.set_caption('My Snake game')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()
# Set start point.
wormCoords = [{'x': 5, 'y': 5},
              {'x': 5, 'y': 4},
              {'x': 5, 'y': 3}]

Apple = {}

direction = 'right'


def drawGrid(win, winSize, cellSize, color):
    """
    Draws the grid for the game
    :param win: identifier of the window
    :param winSize: winSize (width,height)
    :param cellSize:
    :param color:
    """
    for x in range(0, winSize[0], cellSize):  # draw vertical lines
        pg.draw.line(win, color, (x, 0), (x, winSize[1]))
    for y in range(0, winSize[1], cellSize):  # draw horizontal lines
        pg.draw.line(win, color, (winSize[0], y), (0, y))


def drawWorm(win, wormCoor, cellSize, wormColor, headColor):
    for i,c in enumerate(wormCoor):
        x = c['x'] * cellSize
        y = c['y'] * cellSize
        wormSegmentRect = pg.Rect(x, y, cellSize, cellSize)
        if i == 0:
            pg.draw.rect(win, headColor, wormSegmentRect)
        elif i > 0:
            pg.draw.rect(win, wormColor, wormSegmentRect)

def Getrandom(win, Apple):
    Apple = {}
    Ax= rd.randint(0,19)
    Ay= rd.randint(0,14)
    Apple['x'] = Ax
    Apple['y'] = Ay
    return Apple

def drawApple(win, cellSize, Apple, color):
    Ac1= rd.randint(0,255)
    Ac2= rd.randint(0,255)
    Ac3= rd.randint(0,255)
    AColor = (Ac1,Ac2,Ac3)
    Ax = Apple['x'] * cellSize
    Ay = Apple['y'] * cellSize
    AppleRect = pg.Rect(Ax, Ay, cellSize, cellSize)
    pg.draw.rect(win, AColor, AppleRect, 0)

def texts(f, a, win, p, color):
   font= pg.font.Font(None, f)
   scoretext= font.render(a, True, color, None)
   win.blit(scoretext, p)

def bite(wormCoords):
    for i,n in enumerate(wormCoords):
        print(n['x'] , n['y'])
        print(i)
        if i!=0 and wormCoords[0]['x']==n['x'] and wormCoords[0]['y']==n['y']:
            return True
        else:
            return False

def showStartScreen(Start):
    while Start == True:
        for event in pg.event.get():
            if event.type is QUIT:
                pg.quit()
                sys.exit()
        window.fill((255, 255, 255))
        texts(50, "Snake Game~", window, (80,20), (0,255,255))
        texts(25, "- press [Space] to start -", window, (80,260), (0,255,255))
        pg.display.flip()
        clock.tick(10)
        if pg.key.get_pressed()[pg.K_SPACE]:
            Start = False
            break
        else:
            continue

Apple = Getrandom(window, Apple)
print(Apple)
drawApple(window, cellSize, Apple, green)
score = 0
showStartScreen(Start)
while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    #showStartScreen(Start)
    
    keys = pg.key.get_pressed()
    if direction != 'right' and keys[pg.K_LEFT]:
        direction = 'left'
    if direction != 'left' and keys[pg.K_RIGHT]:
        direction = 'right'
    if direction != 'down' and keys[pg.K_UP]:
        direction = 'up'
    if direction != 'up' and keys[pg.K_DOWN]:
        direction = 'down'

    if direction is 'up':
        if wormCoords[0]['y'] - 1 >= 0 :
            newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] - 1}
        else:
            newHead = {'x': wormCoords[0]['x'] + 1, 'y': wormCoords[0]['y']}
            direction = 'right'
    elif direction is 'down':
        if wormCoords[0]['y'] + 1 <= 14:
            newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] + 1}
        else:
            newHead = {'x': wormCoords[0]['x'] - 1, 'y': wormCoords[0]['y']}
            direction = 'left'
    elif direction is 'left':
        if wormCoords[0]['x'] - 1 >= 0:
            newHead = {'x': wormCoords[0]['x'] - 1, 'y': wormCoords[0]['y']}
        else:
            newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] - 1}
            direction = 'up'
    else:
        if wormCoords[0]['x'] + 1 <= 19:
            newHead = {'x': wormCoords[0]['x'] + 1, 'y': wormCoords[0]['y']}
        else:
            newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] + 1}
            direction = 'down'
    
    wormCoords.insert(0, newHead)
    if bite(wormCoords)==True:
        window.fill((0,0,0))
        texts(70, "~ GAME OVER ~", window, (20,60), (155,155,155))
    else:
        window.fill((255, 255, 255))

        if wormCoords[0]['x'] != Apple['x'] or wormCoords[0]['y'] != Apple['y']:
            del wormCoords[-1]  # remove worm's tail segment
        else:
            score += 1
            Apple = Getrandom(window, Apple)
            print(Apple)
            
        drawApple(window, cellSize, Apple, (0,255,0))
        drawGrid(window, winSize, cellSize, (40, 40, 40))
        drawWorm(window, wormCoords, cellSize, green, purple)
        
    texts(25, "Score: " + str(score), window, (320,10), (255,255,0))

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
