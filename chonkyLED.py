#!/usr/bin/python3
# This code is for the Spot neighbour for GreatFET.
# This code works when Spot is plugged into GreatFET.
# Load this file into a Python interpretive shell using:
#   exec(open("chonkyLED.py").read())

import time
from greatfet import GreatFET

gf = GreatFET()

# Set the pins
greenPin = gf.gpio.get_pin('J1_P23')
redPin = gf.gpio.get_pin('J2_P23') 

# Set the direction of the pins
greenPin.set_direction(gf.gpio.DIRECTION_OUT)
redPin.set_direction(gf.gpio.DIRECTION_OUT)

# Turn the red LED on.
def redOn():
  redPin.write(True)

# Turn the red LED off.
def redOff():
  redPin.write(False)

# Blink the red LED.
def redBlink():
  for i in range(10):
    redPin.write(not redPin.read())
    time.sleep(0.2)

# Turn the green LED on.
def greenOn():
  greenPin.write(True)

# Turn the green LED off.
def greenOff():
  greenPin.write(False)

# Blink the green LED.
def greenBlink():
  for i in range(10):
    greenPin.write(not greenPin.read())
    time.sleep(0.2)

# Turn both the green and red LED on.
def yellowOn():
  redPin.write(True)
  greenPin.write(True)

# Turn both the green and red LED off.
def allOff():
  redPin.write(False)
  greenPin.write(False)
