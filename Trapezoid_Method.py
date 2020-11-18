"""includes function to produce graphs of trapeziod problem in readme, it uses
the trapezium rule to work out the area with interval 0.01"""
import numpy as np
import matplotlib.pyplot as plt

def trape(nlist=[0,1,5,2,4,7,9,6]):
    """ outputs a list of values of the green area given a list of n values """
    areaslist=[]

    x=np.arange(0,13.01,0.01)
    y=np.sin(np.arccos((x-3)/10))*10
    N=len(x)-1
    dx = (x[1] - x[0])

    for n in nlist:
        y2=np.sin(2*np.pi*n*x/13)*np.exp(-x/10)

        y3=y-y2

        y_right = y3[1:] # right endpoints
        y_left = y3[:-1] # left endpoints
        T = (dx/2) * np.sum(y_right + y_left)

        areaslist.append(T)
    return nlist, areaslist


if __name__ == '__main__':
    nlist,areaslist = trape()
    plt.figure(figsize=(12, 6))
    plt.scatter(nlist,areaslist, color='b')
    plt.xlabel('n')
    plt.ylabel('area')
    plt.title('area with trapeziod rule')
    plt.show()
