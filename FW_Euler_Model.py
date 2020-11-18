"""Basic Explicit Euler Forward Method to solve 2nd order ode (see read me for equation). FwEuler uses func1 to calculate function term."""

import numpy as np
import matplotlib.pyplot as plt


def func1(x,u):
  """ function part of euler method used in FW Euler"""
  return 5*x*u+(x+7)*np.sin(x)


def FwEuler(u0=5,y0=8,h=0.02):
    """ Function to solve 2nd order ode using Explicit Euler Forward Method.
        Input:
        u0: initial condition of u=y'
        y0: initial condition of y
        h = nodal times
        Output:
        x: time array over 15 (Nx1)
        y: position array (Nx1)"""
    x = np.arange(0,15+h,h)
    # determine the number of time steps
    N = len(x)
    # allocate output array
    u = np.ndarray(N)
    y = np.ndarray(N)
    # initialise the solution
    u[0] = u0
    y[0] = y0
    # compute the solution incrementally at subsequent time steps
    for n in range(1,N):
        u[n] = u[n-1] - func1(x[n-1],u[n-1]) * h
        y[n] = y[n-1]+u[n-1]*h

    return y,x

if __name__ == '__main__':
  y,x=FwEuler()
  plt.figure(figsize=(12, 6))
  plt.scatter(x,y, color='b')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('ODE simulation')
  plt.show()
