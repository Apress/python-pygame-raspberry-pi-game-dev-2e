#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

class Ball:
    def __init__(self, x, y, speed, imgPath):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = pygame.image.load(imgPath)

    def update(self, gameTime):
        sx = self.speed[0]
        sy = self.speed[1]

        self.x += sx
        self.y += sy

        if (self.y <= 0):
            self.y = 0
            sy = sy * -1
        if (self.y >= 600 - 8):
            self.y = 600 - 8
            sy = sy * -1
        if (self.x <= 0):
            self.x = 0
            sx = sx * -1
        if (self.x >=800 - 8):
            self.x = 800 - 8
            sx = sx * -1

        self.speed = (sx, sy)

    def hasHitBrick(self, bricks):
        return False

    def hasHitBat(self, bat):
        return False
    
    def draw(self, gameTime, surface):
        surface.blit(self.img, (self.x, self. y))

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))
    ball = Ball(0, 200, (4, 4), 'ball.png')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ball.update(fpsClock)

        surface.fill((0, 0, 0))
        ball.draw(fpsClock, surface)
        pygame.display.update()
        fpsClock.tick(30)
