from gpiozero import LED
from time import sleep

led = LED(4)
led.on() 
sleep(1)
led.off()
sleep(1)
