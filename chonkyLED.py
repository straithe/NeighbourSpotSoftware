#!/usr/bin/python3

import time
from greatfet import GreatFET

gf = GreatFET()

# Set the pins
greenPin = gf.gpio.get_pin('J1_P23')
redPin = gf.gpio.get_pin('J2_P23') 

# Set the direction of the pins
greenPin.set_direction(gf.gpio.DIRECTION_OUT)
redPin.set_direction(gf.gpio.DIRECTION_OUT)

def redOn():
  redPin.write(True)

def redOff():
  redPin.write(False)

def greenOn():
  greenPin.write(True)

def greenOff():
  greenPin.write(False)

def yellowOn():
  redPin.write(True)
  greenPin.write(True)

def allOff():
  redPin.write(False)
  greenPin.write(False)