import RPi.GPIO as gpio
import time
# import tkinter as tk
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(14,gpio.OUT)


while(1):
    gpio.output(18,True)
    time.sleep(2)
    # gpio.output(18,False)
    gpio.output(15,True)
    time.sleep(2)
    gpio.output(15,False)
    gpio.output(18,False)
    gpio.output(14,True)
    time.sleep(2)
    gpio.output(14,False)
