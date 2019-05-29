#!/usr/bin/python

topNum = int(input("Sum of numbers to? "))
count = 0

while topNum > 0:
    count += topNum
    topNum = topNum - 1

print("Sum of all numbers is %d" % count)
