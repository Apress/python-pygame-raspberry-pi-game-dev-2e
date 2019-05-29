import pygame
from pygame.locals import *

from robotmodel import RobotModel

class RobotView(object):
    def __init__(self, imgPath):
        self.img = pygame.image.load(imgPath)

    def draw(self, surface, models):
        for model in models:
            rect = Rect(model.getFrame() * 32, 0, 32, 32)
            surface.blit(self.img, model.getPosition(), rect)
