""" includes function used to decode rsa encrpyted messagfes givin certain important info""" 

from math import log10

def digitcount(a):
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
    
def decode7(c,e,n,q):
    dfinder(e,q)
    p = pow(c,d,n)
    string1 = ''  
    for t in xrange(1,((digitcount(p)/2)+1)):
        w = (digitcount(p)/2)-t
        r = (p/(10**(w*2)))-100*(p/(10**((w*2)+2)))
        string1 = string1 + chr(r+32)
    return string1
