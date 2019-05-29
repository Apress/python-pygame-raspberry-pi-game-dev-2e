#!/usr/bin/python

players = ['Anna,10000', 'Barney,9000', 'Jane,8000', 'Fred,7000']

f = open('highscores.txt', 'w')
for p in players:
    f.write(p + '\n')

f.close()