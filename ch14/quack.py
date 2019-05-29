#!/usr/bin/python
class Duck:
    def Quack(self):
        print ("Duck quack!")

class Person:
    def Quack(self):
        print ("Person quack!")

def makeItQuack(duck):
    duck.Quack()

duck = Duck()
person = Person()

makeItQuack(duck)
makeItQuack(person)
