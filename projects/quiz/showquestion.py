from gamerunner import NullState
from ui import Text, QuestionText, Countdown

class ShowQuestion(NullState):
    def __init__(self, nextState, currentQuestion, player1, player2):
        self.nextState = nextState
        self.player1 = player1
        self.player2 = player2
        self.player1Choice = -1
        self.player2Choice = -1
        self.currentQuestion = currentQuestion
        self.showAnswer = False
        self.endCount = 3
        self.questionText = QuestionText()
            
        text = Text(32, (255, 255, 255))
        self.countdown = Countdown(30, (80, 560), 640, 32, (128, 0, 0), (255, 0, 0), text)

    def calcScore(self):
        if self.player1Choice == self.currentQuestion.answerIndex:
            self.player1.score = self.player1.score + 1
        if self.player2Choice == self.currentQuestion.answerIndex:
            self.player2.score = self.player2.score + 1
    
    def update(self, deltaTime):
        if self.player1Choice == -1:
            p1 = self.player1.playerChoice()
            if p1 >= 0:
                self.player1Choice = p1

        if self.player2Choice == -1:
            p2 = self.player2.playerChoice()
            if p2 >= 0:
                self.player2Choice = p2

        if self.player1Choice >= 0 and self.player2Choice >= 0:
            self.showAnswer = True

        if not self.showAnswer: 
            self.countdown.update(deltaTime)
            if self.countdown.finished:
                self.showAnswer = True
        else:
            self.endCount = self.endCount - deltaTime
            if self.endCount <= 0:
                self.calcScore()
                return self.nextState
            
        return self

    def draw(self, surface):
        self.questionText.draw(surface, self.currentQuestion.question, self.currentQuestion.answer, self.currentQuestion.answers, self.showAnswer)
        if not self.showAnswer:
            self.countdown.draw(surface)

    def onExit(self):
        self.endCount = 3
        self.showAnswer = False
        self.countdown.reset()

    def onEnter(self):
        self.player1Choice = -1
        self.player2Choice = -1
