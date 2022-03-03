import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]

gpio.cleanup()