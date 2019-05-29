import pygame, os, sys
from pygame.locals import *

# Our imports
from raspigame import *
from interstitial import *
from menu import MainMenuState
from invadersgame import PlayGameState

"""
----------------------------------------------------------------------------------------------------
    Application Entry Point
                
    Main entry point to the application. Sets up the objects and starts the main loop.
----------------------------------------------------------------------------------------------------
"""

invadersGame = RaspberryPiGame("Invaders", 800, 600)
mainMenuState = MainMenuState( invadersGame )
gameOverState = InterstitialState( invadersGame, 'G A M E  O V E R !', 5000, mainMenuState )
playGameState = PlayGameState( invadersGame, gameOverState )
getReadyState = InterstitialState( invadersGame, 'Get Ready!', 2000, playGameState )
mainMenuState.setPlayState( getReadyState )

invadersGame.run( mainMenuState )
