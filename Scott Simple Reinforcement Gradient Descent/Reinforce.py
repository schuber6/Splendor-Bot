# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:38:51 2019

@author: huber.288
"""
from NeuralNet4 import *
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable
from Splendor import Splendor
from MakeMove import *
from helper import *


def Reinforce(NN,GameType,Levels,Steps):
    '''Takes NN and gradient descends it towards best score'''
    Ngames=10
    loss_fn = torch.nn.MSELoss()
    optim = torch.optim.Adam(NN.parameters(),lr=.0001)
    Turns=[]
    for i0 in range(Steps):
        ChosenMoves,Outputs,Rewards,Ts,GN=PlayGames(NN,GameType,Levels,Ngames)   #TODO
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
    return NN
        
