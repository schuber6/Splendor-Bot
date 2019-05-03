# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:10:40 2019

@author: huber.288
"""
from copy import deepcopy
from NeuralNet4 import *
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable
from Splendor import Splendor
from MakeMove import *


def WeightSize(Ws):
    DC=Ws
    S=[i.shape[0]-1 for i in DC]
    S.append(DC[-1].shape[1])
    return S

def PlayGames(NN,GameType,Levels,Ngames):
    MaxTurns=15
    #Ngames=10
    Discount=.6
    ChosenMoves=[]
    Outputs=[]
    Rewards=[]
    GN=[]
    Turns=np.zeros(Ngames)+MaxTurns+1
    for i2 in range(Ngames):
        Game=Splendor(1,GameType)
        VPs=[0]
        for i in range(MaxTurns):
            playern=0
            Player=Game.player[0]
            Out,I=MakeMove_Reinforce(Game,playern,Player,NN,Levels)
            Chosen=np.zeros(26)
            Chosen[I]+=1
            Chosen=torch.FloatTensor(Chosen)
            ChosenMoves.append(Chosen)
            Outputs.append(Out)
            VPs.append(float(Game.player[0].VPs))
            GN.append(i2)
            Game.CheckWin()
            if Game.winner:
                Turns[i2]=i+1
                break
        Rs=[]
        for i in range(len(VPs)-1):
            Rs.append(VPs[i+1]-VPs[i])
        for ind1,R1 in enumerate(Rs):
            for ind2,R2 in enumerate(Rs[ind1+1:]):
                Rs[ind1]+=R2*Discount**(ind2+1)
        Rewards.extend(Rs)
        np.array(Rewards)
    return ChosenMoves,Outputs,Rewards,Turns,GN