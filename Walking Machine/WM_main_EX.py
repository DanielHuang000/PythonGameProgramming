import pygame as pg
import sys
from os import path
from WM_settings import *
from WM_Characters_EX import *
from WM_Camera import *
from pygame.locals import *


class Game:
    def __init__(self):
        #innitialize pygame
        pg.init()
        #innitialize sound
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.map3 = pg.image.load('Map_lower.jpg')
        self.map03 = pg.transform.scale(self.map3, (1024, 768))

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'RE_map2.txt'))

    def update(self):
        self.all_sprites.update()
        #self.map_rect = pg.Rect(0,0,2000,1700)
        #self.screen.blit(self.map03,self.map_rect)
        self.camera.update(self.player)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()       
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'P':
                    self.player = Character(self,col,row)
        self.camera = Camera(self.map.width, self.map.height)

    """
    def draw_grid(self):
        for x in range(0,WIDTH,TS):
            pg.draw.line(self.screen, LIGHTGREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TS):
            pg.draw.line(self.screen, LIGHTGREY,(0,y),(WIDTH,y))
    """
    
    def draw(self):
        #self.screen.fill(DARKGREY)
        #self.draw_grid()
        self.map_rect = pg.Rect(0,0,2000,1700)
        self.screen.blit(self.map03,self.map_rect)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def event(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                    """
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
                    """

    def run(self):
        self.playing = True
        while self.playing == True:
            self.dt = self.clock.tick(FPS)/1000
            self.event()
            self.update()
            self.draw()


    def opening_scene(self):
        pass

    def end_scene(self):
        pass

    def quit(self):
        pg.quit()
        sys.exit()

# create the game object
g = Game()
g.opening_scene()
while True:
    g.new()
    g.run()
    g.end_scene()
