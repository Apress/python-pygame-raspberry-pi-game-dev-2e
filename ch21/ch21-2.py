from gpiozero import LED, Button
from time import sleep

led = LED(4)
button = Button(17)


ledOn = False

while True:
    if button.is_pressed:
        ledOn = not ledOn

        if ledOn:
            led.blink()
        else:
            led.off()
        
