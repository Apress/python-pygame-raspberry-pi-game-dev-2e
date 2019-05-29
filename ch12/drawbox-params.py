#!/usr/bin/python

def drawBox(width, height):

    if width < 0:
        width = 3

    if height < 0:
        height = 3

    width = width - 2

    print("+" + "-" * width + "+")
    for y in range(3, height + 1):
        print("|" + " " * width + "|")
    print("+" + "-" * width + "+")

drawBox(5, 4)
print("Between two boxes")
drawBox(4, 5)