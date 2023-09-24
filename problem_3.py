import RPi.GPIO as gpio
import time
# import tkinter as tk
import tkinter as tk
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(14,gpio.OUT)
gpio.output(14,False)
gpio.output(15,False)
gpio.output(18,False)

window = tk.Tk()
window.title('Check Button')
#window.geometry('500x500')
 
l = tk.Label(window, bg='white', width=40, text='Select LED')
l.pack()
 
def print_selection():
    if (var1.get() == True) :
        gpio.output(18,True)
        #gpio.output(14,False)
        #gpio.output(15,False)
        print('Red')
        
    if (var1.get() == False) :
        gpio.output(18,False)
        
    if (var2.get() == True):
        gpio.output(15,True)
        #gpio.output(14,False)
        #gpio.output(18,False)
        print('Yellow')
    if (var2.get() == False):
        gpio.output(15,False)
        
    if (var3.get() == True):
        gpio.output(14,True)
        #gpio.output(15,False)
        #gpio.output(18,False)
        print('Green')
    if (var3.get() == False):
        gpio.output(14,False)
   #
        
 
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
c1 = tk.Checkbutton(window, text='red',variable=var1, onvalue=True, offvalue=False, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='yellow',variable=var2, onvalue=True, offvalue=False, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='greeny',variable=var3, onvalue=True, offvalue=False, command=print_selection)
c3.pack() 
window.mainloop()





