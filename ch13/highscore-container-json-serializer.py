#!/usr/bin/python
import json

def serialize(fileName, players):
    f = open(fileName, 'w')
    json.dump(players, f)
    f.close()

players = { 'Anna': 10000, 'Barney': 9000, 'Jane': 8000, 'Fred': 7000 }
serialize('jsonhiscore.txt', players)