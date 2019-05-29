#!/usr/bin/python

def drawBox(width = 3, height = 3):

    if width < 0:
        width = 3

    if height < 0:
        height = 3

    width = width - 2

    print("+" + "-" * width + "+")
    for y in range(3, height + 1):
        print("|" + " " * width + "|")
    print("+" + "-" * width + "+")

drawBox(height = 10)
print("Between two boxes")
drawBox(5)