import pygame, os, sys
from pygame.locals import *

from bullet import *
from bitmapfont import *

"""
----------------------------------------------------------------------------------------------------
PlayerModel

The player model.
----------------------------------------------------------------------------------------------------
"""

class PlayerModel(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.speed = 100 # pixels per second

"""
----------------------------------------------------------------------------------------------------
Player
                            
The tank at the bottom of the screen.
----------------------------------------------------------------------------------------------------
"""

class PlayerController(object):
    
    def __init__(self, x, y):
        self.model = PlayerModel(x, y)
        # self.x = x
        # self.y = y
        self.isPaused = False
        # self.lives = 3
        # self.score = 0
        # self.speed = 100 # pixels per sec
        self.bullets = BulletController(-200) # pixels per sec
        self.shootSound = pygame.mixer.Sound('playershoot.wav')
        
    def pause(self, isPaused):
        self.isPaused = isPaused
        
    def update(self, gameTime):
        
        self.bullets.update(gameTime)
        
        if ( self.isPaused ):
            return
        
        keys = pygame.key.get_pressed()
        
        if (keys[K_RIGHT] and self.model.x < 800 - 32):
                self.model.x += ( gameTime/1000.0 ) * self.model.speed
        elif (keys[K_LEFT] and self.model.x > 0):
                self.model.x -= ( gameTime/1000.0 ) * self.model.speed
                
        if (keys[K_SPACE] and self.bullets.canFire()):
            x = self.model.x + 9 # bullet is 8 pixels
            y = self.model.y - 16
            self.bullets.addBullet(x, y)
            self.shootSound.play()
            
    def hit(self, x, y, width, height):
        return (x >= self.model.x and y >= self.model.y and x + width <= self.model.x + 32 and y + height <= self.model.y + 32)

"""
----------------------------------------------------------------------------------------------------
PlayerView
                    
Renders the player tank.
----------------------------------------------------------------------------------------------------
"""
        
class PlayerView(object):
    def __init__(self, player, imgpath):
        self.player = player
        self.image = pygame.image.load(imgpath)
        
    def render(self, surface):
        surface.blit(self.image, (self.player.model.x, self.player.model.y, 32, 32))


"""
----------------------------------------------------------------------------------------------------
PlayerLivesView
                
Renders the number of lives left for the player.
----------------------------------------------------------------------------------------------------
"""
class PlayerLivesView(object):
    def __init__(self, player, imgpath):
        self.player = player
        self.image = pygame.image.load(imgpath)
        self.font = BitmapFont('fasttracker2-style_12x12.png', 12, 12)
        
    def render(self, surface):
        x = 8
        
        for life in range(0, self.player.model.lives):
            surface.blit(self.image, (x, 8, 32, 32))
            x += 40
            
        self.font.draw(surface, '1UP SCORE: ' + str(self.player.model.score), 160, 12)
        

if ( __name__ == '__main__'):
    
    pygame.init()
    fpsClock = pygame.time.Clock()
    
    surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Player Test')
    black = pygame.Color(0, 0, 0)
    
    player = PlayerController(0, 400)
    playerView = PlayerView(player, 'ship.png')
    playerLivesView = PlayerLivesView(player, 'ship.png')
    
    while True:		
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player.update(fpsClock.get_time())
    
        surface.fill(black)
        playerView.render(surface)
        playerLivesView.render(surface)
        
        pygame.display.update()
        fpsClock.tick(30)
    