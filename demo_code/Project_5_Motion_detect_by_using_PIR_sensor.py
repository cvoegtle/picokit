from machine import Pin
from machine import I2C
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
addr = i2c.scan()[0]
print(addr)
lcd = I2cLcd(i2c, addr, 2, 16)
pir_sensor = Pin(15, Pin.IN)

while True:
    reading = pir_sensor.value()
    if reading == 1:
        lcd.putstr("Bewegung\n")
        lcd.putstr("erkannt")
        sleep(1)
        lcd.clear()
