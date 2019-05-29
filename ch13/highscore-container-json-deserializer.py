#!/usr/bin/python
import json

def deserialize(fileName):
    f = open(fileName, 'r')
    players = json.load(f)
    f.close()

    return players

players = deserialize('jsonhiscore.txt')
print (players)