#!/usr/bin/python3

import sys
from time import sleep
from buttonled import ButtonLED, ButtonLEDCollection

collection = ButtonLEDCollection()

print ("Welcome to the Game of Memory!")
print ("A sequence of LEDs will flash, ")
print ("you will be asked to repeat the")
print ("pattern. Press any button to start")

collection.waitForClick()

for n in range(1, 5):
    leds = collection.pick(n)
    print ("Remember this sequence")
    for led in leds:
        led.on()
        sleep(1)
        led.off()
    print("Your turn!")
    for led in leds:
        if led.wait(1):
            led.on()
            sleep(0.5)
            led.off()
        else:
           print ("Missed! Game Over!")
           sys.exit()

print ("Congratulations!")
