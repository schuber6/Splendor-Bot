# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:33:52 2019

@author: huber.288
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:38:51 2019

@author: huber.288
"""

import sys
sys.path.append('../Game implementation')
sys.path.append('../Convenient Solver Stuff')
from NeuralNet4 import *
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable
from Splendor import *
from MakeMove import *
from helper import *

NetSize=[46,35,35,26]
Steps=30
Ngames=10
Record=1
GameType=0
Levels=1
loss_fn = torch.nn.MSELoss()
BestT=4
BestWs=[]
for i00 in range(100):
    NN=NeuralNet4(deepcopy(NetSize),[])
    optim = torch.optim.Adam(NN.parameters(),lr=.0001)
    Turns=[]
    for i0 in range(Steps):
        ChosenMoves,Outputs,Rewards,Ts,GN=PlayGames(NN,GameType,Levels,Ngames)   #TODO
        if i0 % Record==0:
            Turns.append(np.mean(Ts))
            if np.mean(Ts)<=BestT:
                TT=ThoroughCheck(NN,GameType,Levels)
                if np.mean(TT)<BestT:
                    BestT=np.mean(TT)
                    print(BestT)
                    BestWs=NN.return_parameters()
            if BestT==2:
                break
            NormRewards=(Rewards-np.mean(Rewards))/np.std(Rewards)
            GoodGs=Ts==np.min(Ts)
            GoodMs=GoodGs[GN]
            NormRewards[GoodMs]=1  #Set Reward for all fastest games to be +1
            for ind,Move in enumerate(ChosenMoves):
                optim.zero_grad()
                loss = loss_fn(Outputs[ind], Move)
                loss.backward()
                A=NN.parameters()
                for p in A:
                    p.grad.data*=NormRewards[ind]
                optim.step()
    plt.plot(Turns)
    plt.show()
        
