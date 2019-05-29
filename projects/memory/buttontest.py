#!/usr/bin/python3

from gpiozero import LED, Button
from time import sleep

pair1 = (LED(23), Button(4))
pair2 = (LED(12), Button(17))
pair3 = (LED(16), Button(22))
pair4 = (LED(21), Button(6))

pairs = [ pair1, pair2, pair3, pair4 ]

while True:
    for pair in pairs:
        if pair[1].is_pressed:
            pair[0].on()
        else:
            pair[0].off()
