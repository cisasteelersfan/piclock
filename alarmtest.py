#!/usr/bin/env python3

import os
import time
from math import *

red = 17
green = 22
blue = 23
leds = [17, 22, 23]

def main():
#        fade(red, 25)
#        fade(blue, 50)
#        fade(green, 20)
#        flash(red, 30)
        sunrise(6)
        time.sleep(300)
        allOff()
def antilog(x):
        '''Input: Float 0-100
           Output: Float 0-100, scaled appropriately to make LED increase
           in brightness appear more linear.
           '''
        return (1/(1+exp(((x/21)-3)*-2))*102.5)


def setColor(pin, value):
        os.system('echo "%d=%f" >/dev/pi-blaster' % (pin, value))

def sunrise(timeSleep):
        for i in range(100):
                for led in leds:
                        setColor(led, antilog(i)/100)
                        print("color "+str(led)+" "+str(antilog(i)/100))
                time.sleep(timeSleep)


def fade(pincolor, delay):
        for i in range(100):
                setColor(pincolor, antilog(i)/100)
                time.sleep(delay/1000)
                print(antilog(i)/100)
        setColor(pincolor, 0)

def flash(pincolor, delay):
        for i in range(100):
                setColor(pincolor, 1)
                time.sleep(delay/1000)
                setColor(pincolor, 0)
                time.sleep(delay/1000)
def allOff():
        for led in leds:
                setColor(led, 0)


main()
print('Done')
