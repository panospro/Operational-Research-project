#!/usr/bin/env python
# coding: utf-8

# In[133]:


cleaning= [[0,  11,  7, 13,  11],
          [5,   0, 13, 15,  15],
          [13, 15,  0, 23,  11],
          [9,  13,  5,  0  , 3],
          [3,  7,   7,  7,   0]
         ]

mixing=[40,35,45,32,50]
matrix=[]
minTime=100000

for a in range(len(cleaning)):    
   for b in range(len(cleaning)):
       if a!=b:  
           for c in range(len(cleaning)):
               if c!=a and c!=b: 
                   for d in range(len(cleaning)):
                       if d!=a and d!=b and d!=c:
                           for e in range(len(cleaning)):
                               if e!=a and e!=b and e!=c and e!=d:
                                   matrixTemp=[a,b,c,d,e]
                                   minTimeTemp=cleaning[b][a]+cleaning[c][b]+cleaning[d][c]+cleaning[e][d]+cleaning[a][e]
                                   #print(matrixTemp)
                                   #print(minTimeTemp)
                                   if minTimeTemp<=minTime:
                                       minTime=minTimeTemp
                                       matrix=matrixTemp
                                       print(matrix)
                                       print(minTimeTemp)
                                       
minimumOverallTime=minTime+sum(mixing)    
print('The minimum time is',minimumOverallTime,'minutes')



               


# In[89]:


import gurobipy as gp
from gurobipy import GRB
import numpy as np
import math
from gurobipy import quicksum


try:

    n = 5
    cleaning = np.array([  [0,  11,  7, 13,  11],
                           [5,   0, 13, 15,  15],
                           [13, 15,  0, 23,  11],
                           [9,  13,  5,  0  , 3],
                           [3,  7,   7,  7,   0]
                           ])
    
    mixing=[40,35,45,32,50]
        
    # Create a new model
    model = gp.Model("or1")

    # Create variables
    x = model.addMVar((n,n), vtype=GRB.BINARY, name ="x")
    
    
    # Set objective
    model.setObjective(gp.quicksum(cleaning[i][j]*x[i][j]
        for i in range(n) for j in range(n)), GRB.MINIMIZE)
    
    # Add Constraints
  
    # Each value appears once per row
    model.addConstrs((x[i,:].sum() == 1
                     for i in range(n)), name='R')

    # Each value appears once per column
    model.addConstrs((x[:,j].sum() == 1
                     for j in range(n)), name='C')

    # There must be 5 values
    model.addConstrs((x[:,:].sum() == 5
                     for j in range(n)
                     for i in range(n)))
                     
    #In order for the graph to be connected and make a circle
    for i in range(5):
        for j in range(5):
                model.addConstr(x[j,i]+x[i,j] <= 1)
    
    
    # Optimize model
    model.optimize()
    
    #The array that shows the order that should be followed,so we have the minimum time
    array = x.X
    print(array)
    
    #The minimum time of the optimazation
    minTime=model.ObjVal

    #The overall time adding the mixing time 
    minimumOverallTime=minTime+sum(mixing)    
    print('\nThe overall minimum time is',minimumOverallTime,'minutes')

except GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')


# In[134]:


import gurobipy as gp
from gurobipy import GRB
import numpy as np
import math
from gurobipy import quicksum


try:

    n = 3
    M = 1000  #3M-4M
    m = 7
    paintTime = np.array([  [45,  20,  12],
                           [ 0,  10,  17],
                           [10,  34,  28],
                           ])

        
    # Create a new model
    model = gp.Model("or2")

    # Create variables
    beginningTime   = model.addMVar((n,n), name ="beginningTime")
    y               = model.addMVar(shape=m, vtype=GRB.BINARY, name ="y")
    endTime         = model.addVar(1,name ="endTime")
  
    # Set objective
    objective =  [beginningTime[2,0]+paintTime[2,0],beginningTime[2,1]+paintTime[2,1],beginningTime[1,2]+paintTime[1,2]]
    
    model.setObjective(endTime,GRB.MINIMIZE)
 
    # Add Constraints  
    
    # constraints for machine 1
    model.addConstr(beginningTime[0,0]+paintTime[0,0]<=beginningTime[0,1]+(M*(1-y[0])), "c0")
    model.addConstr(beginningTime[0,1]+paintTime[0,1]<=beginningTime[0,0]+(M*y[0]), "c1")    
    model.addConstr(beginningTime[0,0]+paintTime[0,0]<=beginningTime[0,2]+(M*(1-y[1])), "c2")
    model.addConstr(beginningTime[0,2]+paintTime[0,2]<=beginningTime[0,0]+(M*y[1]), "c3")
    model.addConstr(beginningTime[0,1]+paintTime[0,1]<=beginningTime[0,2]+(M*(1-y[2])), "c4")
    model.addConstr(beginningTime[0,2]+paintTime[0,2]<=beginningTime[0,1]+(M*y[2]), "c5")
    
    # constraints for machine 2
    model.addConstr(beginningTime[1,1]+paintTime[1,1]<=beginningTime[1,2]+(M*(1-y[3])), "c6")
    model.addConstr(beginningTime[1,2]+paintTime[1,2]<=beginningTime[1,1]+(M*y[3]), "c7")
    
    # constraints for machine 3
    model.addConstr(beginningTime[2,0]+paintTime[2,0]<=beginningTime[2,1]+(M*(1-y[4])), "c8")
    model.addConstr(beginningTime[2,1]+paintTime[2,1]<=beginningTime[2,0]+(M*y[4]), "c9")
    model.addConstr(beginningTime[2,0]+paintTime[2,0]<=beginningTime[2,2]+(M*(1-y[5])), "c10")
    model.addConstr(beginningTime[2,2]+paintTime[2,2]<=beginningTime[2,0]+(M*y[5]), "c11")
    model.addConstr(beginningTime[2,1]+paintTime[2,1]<=beginningTime[2,2]+(M*(1-y[6])), "c12")
    model.addConstr(beginningTime[2,2]+paintTime[2,2]<=beginningTime[2,1]+(M*y[6]), "c13")
    
    
    # colors in order wallpaper1
    model.addConstr(beginningTime[0,0]+paintTime[0,0]<=beginningTime[2,0], "c14")
    
    # colors in order wallpaper2
    model.addConstr(beginningTime[1,1]+paintTime[1,1]<=beginningTime[0,1], "c15")
    model.addConstr(beginningTime[0,1]+paintTime[0,1]<=beginningTime[2,1], "c16")
    
    # colors in order wallpaper3
    model.addConstr(beginningTime[2,2]+paintTime[2,2]<=beginningTime[0,2], "c17")
    model.addConstr(beginningTime[0,2]+paintTime[0,2]<=beginningTime[1,2], "c18")
        
    
    # finish constr
    model.addConstr(objective[0]<=endTime, "c19")
    model.addConstr(objective[1]<=endTime, "c20")
    model.addConstr(objective[2]<=endTime, "c21")
            
 
    # Optimize model
    model.optimize()
    
    print('\n\nThe time the process begins = \n',beginningTime.X)
    print('\nThe time the process ends = \n',beginningTime.X+paintTime)
    print('\n\nThe varialbes y =',y.X)
    # The minimum time of the optimazation
    minTime=endTime

    # The overall time adding the mixing time 
    minimumOverallTime=minTime  
    print('\nThe overall minimum time is',minimumOverallTime.X,'minutes')

except GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')


# In[ ]:




