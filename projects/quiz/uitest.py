#!/usr/bin/python3
import pygame, os, sys
from pygame.locals import *
from gpiozero import Button

class Text(object):

    def __init__(self, surface, size, colour):
        self.surface = surface
        self.size = size
        self.colour = colour
        self.font = pygame.font.Font(None, size)

    def draw(self, msg, pos, centred = False):
        x, y = pos
        tempSurface = self.font.render(msg, True, self.colour)
        if centred:
            x = x - tempSurface.get_width() / 2
            y = y + tempSurface.get_height() / 4
            pos = (x, y)
        self.surface.blit(tempSurface, pos)

class QuestionText(object):
    def __init__(self, surface, question, answer, answers):
        self.questionText = Text(surface, 32, (255, 255, 0))
        self.answerText = Text(surface, 32, (255, 255, 255))
        self.disabledText = Text(surface, 32, (56, 56, 56))
        self.question = question
        self.answer = answer
        self.answers = answers

    def draw(self, showAnswer = False):
        self.questionText.draw(self.question, (400, 64), True)

        y = 160
        label = "A"
        for answer in self.answers:
            font = self.answerText
            if showAnswer and answer != self.answer:
                font = self.disabledText
            
            font.draw("%s. %s" % (label, answer), (100, y), False)
            labelChar = ord(label)
            labelChar = labelChar + 1
            label = chr(labelChar)
            y = y + 40

class Countdown(object):
    def __init__(self, surface, seconds, pos, width, height, innerColour, borderColour, text):
        self.surface = surface
        self.maxSeconds = seconds
        self.seconds = seconds
        self.pos = pos
        self.width = width
        self.height = height
        self.finished = False
        
        self.text = text
        self.innerColour = innerColour
        self.borderColour = borderColour
        self.fullRect = Rect(pos, (width, height))
        self.rect = Rect(pos, (width, height))

    def draw(self):
        pygame.draw.rect(self.surface, self.innerColour, self.rect)
        pygame.draw.rect(self.surface, self.borderColour, self.fullRect, 2)

        x, y = self.pos
        x = x + self.width / 2
        pos = (x, y)
        self.text.draw("%02d" % self.seconds, pos, True)
        

    def reset(self):
        self.finished = False
        self.seconds = self.maxSeconds

    def update(self, deltaTime):
        if self.seconds == 0:
            return
        
        self.seconds = self.seconds - deltaTime
        if self.seconds < 0:
            self.seconds = 0
            self.finished = True
        progressWidth = self.width * (self.seconds / self.maxSeconds)
        self.rect = Rect(self.pos, (progressWidth, self.height))


if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))

    text = Text(surface, 32, (255, 255, 255))
    questionText = QuestionText(surface, "What letter follows 'C' in the alphabet?", "D", ["A", "B", "D"])
    countdown = Countdown(surface, 30, (80, 560), 640, 32, (128, 0, 0), (255, 0, 0), text)

    background = (0, 0, 0) # Black

    while True:
        surface.fill(background)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        deltaTime = fpsClock.tick(30) / 1000.0
        countdown.update(deltaTime)
        
        countdown.draw()
        questionText.draw(True)
        
        pygame.display.update()
    
