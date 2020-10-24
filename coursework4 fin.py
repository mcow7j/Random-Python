9655020917106901547888376921602009

n=99158679366511727*97369398007206967
n=9655020917106901547888376921602009

e = 43

#ist1=map(lambda c: ord(c)-32,'My name is Bond')
#str1=""
#for n in xrange(1,len(list1)+1):
 #   if list1(n)==0:
  #      str1=str1+'00'
   # else:
    #    w=list1(n)
     #   str2=
def cypherconverter(str1):
    list1=map(lambda c: ord(c)-32, str1)
    p=0       
    for n in xrange(1,len(list1)+1):
        w=len(list1)
        p=(list1[w-n]*(10**(2*(n-1))))+p
    print p
 
def encoder2(str1,e,n):
    list1=map(lambda c: ord(c)-32, str1)
    p=0       
    for n in xrange(1,len(list1)+1):
        w=len(list1)
        p=(list1[w-n]*(10**(2*(n-1))))+p
    pow(p,e,n)
    
from math import log10

def digitcount(a):
    z=log10(a)
    return int(z)+1
    
def decode6(Q):
    d=4715242773470812287873634662919759
    n=9655020917106901547888376921602009
    p = pow(Q,d,n)
    string1 = ''
    for t in xrange(1,((digit_count(p)/2)+1)):
        w = (digit_count(p)/2)-t
        r = (p/(10**(w*2)))-100*(p/(10**((w*2)+2)))
        string1 = string1 + chr(r+32)
    return string1



def digit_count(a):
    z=log10(a)
    return int(z)+1
