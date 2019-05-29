import pygame, os, sys
from pygame.locals import *

from raspigame import *
from swarm import *
from player import *
from collision import *


class PlayGameState(GameState):
    def __init__(self, game, gameOverState):
        super(PlayGameState, self).__init__(game)
        self.controllers = None
        self.renderers = None
        self.player_controller = None
        self.swarm_controller = None
        self.swarmSpeed = 500
        self.gameOverState = gameOverState
        self.initialise()
        
    def onEnter(self, previousState):
        self.player_controller.pause(False)

    def initialise(self):
        self.swarm_controller = SwarmController(800, 48, self.swarmSpeed)
        swarm_renderer = InvaderView(self.swarm_controller, 'invaders.png')

        self.player_controller = PlayerController(0, 540)
        player_renderer = PlayerView(self.player_controller, 'ship.png')
        lives_renderer = PlayerLivesView(self.player_controller, 'ship.png')
        bullet_renderer = BulletView(self.player_controller.bullets, 'bullet.png')
        alienbullet_renderer = BulletView(self.swarm_controller.bullets, 'alienbullet.png')

        explosion_controller = ExplosionController(self.game)
        collision_controller = CollisionController(self.game, self.swarm_controller, self.player_controller, explosion_controller, self)

        explosion_view = ExplosionView(explosion_controller.list.explosions, 'explosion.png', 32, 32)

        self.renderers = [ alienbullet_renderer, swarm_renderer, bullet_renderer, player_renderer, lives_renderer, explosion_view ]
        self.controllers = [ self.swarm_controller, self.player_controller, collision_controller, explosion_controller ]

    def update(self, gameTime):
        for ctrl in self.controllers:
            ctrl.update(gameTime)	
            
        if ( self.player_controller.model.lives == 0 ):
            self.game.changeState( self.gameOverState )
            
        if ( len(self.swarm_controller.invaders) == 0 ):
            self.swarmSpeed -= 50
            if ( self.swarmSpeed < 100 ):
                self.swarmSpeed = 100
            
            self.swarm_controller.reset(48, self.swarmSpeed)
            levelUpMessage = InterstitialState( invadersGame, 'Congratulations! Level Up!', 2000, self )
            self.game.changeState ( levelUpMessage )

    def draw(self, surface):
        for view in self.renderers:
            view.render(surface)