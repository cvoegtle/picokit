import time
from machine import Pin


LED = Pin(0, Pin.OUT)
onboardLED = Pin(25, Pin.OUT)

count = 0
while True:
    count += 1
    LED.value(count % 2)
    onboardLED.value(count % 2 - 1)
    time.sleep(0.8)

