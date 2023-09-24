import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(9, gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(10, gpio.IN,pull_up_down=gpio.PUD_UP)
for i in range(18,26):
    gpio.setup(i, gpio.OUT)

while True:
    #if gpio.add_event_detect(10,gpio.callback=button_callback):
    if gpio.input(9) == gpio.LOW:
        for x in range(18,26): 
            gpio.output(x,True)
            time.sleep(0.05)
            gpio.output(x,False)
            time.sleep(.05)
    if gpio.input(10) == gpio.LOW:
            gpio.output(x,False)
            
