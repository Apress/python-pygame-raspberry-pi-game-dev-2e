import pygame
from pygame.locals import *

class Text(object):

    def __init__(self, size, colour):
        self.size = size
        self.colour = colour
        self.font = pygame.font.Font(None, size)

    def draw(self, surface, msg, pos, centred = False):
        x, y = pos
        tempSurface = self.font.render(msg, True, self.colour)
        if centred:
            x = x - tempSurface.get_width() / 2
            y = y + tempSurface.get_height() / 4
            pos = (x, y)
        surface.blit(tempSurface, pos)

class QuestionText(object):
    def __init__(self):
        self.questionText = Text(32, (255, 255, 0))
        self.answerText = Text(32, (255, 255, 255))
        self.disabledText = Text(32, (56, 56, 56))

    def draw(self, surface, question, answer, answers, showAnswer = False):
        y = 64
        maxWidth = 60
        lineHeight = 32
    
        if len(question) > maxWidth:
            # Split the question down in maxWidth char chunks and draw it on-screen
            question.split(" ")
            temp = ""
            for word in question:
                temp = temp + word
                if len(temp) > maxWidth:
                    self.questionText.draw(surface, temp, (400, y), True)
                    temp = ""
                    y = y + lineHeight
            self.questionText.draw(surface, temp, (400, y), True)
        else:
            self.questionText.draw(surface, question, (400, y), True)

        y = y + lineHeight * 2
        label = "A"
        for a in answers:
            font = self.answerText
            if showAnswer and a != answer:
                font = self.disabledText
            
            font.draw(surface, "%s. %s" % (label, a), (100, y), False)
            labelChar = ord(label)
            labelChar = labelChar + 1
            label = chr(labelChar)
            y = y + 40


class Countdown(object):
    def __init__(self, seconds, pos, width, height, innerColour, borderColour, text):
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

    def draw(self, surface):
        pygame.draw.rect(surface, self.innerColour, self.rect)
        pygame.draw.rect(surface, self.borderColour, self.fullRect, 2)

        x, y = self.pos
        x = x + self.width / 2
        pos = (x, y)
        self.text.draw(surface, "%02d" % self.seconds, pos, True)
        

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
