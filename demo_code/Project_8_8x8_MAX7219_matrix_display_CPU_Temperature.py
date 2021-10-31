from machine import Pin, SPI, ADC
import max7219
from utime import sleep


MAX7219_NUM = 4
MAX7219_INVERT = False
READ_TEMPERATURE_DELAY = 5
cs_pin = 5

spi = SPI(0)
display = max7219.Matrix8x8(spi=spi, cs=Pin(cs_pin), num=MAX7219_NUM)
display.brightness(2)

p = MAX7219_NUM * 8
to_volts = 3.3 / 65535
temper_sensor = ADC(4)

while True:
    temper_volts = temper_sensor.read_u16() * to_volts
    celsius_degrees = 27 - (temper_volts - 0.706) / 0.001721
    text = str(round(celsius_degrees, 1)) + '°C'

    display.fill(MAX7219_INVERT)
    display.text(text, 0, 1, not MAX7219_INVERT)
    display.show()
    sleep(READ_TEMPERATURE_DELAY)
