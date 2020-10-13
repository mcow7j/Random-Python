import numpy as np

def ARM_simulation(timesteps=100,num_of_pairs_workers=3,conv_length=3,prob=[0.2,0.4,0.2,0.2]):
  """The following assuumptions have be made when simulating the arm conveyor problem:
      -conveyor and workers hands are empty at start
      -one of a pair of workers is dominate and always makes all his decisions first
      -if a worker doesn't have a component in his hands he will pick a item up
      or if he does he will try to make a product if possible.
    inputs:
      timesteps(int)- period of time conveyor is on for
      num_of_pairs_workers (int)- number of pairs of workers
      conv_length (int)- length of conveyor (generally assumed to be same as
      number of pairs of workers)
      prob (array)- probabilty distubtion for components entering the conveyor
    outputs:
      num_P (int)- number of products P produced by production line in simulation
      num_Q (int)- number of products Q produced by production line in simulation
      num_untouched (int)- number of components untouched by production line in simulation
       """
  #set up conveyor and workers
  conveyor= []
  workers=[]
  #set up workers assume they having nothing 'N'
  for i in range(num_of_pairs_workers):
    workers.append(['N','N'])

  #set up conveyor assume it is empty at the start
  for i in range(conv_length):
    conveyor.append('N')


  #alternative for full conveyer belt at the start is given below
  #conveyer=np.random.choice(['N','A','B','C'],size=conv_length, replace=True, prob)

  # the following dictionary is used to countdown how long a product takes to assesmble
  time_dic = {"Q3":"Q2", "Q2":"Q1","Q1":"Q", "P3":"P2","P2":"P1","P1":"P" }


  for t in range(timesteps):
    #insert new item into start of conveyor belt
    conveyor.insert(0,np.random.choice(['N','A','B','C'], p=prob))

    #update assemble time of all workers making products
    for j in range(num_of_pairs_workers):
      workers[j] = [time_dic.get(n, n) for n in workers[j]]

    #iterate through the conveyor and so the workers next to them
    for j in range(num_of_pairs_workers):
      item = conveyor[j]
      #check if there is space on conveyor
      if item == 'N':
        for i in range(2):
          k = workers[j][i]
          #check if a worker has a finished product
          if k =='Q' or k =='P':
            conveyor[j] = k
            workers[j][i] ='N'
            break
      else:
        #assume 1 worker in the pair is dominant, so always makes all his decisions first
        for i in range(2):
          combin = {workers[j][i],item}

          #check if worker doesn't have a component, if he doesn't he picks up component
          if workers[j][i] == 'N':
            workers[j][i] = item
            conveyor[j] = 'N'
            break
          #check to see if item on the conveyor and in workers hand can make product Q
          elif  combin == {'A','B'}:
            workers[j][i] = 'Q3'
            conveyor[j] = 'N'
            break
          #check to see if item on the conveyor and in workers hand can make product P
          elif combin == {'A','C'}:
            workers[j][i] = 'P3'
            conveyor[j] = 'N'
            break

  #remove item currently on the converyor
  del conveyor[0:conv_length]

  #count up the relevent number of items in the post production line
  num_P = conveyor.count('P')
  num_Q = conveyor.count('Q')
  num_N = conveyor.count('N')
  num_untouched = timesteps-num_P-num_Q-num_N

  return num_P, num_Q, num_untouched



if __name__=='__main__':
    P,Q,I = ARM_simulation()
    print( 'number of P produced = ', P)
    print( 'number of Q produced  = ', Q)
    print( 'number of components untouched  = ', I)
