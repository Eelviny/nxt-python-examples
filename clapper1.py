#!/usr/bin/env python

"""
This script will listen to the Sound sensor connected
to Port 1 and will print a message as soon as the
sound level is higher than a certain threshold.
"""

import nxt.locator
from nxt.sensor import *
import time

b = nxt.locator.find_one_brick()

print("Please have the Sound sensor connected to Port 1")
print(("Sound: ", Sound(b, PORT_1).get_sample()))
print("Now I wait until you clap...")
print("Use Ctrl+C to abort.")

while True:
    time.sleep(0.1)
    s = Sound(b, PORT_1).get_sample()
    if s > 300:
        print("CLAP {}".format(s))
        time.sleep(0.3)
        print("Ready again...")
    #print(("Sound: ", Sound(b, PORT_1).get_sample()))
