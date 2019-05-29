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
ball = pygame.image.load('ball.png')
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed = 3
ballServed = False
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)



# brick init

while True:
    mainSurface.fill(black)
    # brick draw

    # bat and ball draw
    mainSurface.blit(bat, batRect)
    mainSurface.blit(ball, ballRect)

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
    bx += sx
    by += sy
    ballRect.topleft = (bx, by)

    if (by <= 0):
        by = 0
        sy *= -1

    if (by >= 600 - 8):
        by = 600 - 8
        sy *= -1

    if (bx <= 0):
        bx = 0
        sx *= -1

    if (bx >=800 - 8):
        bx = 800 - 8
        sx *= -1

    if ballRect.colliderect(batRect):
        by = playerY - 8
        sy *= -1

    # collision detection

    pygame.display.update()
    fpsClock.tick(30)
