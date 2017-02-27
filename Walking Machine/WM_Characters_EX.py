import pygame as pg
import sys
import os
from WM_settings import *
from pygame.locals import *
#from WM_Library import *

#pg.init()

#game_folder = os.path.dirname("/Users/daniel/Desktop/CodesTemp/Walking Machine/")
#img_folder = os.path.join(game_folder, "PNG")

class Character(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        #self.image = pg.image.load(os.path.join(img_folder,
        # "wait.png")).convert()
        #self.image.set_colorkey(BLACK)
        self.game = game
        self.image = pg.Surface((TS, TS))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x*TS
        self.y = y*TS
        # self.rect.top = x
        # self.rect.left = y
        # self.speedx = 0
        # self.speedy = 0
    """
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy
    """
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        # find out where is self.game.dt calcualted so that you change 0.01 for that variable
        self.x += self.vx * 0.01
        self.y += self.vy * 0.01
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        
        if keys[K_LEFT] or keys[K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TS, TS),pg.SRCALPHA)
        self.image.fill(GREEN)
        #self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TS
        self.rect.y = y * TS
