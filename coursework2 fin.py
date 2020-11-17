def hcf1(a, b):
    """finds highest common factor between a and b"""
    while b>0:
        a, b = b, a % b
    return a
    
from itertools import count

def hcf2(a, b):
    """finds highest common factor between a and b"""
    for n in count():
        a, b = b, a % b
        if b == 0:
            return a

def ehcf(a, b):
    """finds highest common factor between a and b"""
    p1,q1,h1,p2,q2,h2=1,0,a,0,1,b
    while h2>0:
        r=h1/h2
        p3=p1-r*p2
        q3=q1-r*q2
        h3=h1-r*h2
        p1,q1,h1,p2,q2,h2=p2,q2,h2,p3,q3,h3
    return (p1,q1,h1)
