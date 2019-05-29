# Our imports

import pygame, os, sys
from pygame.locals import *

from player import *
from bullet import *
from swarm import *
from interstitial import *

class ExplosionModel(object):
    def __init__(self, x, y, maxFrames, speed, nextState = None):
        self.x = x
        self.y = y
        self.maxFrames = maxFrames
        self.speed = speed
        self.initialSpeed = speed
        self.frame = 0
        self.nextState = nextState
        
class ExplosionModelList(object):
    
    def __init__(self, game):
        self.explosions = []
        self.game = game
        
    def add(self, explosion, nextState = None):
        x, y, frames, speed = explosion
        exp = ExplosionModel(x, y, frames, speed, nextState)
        self.explosions.append(exp)
        
    def cleanUp(self):
        
        killList = []
        
        for e in self.explosions:
            if ( e.frame == e.maxFrames ):
                killList.append(e)
                
        nextState = None
                
        for e in killList:
            if (nextState == None and e.nextState != None):
                nextState = e.nextState
                
            self.explosions.remove(e)
            
        if (nextState != None):
            self.game.changeState(nextState)
        
class ExplosionView(object):
    def __init__(self, explosions, explosionImg, width, height):
        self.image = pygame.image.load(explosionImg)
        self.image.set_colorkey((255, 0, 255))
        self.explosions = explosions
        self.width = width
        self.height = height
    
    def render(self, surface):
        for e in self.explosions:
            surface.blit(self.image, ( e.x, e.y, self.width, self.height ), (e.frame * self.width, 0, self.width, self.height) )
            
class ExplosionController(object):
    
    def __init__(self, game):
        self.list = ExplosionModelList(game)
        
    def update(self, gameTime):
        for e in self.list.explosions:
            e.speed -= gameTime
            if ( e.speed < 0 ):
                e.speed += e.initialSpeed
                e.frame += 1
            
        self.list.cleanUp()

class CollisionController(object):
    def __init__(self, game, swarm, player, explosionController, playState):
        self.swarm = swarm
        self.player = player
        self.game = game
        self.BulletController = player.bullets
        self.EnemyBullets = swarm.bullets
        self.expCtrl = explosionController
        self.playGameState = playState
        self.alienDeadSound = pygame.mixer.Sound('aliendie.wav')
        self.playerDie = pygame.mixer.Sound('playerdie.wav')

#	def render(self, surface):
#		for b in self.BulletController.bullets:
#			pygame.draw.rect(surface, (255, 0, 0), (b.x+3, b.y+3, 8, 12), 1)
        
    def update(self, gameTime):
        
        aliens = []
        bullets = []
        
        for b in self.BulletController.bullets:
            
            if (bullets.count(b)>0):
                continue
            
            for inv in self.swarm.invaders:
                if (inv.hit(b.x+3, b.y+3, 8, 12)):
                    aliens.append(inv)
                    bullets.append(b)
                    break
            
        for b in bullets:
            self.BulletController.removeBullet(b)
            
        for inv in aliens:
            self.swarm.invaders.remove(inv)
            self.player.model.score += (10 * (inv.alientype + 1))
            self.expCtrl.list.add((inv.x, inv.y, 6, 50))
            self.alienDeadSound.play()
            
        playerHit = False
            
        for b in self.EnemyBullets.bullets:
            if ( self.player.hit (b.x+3, b.y+3, 8, 12 ) ):
                self.player.model.lives -= 1
                playerHit = True
                break
                
        if ( playerHit ):
            self.EnemyBullets.clear()
            self.player.bullets.clear()
            
            if ( self.player.model.lives > 0 ):
                self.player.pause(True)
                getReadyState = InterstitialState( self.game, 'Get Ready!', 2000, self.playGameState )
                self.expCtrl.list.add((self.player.model.x, self.player.model.y, 6, 50), getReadyState)
                
            self.playerDie.play()