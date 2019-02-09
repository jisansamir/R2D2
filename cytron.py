import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk



def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)

def forward(tf):
    gpio.output(7, gpio.HIGH)
    gpio.output(11, gpio.HIGH)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    gpio.output(7, gpio.LOW)
    gpio.output(11, gpio.HIGH)
    time.sleep(tf)
    gpio.cleanup()

def key_input(event):
    init()
    print 'key:', event.char
    key_press = event.char
    sleep_time = 0.0000001

    if key_press.lower() =='w':
        forward(sleep_time)
    elif key_press.lower() =='s':
        reverse(sleep_time)
    else :
        print "try again "


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
