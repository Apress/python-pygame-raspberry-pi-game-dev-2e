import pygame
from pygame.locals import *

"""
Main entry point to the Quiz game
"""

"""
Base game state class. All other state classes will derive from this.
"""
class NullState(object):

    """
    Update the game state. Returns the new game state.
    """
    def update(self, deltaTime):
        return None

    """
    Draw the state.
    """
    def draw(self, surface):
        pass

    """
    On enter
    """
    def onEnter(self):
        pass

    """
    On exit
    """
    def onExit(self):
        pass

"""
Game runner code. Uses the game state class to control the current update
and draw.
"""
class GameRunner(object):
    """
    Constructor.
    dimensions - The width and height of the window
    title - The title of the window
    backColour - Tuple representing the RGB value of the background colour
    initialState - The initial state of the game
    """
    def __init__(self, dimensions, title, backColour, initialState):
        self.state = initialState
        self.clock = pygame.time.Clock()
        self.backColour = backColour
        self.surface = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(title)

    def update(self):
        deltaTime = self.clock.tick(30) / 1000.0
        if self.state != None:
            self.state = self.state.update(deltaTime)

        return self.state

    def draw(self):
        self.surface.fill(self.backColour)
        if self.state != None:
            self.state.draw(self.surface)

        pygame.display.update()
