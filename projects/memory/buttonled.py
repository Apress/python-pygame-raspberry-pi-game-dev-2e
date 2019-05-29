from gpiozero import LED, Button
import random

class ButtonLED(object):
    def __init__(self, ledPin, buttonPin):
        self.led = LED(ledPin)
        self.button = Button(buttonPin)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def wait(self, timeout):
        self.button.wait_for_press(timeout)
        return self.button.is_pressed
        

class ButtonLEDCollection(object):
    def __init__(self):
       led1 = ButtonLED(23, 4)
       led2 = ButtonLED(12, 17)
       led3 = ButtonLED(16, 22)
       led4 = ButtonLED(21, 6)

       self.items = [ led1, led2, led3, led4 ]

    def pick(self, count):
        leds = self.items
        random.shuffle(leds)
        picked = []
        for n in range(0, count):
            picked.append(leds[n])
        return picked

    def waitForClick(self):
        isPressed = False
        while not isPressed:
            for led in self.items:
                isPressed = isPressed or led.button.is_pressed
            

if __name__=='__main__':
    from time import sleep    
    collection = ButtonLEDCollection()

    leds = collection.pick(4)
    for led in leds:
        led.on()
        sleep(1)
        led.off()
