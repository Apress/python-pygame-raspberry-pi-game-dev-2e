#!/usr/bin/python

class Dog(object):
    def makeNoise(self):
        print ("Bark!")

class Duck(object):
    def makeNoise(self):
        print ("Quack!")

animals = [ Dog(), Duck() ]

for a in animals:
    a.makeNoise()