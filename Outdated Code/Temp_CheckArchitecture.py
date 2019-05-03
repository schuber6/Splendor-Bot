# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:45:31 2019

@author: huber.288
"""
from NeuralNet2 import *
from NeuralNet4 import *
import numpy as np

W=AllWeights[1]
NN=Neural_Network2(NetSize,W)
S2=ThoroughCheck(NN,0,-1)
print(S2)
print(np.mean(S2))
Weights=[]
for i in W:
    Weights.append(i.t())
NN2=NeuralNet4(NetSize,Weights)
S4=ThoroughCheck(NN2,0,-1)
print(S4)
print(np.mean(S4))
W4=NN2.linear1.weight
W2=W[0]
print(NN(IV))
print(NN2(IV))
_,GMove=MakeMove_TreeSearch(Game,0,Game.player[0],NN,-1)
print(GMove)
_,GMove=MakeMove_TreeSearch(Game,0,Game.player[0],NN2,-1)
print(GMove)