"""module to to find the next prime number using miller rabin test, given integer n.
-isprime uses miller rabin test test if prime number
-next primes uses isprime"""

from itertools import *
from random import *

def divisor(b):
    for i in count():
        if not(b % 2 == 0):
            global s,d
            s=i
            d=b
            return s, d
        else:
            b = b/2

def miller(n,a):
    divisor(n-1)
    list1=[]
    for m in xrange(max(1,s)):
        list1.append(pow(a,(2**m)*d,n))
    return list1

def miller_rabin_test(n,a):
    divisor(n-1)
    if pow(a,d,n)==1:
        return True
    for m in xrange(max(1,s)):
        x=pow(a,(2**m)*d,n)
        if x==n-1:
            return True
    return False

def isprime(n):
    v=0
    for i in xrange(10):
        u=randint(2,n-2)
        if miller_rabin_test(n,u)==True:
            v=v+1
    if v==10:
        return True
    else:
        return False

def nextprime(n):
    if n%2==0:
        for i in count(n+1,2):
            if isprime(i)==True:
                return i
    else:
        for i in count(n+2,2):
            if isprime(i)==True:
                return i
    
    
    
    
    
    
    
    
    
