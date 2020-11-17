""" module with 2 different functions to find the highest common factor between 2 intergers a,b """

from itertools import count

def hcf1(a, b):
    """finds highest common factor between a and b"""
    while b>0:
        a, b = b, a % b
    return a

def hcf2(a, b):
    """finds highest common factor between a and b"""
    for n in count():
        a, b = b, a % b
        if b == 0:
            return a
