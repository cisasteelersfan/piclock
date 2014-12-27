
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def initialize():
	GPIO.setup(17, GPIO.OUT) #Red
	GPIO.setup(27, GPIO.OUT) #Green
	GPIO.setup(22, GPIO.OUT) #Blue

def turnOff():
	GPIO.output(17, 0)
	GPIO.output(27, 0)
	GPIO.output(22, 0)


def turnOn():
	GPIO.output(17, 1)
	GPIO.output(27, 1)
	GPIO.output(22, 1)

initialize()
turnOn()
time.sleep(1)
turnOff()
time.sleep(1)
turnOn()
time.sleep(1)
turnOff()
time.sleep(1)
turnOn()
time.sleep(1)
turnOff()
GPIO.cleanup()
