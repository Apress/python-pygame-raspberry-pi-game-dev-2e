#!/usr/bin/python
import pygame, sys
from pygame.locals import *

from robotview import RobotView
from robotcontroller import RobotController
from robotgenerator import RobotGenerator
from radarview import RadarView

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))

lastMillis = 0

generator = RobotGenerator()
view = RobotView('robot.png')
radar = RadarView('blip.png', 'radarview.png')
controller = RobotController(generator.getRobots())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    deltaTime = lastMillis / 1000

    generator.update(deltaTime)
    controller.update(deltaTime)

    surface.fill((0, 0, 0))

    view.draw(surface, generator.getRobots())
    radar.draw(surface, generator.getRobots())

    pygame.display.update()
    lastMillis = fpsClock.tick(30)
