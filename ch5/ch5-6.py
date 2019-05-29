#!/usr/bin/python

print("This program will take two strings and decide which one is greater")
tup = None 
first = input("First string: ")
second = input("Second string: ")
if first > second:
    tup = (first, second)
elif second > first:
    tup = (second, first)
if tup != None:
    print("%s is greater than %s" % tup)
else:
    print("The strings were equal")


