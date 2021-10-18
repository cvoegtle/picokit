from machine import Pin, PWM
from time import sleep
from math import floor, sin, fabs, pi

RED_PIN = 0
BLUE_PIN = 1
MOTOR_PIN = 2

COLOR_MAX_DUTY = 4000


def setup_pwm(pin, freq=1024, initial_duty=0):
    pwn = PWM(Pin(pin))
    pwn.freq(freq)
    pwn.duty_u16(initial_duty)
    return pwn


motor_pwm = setup_pwm(pin=MOTOR_PIN, freq=50)
red_pwm = setup_pwm(pin=RED_PIN)
blue_pwm = setup_pwm(pin=BLUE_PIN, initial_duty=COLOR_MAX_DUTY)

duty = 0
motor_pwm.duty_u16(duty)
sleep(0.1)

min_duty = 2500
max_duty = 8050
min_degrees = 0
degrees_full_circle = 360
degrees_half_circle = degrees_full_circle / 2


def degrees_to_duty(degrees):
    # increment value per degree
    duty_step = ((max_duty - min_duty) / degrees_half_circle)

    if degrees > degrees_half_circle:
        degrees = degrees_half_circle
    elif degrees < min_degrees:
        degrees = min_degrees

    # Get the duty value for the degrees
    duty = floor((duty_step * degrees) + min_duty)

    # Check value not out of bounds
    if duty > max_duty:
        duty = max_duty
    elif duty < min_duty:
        duty = min_duty

    return duty


def calculate_color_duty(x):
    return int(COLOR_MAX_DUTY * sin(2 * x))


loop_count = 0
degrees = 0
while True:
    x = loop_count * 0.01
    color_duty = calculate_color_duty(x)
    degrees = int(fabs(((x % (2 * pi)) / (2 * pi)) * degrees_full_circle - degrees_half_circle))
    if degrees % 5 == 0:
        print(f'x {x} c {color_duty} d {degrees}')
        duty = degrees_to_duty(degrees)
        motor_pwm.duty_u16(duty)
    red_pwm.duty_u16(COLOR_MAX_DUTY + color_duty)
    blue_pwm.duty_u16(COLOR_MAX_DUTY - color_duty)
    sleep(0.01)
    loop_count += 1
