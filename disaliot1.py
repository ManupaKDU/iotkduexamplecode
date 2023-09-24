import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

while True:
    gpio.output(18,True)
    time.sleep(1)
    gpio.output(18,False)
    time.sleep(1)
