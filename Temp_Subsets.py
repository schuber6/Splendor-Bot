# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:50:45 2019

@author: huber.288
"""

from itertools import combinations, chain
import numpy as np
allsubsets = lambda n: list(chain(*[combinations(range(n), ni) for ni in range(n+1)]))
A=allsubsets(5)
Gs=[]
for sub in A:
    if len(sub)==3:
        Gs.append(sub)
for i in range(5):
    Gs.append((i,i))
print(Gs)
Gs1=Gs
Gs=[]
for i in Gs1:
    A=[0,0,0,0,0,0]
    for i2 in list(i):
        A[i2]+=1
    Gs.append(np.array(A))
print(Gs)
import pickle

pickle.dump( Gs, open( "GemCombos.p", "wb" ) )
#Gs=pickle.load(open( "GemCombos.p", "rb" ))
#import numpy as np
MType=np.concatenate((np.zeros(4)+2,np.zeros(15)+1))
pickle.dump( MType, open( "MoveType.p", "wb" ) )