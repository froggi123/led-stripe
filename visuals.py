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
              
def led_position(strip,color=(90,90,90),position=0,size=1):
    """turn on LED at desired position"""
    strip.setPixelColor(position, color)
    strip.show()
        