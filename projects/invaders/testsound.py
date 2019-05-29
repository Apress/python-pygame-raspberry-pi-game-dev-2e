import pygame, os, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()
shootSound = pygame.mixer.Sound('playershoot.wav')
shootSound.play()

while pygame.mixer.get_busy():
	pass
	
pygame.mixer.quit()
pygame.quit()