from gpiozero import LED, Button
from time import sleep
from signal import pause

led1 = LED(23)

while True:
    led1.on()
    sleep(0.35)
    led1.off()
    sleep(0.15)
