import pygame as pg
import sys
from pygame import *
# initialize the pygame library
pg.init()
# sets the size of the window
size = (250,500)
screen = pg.display.set_mode(size)
pg.display.set_caption("Traffic Light")
WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 50
clock = pg.time.Clock()

class Games(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.running = True
        self.clock = pg.time.Clock()
        self.r = pg.image.load("RED.jpg")
        self.red = pg.transform.scale(self.r, (250, 500))
        self.g = pg.image.load("GREEN.jpg")
        self.green = pg.transform.scale(self.g, (250, 500))
        self.y = pg.image.load("YELLOW.jpg")
        self.yellow = pg.transform.scale(self.y, (250, 500))
        self.n = pg.image.load("START.jpg")
        self.start = pg.transform.scale(self.n, (250, 500))
        self.state = self.start
        self.juststart = True

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == MOUSEBUTTONUP and self.state == self.start:
                self.state = self.red
                self.juststart = True
            elif event.type == MOUSEBUTTONUP and self.state != self.start:
                self.state = self.start
                self.juststart = False


    def draw(self):
        screen.fill(WHITE)
        self.rect = self.state.get_rect()
        screen.blit(self.state,self.rect)
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        if self.state == self.start:
            #print("....")
            return self.state

        elif self.state != self.start and self.juststart == True:
            self.juststart = False
            return self.state

        elif self.state == self.red:
            pg.time.wait(2000)
            self.state = self.green
            print("hi")
            return self.state

        elif self.state == self.green:
            pg.time.wait(2000)
            self.state = self.yellow
            print("hello")
            return self.state

        elif self.state == self.yellow:
            pg.time.wait(1000)
            self.state = self.red
            print("hey")
            return self.state

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()



g = Games()
while g.running:
    g.event()
    g.update()
    g.draw()
    g.run()
pg.quit()
