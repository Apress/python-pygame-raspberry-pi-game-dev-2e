#!/usr/bin/python3

import pygame
from gamerunner import GameRunner
from questions import *
from headertextscreen import HeaderTextScreen
from choosequestion import ChooseQuestion
from playercontroller import PlayerController
from showquestion import ShowQuestion
from showscore import ShowScore
from currentquestion import CurrentQuestion

pygame.init()

player1 = PlayerController([4, 17, 22])
player2 = PlayerController([5, 6, 13])

currentQuestion = CurrentQuestion()

# Questions
questions = loadQuestions("questions.json")
showQuestion = ShowQuestion(None, currentQuestion, player1, player2)
gameOver = ShowScore(None, player1, player2, True)
chooseQuestion = ChooseQuestion(showQuestion, gameOver, currentQuestion, questions)
showScore = ShowScore(chooseQuestion, player1, player2)
showQuestion.nextState = showScore

# Interstitial screen
interstitial = HeaderTextScreen(chooseQuestion, player1, player2, 3)
interstitial.setHeader("Get Ready!")
interstitial.setSub("")

# Splash screen (starts the game)
splashScreen = HeaderTextScreen(interstitial, player1, player2)
splashScreen.setHeader("QUIZ!")
splashScreen.setSub("Press any button to start")

game = GameRunner((800, 600), "Quiz", (0, 0, 0), splashScreen)


"""
States:
    Title screen
    Load the questions
    Choose next question (*)
    Display questions
    Show correct answer
    Show who won
    Display scores
    Jump back to (*) if there are more questions
    Show final winner   
    End game
"""

lastState = None
while game.state != None:
    nextState = game.update()
    if nextState != lastState:
        if game.state != None:
            game.state.onExit()
        if nextState != None:
            nextState.onEnter()
        lastState = nextState
    game.draw()

pygame.quit()
