#!/usr/bin/python
import os

def fileExists(fileName):
    try:
        f = open(fileName, 'r')
        f.close()
        return True
    except IOError:
        return False

print (fileExists('filenotfound.py'))
print (fileExists('this-does-not-exist.txt'))