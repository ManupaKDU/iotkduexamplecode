import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
for i in range(18,26):
    gpio.setup(i, gpio.OUT)

while True:
    for x in range(18,26): 
        gpio.output(x,True)
        time.sleep(0.05)
        gpio.output(x,False)
        time.sleep(0.05)
