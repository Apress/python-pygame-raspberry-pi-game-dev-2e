#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks')

black = pygame.Color(0, 0, 0)

# bat init
bat = pygame.image.load('bat.png')
playerY = 540
batRect = bat.get_rect()
mousex, mousey = (0, playerY)

# ball init
# brick init

while True:
    mainSurface.fill(black)
    # brick draw
    # bat and ball draw
    mainSurface.blit(bat, batRect)

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if (mousex < 800 - 55):
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = (800 - 55, playerY)

    # main game logic
    # collision detection

    pygame.display.update()
    fpsClock.tick(30)
