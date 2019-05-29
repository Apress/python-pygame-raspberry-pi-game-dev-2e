import pygame
from pygame.locals import *

# Music 'The Elevator Bossa Nova' by BenSounds https://www.bensound.com
# It's available on the website as an MP3. I used Audacity https://sourceforge.net/projects/audacity/
# to convert it to OGG

# Helper print class to make drawing text less repetitive in the main body of the code
class Print:

    # Constructor
    def __init__(self):
        self.font = pygame.font.Font(None, 32)

    # Draw the text on the screen at the given co-ordinates
    def draw(self, surface, msg, position):
        obj = self.font.render(msg, True, (255, 255, 255))
        surface.blit(obj, position)


pygame.init()
pygame.mixer.init()

fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
out = Print()

song = pygame.mixer.Sound('bensound-theelevatorbossanova.ogg')
song.play(-1)

running = True
paused = False
fading = False
volume = 1

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.fadeout(1000)
        elif event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                if paused:
                    pygame.mixer.pause()
                else:
                    pygame.mixer.unpause()
            elif event.key == pygame.K_ESCAPE and not fading:
                fading = True
                pygame.mixer.fadeout(1000)
            elif event.key == pygame.K_LEFTBRACKET:
                volume = volume - 0.1
                if volume < 0:
                    volume = 0
                song.set_volume(volume)
            elif event.key == pygame.K_RIGHTBRACKET:
                volume = volume + 0.1
                if volume > 1:
                    volume = 1
                song.set_volume(volume)

    if not pygame.mixer.get_busy():
        running = False

    surface.fill((0, 0, 0))

    out.draw(surface, "Press <SPACE> to pause / unpause the music", (4, 4))
    out.draw(surface, "Press <ESC> to fade out and close program", (4, 36))
    out.draw(surface, "Press [ and ] to alter the volume", (4, 68))
    out.draw(surface, "Current volume: {0:1.2f}".format(volume), (4, 100))

    pygame.display.update()
    fpsClock.tick(30)

pygame.mixer.quit()
pygame.quit()