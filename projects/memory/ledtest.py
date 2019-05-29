#!/usr/bin/python3

from gpiozero import LED
from time import sleep

leds = [ LED(23), LED(12), LED(16), LED(21) ]

while True:
    for led in leds:
        led.on()
        sleep(0.5)
        led.off()
