import pygame as pg
import random as rd

WIDTH = 512#1024
HEIGHT = 384#768
FPS = 40
TITLE = "My Game"

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)

#clock = pg.time.Clock()
#felix = Character()
TS = 16

GRIDWIDTH = WIDTH / TS
GRIDHEIGHT = HEIGHT / TS
PLAYER_SPEED = 300
