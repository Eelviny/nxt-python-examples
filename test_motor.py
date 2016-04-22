#!/usr/bin/env python

"""
Asks the user to select an output Port.
Then the connected motor will turn 360 degree
forwards and then backwards with maximum speed.
"""

import nxt.locator
from nxt.motor import *

def user_select_ouput_port():
    """
    returns PORT_A, PORT_B or PORT_C
    """
    port = None
    while port is None:
        port = input("Please select a port where a motor is connected (A, B or C): ")
        if port.upper() == 'A':
            return PORT_A
        elif port.upper() == 'B':
            return PORT_B
        elif port.upper() == 'C':
            return PORT_C
        port = None

def select_and_spin(b):
    port = user_select_ouput_port();
    motor = Motor(b, port)
    motor.turn(100, 360)
    motor.turn(-100, 360)

b = nxt.locator.find_one_brick()
select_and_spin(b)
