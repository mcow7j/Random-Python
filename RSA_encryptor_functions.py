"""code used to rsa encrpt and decode messages, created to use with python 2. There are multiple bugs"""

from math import log10

def digit_count(a):
    z=log10(a)
    return int(z)+1

def ehcf(a, b):
    """ function useful for finding d in rsa p1*a+q1*b=h1"""
    p1,q1,h1,p2,q2,h2=1,0,a,0,1,b
    while h2>0:
        r=h1/h2
        p3=p1-r*p2
        q3=q1-r*q2
        h3=h1-r*h2
        p1,q1,h1,p2,q2,h2=p2,q2,h2,p3,q3,h3
    return (p1,q1,h1)

def dfinder(k,l):
    (d,g,f)=ehcf(k,l)
    if f==1:
        global d
        return d
    else:
        return False

def cypherconverter(str1):
    list1=map(lambda c: ord(c)-32, str1)
    p=0
    for n in xrange(1,len(list1)+1):
        w=len(list1)
        p=(list1[w-n]*(10**(2*(n-1))))+p
    return p

def encode(str1,e,n):
    list1=map(lambda c: ord(c)-32, str1)
    p=0
    for n in xrange(1,len(list1)+1):
        w=len(list1)
        p=(list1[w-n]*(10**(2*(n-1))))+p
    return pow(p,e,n)

def decode(Q,n,d):
    p = pow(Q,d,n)
    string1 = ''
    for t in xrange(1,((digit_count(p)/2)+1)):
        w = (digit_count(p)/2)-t
        r = (p/(10**(w*2)))-100*(p/(10**((w*2)+2)))
        string1 = string1 + chr(r+32)
    return string1

if __name__ == '__main__':
  n = 9655020917106901547888376921602009
  d = 4715242773470812287873634662919759
  e = 43
  g=encoder("Secrtet message",e,n)
  w=decode(g,n,d)
  print(g,w)
