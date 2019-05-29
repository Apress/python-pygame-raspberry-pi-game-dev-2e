import pygame
from robotmodel import RobotModel

class RadarView(object):

    def __init__(self, blipImagePath, borderImagePath):
        self.blipImage = pygame.image.load(blipImagePath)
        self.borderImage = pygame.image.load(borderImagePath)

    def draw(self, surface, robots):
        for robot in robots:
            x, y = robot.getPosition()
            x /= 10
            y /= 10

            x += 1
            y += 1

            surface.blit(self.blipImage, (x, y))

        surface.blit(self.borderImage, (0, 0))
