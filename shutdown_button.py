#!/usr/bin/python3
# -*- coding: utf-8 -*-
# example gpiozero code that could be used to have a shutdown function on one GPIO button
off_button=27                      
on_button=3

from gpiozero import Button
from signal import pause
from subprocess import check_call

held_for_off=0.0

def rlsOff():
        global held_for_off         
        if (held_for_off > 5.0):
                check_call(['/sbin/poweroff'])
        else:
        	held_for_off = 0.0

def hldOff():
        # callback for when button is held
        #  is called every hold_time seconds
        global held_for_off
        #turn off backlight 
        # need to use max() as held_time resets to zero on last callback
        held_for_off = max(held_for_off, offButton.held_time + offButton.hold_time)

offButton=Button(off_button, hold_time=1.0, hold_repeat=True)
offButton.when_held = hldOff
offButton.when_released = rlsOff

pause() # wait forever
