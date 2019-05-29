import pygame, os, sys
from pygame.locals import *

"""
----------------------------------------------------------------------------------------------------
    GameState

    The game state class defines an interface that is used by the RaspberryPiGame class. Each state
    manages a particular function of the game. For example; main menu, the actual game play, and
    interstitial screens.
----------------------------------------------------------------------------------------------------
"""
class GameState(object):
    
    """
    Initialise the Game state class. Each sub-type must call this method. Takes one parameter, which
    is the game instance.
    """
    def __init__(self, game):
        self.game = game
        
    """
    Called by the game when entering the state for the first time.
    """
    def onEnter(self, previousState):
        pass
    
    """
    Called by the game when leaving the state.
    """
    def onExit(self):
        pass
        
    """
    Called by the game allowing the state to update itself. The game time (in milliseconds) since
    the last call is passed.
    """
    def update(self, gameTime):
        pass
        
    """
    Called by the game allowing the state to draw itself. The surface that is passed is the
    current drawing surface.
    """
    def draw(self, surface):
        pass
        
"""
----------------------------------------------------------------------------------------------------
Raspberry Pi Game
                                    
Basic game object-oriented framework for the Raspberry Pi. Users create 'states' that alter what is
being displayed on-screen / updated at any particular time.
----------------------------------------------------------------------------------------------------
"""
class RaspberryPiGame(object):
            
    """
    Initialise the Raspberry Pi Game class.
    """
    def __init__(self, gameName, width, height):
        
        pygame.init()
        pygame.display.set_caption(gameName);
        
        self.fpsClock = pygame.time.Clock()
        self.mainwindow = pygame.display.set_mode((width, height))
        self.background = pygame.Color(0, 0, 0)
        self.currentState = None
        
    """
    Change the current state. If the newState is 'None' then the game will terminate.
    """
    def changeState(self, newState):
        if ( self.currentState != None ):
            self.currentState.onExit()
            
        if ( newState == None ):
            pygame.quit()
            sys.exit()	
            
        oldState = self.currentState
        self.currentState = newState
        newState.onEnter(oldState)

    """
    Run the game. Initial state must be supplied.
    """
    def run(self, initialState):
        
        self.changeState( initialState )
        
        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()	

            gameTime = self.fpsClock.get_time()
            
            if ( self.currentState != None ):
                self.currentState.update( gameTime )
                
            self.mainwindow.fill(self.background)	
            if ( self.currentState != None ):
                self.currentState.draw ( self.mainwindow )
                
            pygame.display.update()
            self.fpsClock.tick(30)
