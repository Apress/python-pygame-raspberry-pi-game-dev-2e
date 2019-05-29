#!/usr/bin/python

def serialize(fileName, players):
    f = open(fileName, 'w')

    for p in players:
        f.write(p + ',' + str(players[p]) + '\n')

    f.close()


players = { 'Anna': 10000, 'Barney': 9000, 'Jane': 8000, 'Fred': 7000 }
serialize('highscores.txt', players)