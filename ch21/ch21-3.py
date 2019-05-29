from gpiozero import LED, Button
from time import sleep

led = LED(4)
button = Button(17)
quitButton = Button(6)


ledOn = False
running = True

while running:

    if quitButton.is_pressed:
        running = False
    
    if button.is_pressed:
        ledOn = not ledOn

        if ledOn:
            led.blink()
        else:
            led.off()
        
