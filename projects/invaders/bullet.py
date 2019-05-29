import pygame, os, sys
from pygame.locals import *

"""
----------------------------------------------------------------------------------------------------
    BulletModel
                
    A single bullet for the player.
----------------------------------------------------------------------------------------------------
"""
class BulletModel(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def update(self, delta):
        self.y = self.y + delta

"""
----------------------------------------------------------------------------------------------------
Bullet Manager
                        
Manages the update for each bullet.
----------------------------------------------------------------------------------------------------
"""

class BulletController(object):
    
    def __init__(self, speed):
        self.countdown = 0
        self.bullets = []
        self.speed = speed
    
    def clear(self):
        self.bullets[:] = []
    
    def canFire(self):
        return self.countdown == 0 and len(self.bullets) < 3
        
    def addBullet(self, x, y):
        self.bullets.append(BulletModel(x, y))
        self.countdown = 1000
        
    def removeBullet(self, bullet):
        self.bullets.remove(bullet)

    def update(self, gameTime):
        killList = []
        
        if (self.countdown > 0):
            self.countdown = self.countdown - gameTime
        else:
            self.countdown = 0
        
        for b in self.bullets:
            b.update( self.speed * ( gameTime / 1000.0 ) )
            if (b.y < 0):
                killList.append(b)
                
        for b in killList:
            self.removeBullet(b)

"""
----------------------------------------------------------------------------------------------------
BulletView
        
Renders the bullets for the player's missiles.
----------------------------------------------------------------------------------------------------
"""

class BulletView(object):
    
    def __init__(self, bulletController, imgpath):
        self.BulletController = bulletController
        self.image = pygame.image.load(imgpath)
        
    def render(self, surface):
        for b in self.BulletController.bullets:
            surface.blit(self.image, (b.x, b.y, 8, 8))
