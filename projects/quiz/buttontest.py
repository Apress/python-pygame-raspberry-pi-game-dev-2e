#!/usr/bin/python3
import pygame, os, sys
from pygame.locals import *
from gpiozero import Button

"""
Draw the state of the button. If the button is pressed, a bright circle is displayed.
"""
def drawButtonState(surface, button, pos):
    color = 32
    if button.is_pressed:
        color = 192
    pygame.draw.circle(surface, (color, 0, 0), pos, 35)

"""
Loop through the given buttons and detect if each is pressed. Calls drawButtonState.
"""
def drawPlayerState(surface, buttons, startx):
    x = startx
    for b in buttons:
        drawButtonState(surface, b, (x, 240))
        x = x + 80

    return x

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))

player1 = [ Button(4), Button(17), Button(22) ]
player2 = [ Button(5), Button(6), Button(13) ]

background = (0, 0, 0) # Black

while True:
    surface.fill(background)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x = 80
    x = drawPlayerState(surface, player1, x)
    x = x + 80
    drawPlayerState(surface, player2, x)
    
    pygame.display.update()
    fpsClock.tick(30)
