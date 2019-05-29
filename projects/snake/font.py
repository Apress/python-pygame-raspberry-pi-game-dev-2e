import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 172)
antialias = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                antialias = not antialias
    
    surface.fill((0, 0, 0))

    text = font.render("Lazy Dog", antialias, (255, 255, 255))
    textpos = text.get_rect(centerx=surface.get_width()/2, top=surface.get_height()/2)
    surface.blit(text, textpos)

    pygame.display.update()
    fpsClock.tick(30)

pygame.quit()