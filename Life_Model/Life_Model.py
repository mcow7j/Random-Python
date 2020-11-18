""" Life Model Predictors """

#import relevant packages and mount data from google drive
import numpy as np
import pandas as pd
from scipy.optimize import minimize


data=pd.read_csv('Estqx2020.csv')

#define data of a,b and d using numpy arrays
a=np.asarray(data['a'])
b=np.asarray(data['b'])
d=np.asarray(data['d'])

#define likihood functions for various assumprions

def likihood_uniform(q):
  #create qhat_i
  w=(b-a)*q/(1-a*q)
  #store in array (qhat_i^d_i)
  w1=np.power(w,d)
  #store in array (1-qhat_i^(1-d_i))
  w2=np.power(1-w,1-d)
  #times out all values in array, like timesing out product
  L=np.prod(w1)*np.prod(w2)
  return L

def likihood_balducci(q):
  #create qhat_i
  w=(b-a)*q/(1-(1-b)*q)
  #store in array (qhat_i^d_i)
  w1=np.power(w,d)
  #store in array (1-qhat_i^(1-d_i))
  w2=np.power(1-w,1-d)
  #times out all values in array, like timesing out product
  L=np.prod(w1)*np.prod(w2)
  return L

#define likihood functioin
def likihood_constant_mort(q):
  n=len(a)
  ones=np.ones(n)
  q_minus_1=ones-q
  #create qhat_i
  w=(np.power(q_minus_1,a)-np.power(q_minus_1,b))/np.power(q_minus_1,a)
  #store in array (qhat_i^d_i)
  w1=np.power(w,d)
  #store in array (1-qhat_i^(1-d_i))
  w2=np.power(1-w,1-d)
  #times out all values in array, like timesing out product
  L=np.prod(w1)*np.prod(w2)
  return L



#set up bounds
bnds = (0,1)



if __name__=='__main__':
    q_uni = minimize(lambda q: -likihood_uniform(q) ,0.5, method='Nelder-Mead', bounds=bnds )
    q_bald = minimize(lambda q: -likihood_balducci(q),0.5, method='Nelder-Mead', bounds=bnds )
    q_mort = minimize(lambda q: -likihood_constant_mort(q),0.5, method='Nelder-Mead', bounds=bnds )
    print("best q for uniform=",q_uni.x)
    print("best q for Balducci=",q_bald.x)
    print("best q for constant for of mortality=",q_mort.x)
