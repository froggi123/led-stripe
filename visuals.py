#!/usr/bin/env python3
# Author: Martin Frauchiger
#
# various animations on a strip of WS2811 LEDs
# for usage see example in strandtest

import time
from rpi_ws281x import *
import argparse
from random import random, randint
import math


# Define functions which animate LEDs in various ways.
              
def led_position(strip,color=(90,90,90),position=0,size=1,show=True):
    """turn on LED at desired position"""
    lowIndex = position // 1                # is the index of the lowest LED positon
    lowStrength = 1 - position % 1          # is the Ratio of the lowest position. Assumed linear behavior. The closer the position to lowIndex the brighter it needs to be.
    print("[0] lowIndex, [1] lowStrength, [2] position, [3] color".format(lowIndex, lowStrength, position, color))  # debug output
    strip.setPixelColor(lowIndex, (lowStrength*color[0],lowStrength*color[1],lowStrength*color[2]))    # actually there are no checks implemented, if Index is fine
    highStrength = 1 - lowStrength
    strip.setPixelColor(lowIndex+1, (highStrength*color[0],highStrength*color[1],highStrength*color[2]))
    if show==True:                          # usefull if used just for calculation
        strip.show()
        
