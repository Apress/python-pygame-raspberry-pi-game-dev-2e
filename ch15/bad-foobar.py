#!/usr/bin/python

class Foo(object):
    x = 0

    def __init__(self):
        print ("Foo constructor")
        self.x = 10

    def printNumber(self):
        print (self.x)

class Bar(Foo):
    def __init__(self):
        print ("Bar constructor")

b = Bar()
b.printNumber()