n=9655020917106901547888376921602009
e = 43



def encoder1(str1,e,a):
    list1=map(lambda c: ord(c)-32, str1)
    p=0       
    for n in xrange(1,len(list1)+1):
        w=len(list1)
        p=(list1[w-n]*(10**(2*(n-1))))+p
    y=pow(p,e,a)
    return y   

from math import log10

def digitcount(a):
    z=log10(a)
    return int(z)+1
    
def decode1(Q,d,n):
    p = pow(Q,d,n)
    string1 = ''
    for t in xrange(1,((digitcount(p)/2)+1)):
        w = (digitcount(p)/2)-t
        r = (p/(10**(w*2)))-100*(p/(10**((w*2)+2)))
        string1 = string1 + chr(r+32)
    return string1