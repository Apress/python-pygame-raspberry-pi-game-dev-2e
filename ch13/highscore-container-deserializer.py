#!/usr/bin/python

def deserialize(fileName, players):
    f = open(fileName, 'r')

    for entry in f:
        split = entry.split(',')
        name = split[0]
        score = int(split[1])

        players[name] = score

players = { }
deserialize('highscores.txt', players)

print(players)
