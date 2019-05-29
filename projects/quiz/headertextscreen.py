from ui import *
from playercontroller import *
from gamerunner import NullState

class HeaderTextScreen(NullState):
    def __init__(self, nextState, player1, player2, waitTime = 0):
        self.nextState = nextState
        self.player1 = player1
        self.player2 = player2
        self.big = Text(128, (255, 192, 0))
        self.small = Text(36, (255, 255, 255))
        self.waitTime = waitTime
        self.currentTime = 0
        self.header = ""
        self.subHeader = ""

    def setHeader(self, header):
        self.header = header

    def setSub(self, subHeader):
        self.subHeader = subHeader

    def setNextState(self, nextState):
        self.nextState = nextState

    def update(self, deltaTime):
        if self.waitTime > 0:
            self.currentTime = self.currentTime + deltaTime
            if self.currentTime >= self.waitTime:
                return self.nextState
        elif self.player1.anyButton() or self.player2.anyButton():
            return self.nextState
        return self

    def draw(self, surface):
        self.big.draw(surface, self.header, (400, 200), True)
        self.small.draw(surface, self.subHeader, (400, 300), True)
