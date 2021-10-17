from machine import Pin
from time import sleep

START_INTERVAL = 0.3
MIN_INTERVAL = 0.06
INTERVAL_DECREMENT = 0.02
INTERVAL_CHANGE_TIME = START_INTERVAL*2


def flash_leds():
    onboard_led = Pin(25, Pin.OUT)

    LEDs = [Pin(i, Pin.OUT) for i in range(4)]
    clear(LEDs)

    interval = START_INTERVAL
    interval_time = 0
    while True:
        interval_time += interval
        if interval_time >= INTERVAL_CHANGE_TIME:
            interval_time = 0
            interval -= INTERVAL_DECREMENT

        if interval < MIN_INTERVAL:
            interval = START_INTERVAL
            LEDs = reverse_leds(LEDs)
            print(LEDs)

        print(f'Interval {interval}')
        onboard_led.toggle()
        for led in LEDs:
            led.toggle()
            sleep(interval)


def reverse_leds(leds):
    leds = leds[::-1]
    clear(leds)
    return leds


def clear(leds):
    for led in leds:
        led.value(0)


flash_leds()
