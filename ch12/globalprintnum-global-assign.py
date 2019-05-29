#!/usr/bin/python

num = 5

def changeNum():
    global num
    num = 10

print (num)
changeNum()
print (num)