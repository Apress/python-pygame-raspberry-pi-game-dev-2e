#!/usr/bin/python

first = input("First string: ")
second = input("Second string: ")
if first > second:
    tup = (first, second)
else:
    tup = (second, first)
print("%s is greater than %s" % tup)

