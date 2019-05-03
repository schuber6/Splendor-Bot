# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:51:58 2019

@author: huber.288
"""

import sys
sys.path.append('../Game implementation')
sys.path.append('../Convenient Solver Stuff')
from Splendor import *
import numpy as np
from InputVector import *
from MakeMove import *
from NeuralNet4 import *
from NeuralNet2 import Neural_Network2
import torch
import copy
from copy import deepcopy
from NaturalSelection4 import *
import matplotlib.pyplot as plt
from InitializeRandomCards import *
from helper import *

cont=0  # if 1, it will start from previous population, otherwise it'll start from random nets
step=.3  # SD of distribution of random numbers to be added to weights when mutated
if not cont:
    AllWeights=[]
    AllLayers=[]
    AvScores=[]

    Nnets=100  #Number of nets each generation
    Ngames=10  #Number of games to play to determine each net's score
    MaxTurns=13  #Max turns after which testing is stopped
    Ngens=25  #Number of generations to run
    Stall=20  #Number of gens to wait before decreasing step
    Stallp=.3  #Factor to decrease step by when algorithm is stalled
    step=1
    mutation=1  #Type of mutation--1 is simple adding of random numbers (other types don't seem much better)
    Levels=0  #Number of levels deep to search decision space to look for best move
    GameType=0  #Type of Splendor game: 0 is simplest, 1 somewhat more complex
    lastdrop=0
    NetSize=[46,30,26]  #Size of NN layers
    pAddNeuron=0  #Probability to add/subtract neuron during mutation
    Ancestors=list(range(Nnets))

for i3 in range(Ngens):
    Turns=np.zeros((Nnets,Ngames))+MaxTurns+2
    for i0 in range(Nnets):
        if i3==0 and not cont:
            Weights=[]
            pre=Neural_Network2(NetSize,Weights)
            for W in pre.W:
                Weights.append(W.t())
            NN=NeuralNet4(deepcopy(NetSize),Weights)
            AllWeights.append(NN.return_parameters())
            AllLayers.append(deepcopy(NN.LayerSizes))
        else:
            NN=NeuralNet4(WeightSize(AllWeights[i0]),AllWeights[i0])
        for i2 in range(Ngames):
            Game=Splendor(1,GameType)
            for i in range(MaxTurns):
                #IV=InputVector_Simple(Game,46)
                playern=0
                Player=Game.player[0]
                MakeMove(Game,playern,Player,NN,Levels)
                Game.CheckWin()
                if Game.winner:
                    Turns[i0,i2]=i+1# +Game.player[0].VPs/100
                    break
    Scores=np.mean(Turns,axis=1)
    AllWeights,Ps,Ancestors=NaturalSelection4(AllWeights,Ancestors,Scores,NetSize,mutation,step,Nnets,pAddNeuron)
    print([min(Scores),Ps[0],Ps[4]])
    AvScores.append([min(Scores),Ps[0],Ps[4]])
    if i3-lastdrop>Stall:
        if AvScores[-Stall][0]<=AvScores[-1][0] and AvScores[-Stall][1]<=AvScores[-1][1]:  #If fittness has converged, lower step size
            step*=Stallp
            lastdrop=i3
            print(step)
            

plt.plot(AvScores) 
plt.ylabel('Average turns to win')
plt.xlabel('Generation')  
plt.legend(['Best','10th percentile','Median'])

    
    
