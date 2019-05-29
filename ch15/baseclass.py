#!/usr/bin/python

class MyBaseClass(object):
    def methodOne(self):
        print ("MyBaseClass::methodOne()")

class MyChildClass(MyBaseClass):
    def methodOne(self):
        print ("MyChildClass::methodOne()")

def callMethodOne(obj):
    obj.methodOne()

instanceOne = MyBaseClass()
instanceTwo = MyChildClass()

callMethodOne(instanceOne)
callMethodOne(instanceTwo)
