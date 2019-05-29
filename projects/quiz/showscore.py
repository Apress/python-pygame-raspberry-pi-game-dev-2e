#!/usr/bin/python3

import pygame
from pygame.locals import *
from gamerunner import NullState
from ui import Text

class ShowScore(NullState):

    def __init__(self, nextState, player1, player2, showWinner = False):
        self.nextState = nextState
        self.player1 = player1
        self.player2 = player2
        self.counter = 3
        self.showWinner = showWinner
        self.scoreText = Text(300, (255, 255, 0))
        self.playerText = Text(128, (255, 255, 255))

    def update(self, deltaTime):
        self.counter = self.counter - deltaTime
        if self.counter <= 0:
            return self.nextState

        return self

    def draw(self, surface):
        self.playerText.draw(surface, "Player 1", (200, 85), True)
        self.playerText.draw(surface, "Player 2", (600, 85), True)

        self.scoreText.draw(surface, str(self.player1.score), (200, 150), True)
        self.scoreText.draw(surface, str(self.player2.score), (600, 150), True)

        if self.showWinner:
            winner = "WINNER!"            
            pos = 200
            if self.player1.score == self.player2.score:
                winner = "TIE!"
                pos = 400
            elif self.player2.score > self.player1.score:
                pos = 600
            self.playerText.draw(surface, winner, (pos, 400), True)
        

    def onEnter(self):
        self.counter = 3

if __name__ == '__main__':
    import sys
    class P(object):
        def __init__(self, s):
            self.score = s

    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))

    score = ShowScore(None, P(55), P(10), True)

    background = (0, 0, 0) # Black

    while True:
        surface.fill(background)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        deltaTime = fpsClock.tick(30) / 1000.0
        
        score.draw(surface)
        
        pygame.display.update()