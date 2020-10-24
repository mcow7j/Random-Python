def power_of_two_divisor1(a):
     n = 0
     while a % 2 == 0:
         n = n+1
         a = a/2
     return n
   


from itertools import count

def power_of_two_divisor2(a):
    for n in count():
        if not(a % 2 == 0):
            return n
        else:
            a = a/2


from math import *

def digitcount(a):
    z=log10(a)
    return int(z)+1

def divisor3(a):
    for n in count():
        if not(a % 2 == 0):
            s=n
            d=a
            return (s, d)
        else:
            a = a/2
            