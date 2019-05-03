# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:27:04 2019

@author: huber.288
"""

import copy
import torch
import numpy as np
from NeuralNet4 import *
from copy import deepcopy
from helper import *
from Reinforce import Reinforce

def ReinforcementSelection(AllWeights,Ancestors,Scores,NetSize,step,Nnets,pAddNeuron,GameType,Levels):
    #StepSize=.3
    #StepSizeAdd=1
    #StepSizem1=.3
    Padd=.1
    NewAllWeights=[]
    NewAncestors=[]
    Ps=[]
    mutation=1
    VeryBest=np.percentile(Scores,3)
    for i in range(9):
        Ps.append(np.percentile(Scores,(i+1)*10))
    if mutation==1:
        StepSizem1=step
        for ind,i in enumerate(Scores):   #Keep best 3%, make mutant of top 50%, make 1 extra mutants of top 10%
            if i<=Ps[4]:
                NewAllWeights.append(Mutate(AllWeights[ind],StepSizem1,pAddNeuron,NetSize,GameType,Levels))
                NewAncestors.append(Ancestors[ind])

            if i<=VeryBest:
                NewAllWeights.append(CopyWeights(AllWeights[ind]))
                NewAncestors.append(Ancestors[ind])

            if i<=Ps[0]:
                NewAllWeights.append(Mutate(AllWeights[ind],StepSizem1,pAddNeuron,NetSize,GameType,Levels))
                NewAncestors.append(Ancestors[ind])

    for i in range(int(np.floor(Nnets/10))): #Make 10 completely new NNs
        Weights=[]
        NN=NeuralNet4(deepcopy(NetSize),Weights)
        NewAllWeights.append(NN.return_parameters())
        NewAncestors.append(max(Ancestors)+1)

    if len(NewAllWeights)>Nnets:
        for i in range(len(NewAllWeights)-Nnets):
            n=int(np.ceil(np.random.rand()*len(NewAllWeights)))-1
            del NewAllWeights[n] #Delete random elements if list grew
            del NewAncestors[n]
   
    if mutation==1:
        if len(NewAllWeights)<Nnets:
            for i in range(Nnets-len(NewAllWeights)):
                n=int(np.ceil(np.random.rand()*len(AllWeights)))-1
                NewAllWeights.append(Mutate(AllWeights[n],StepSizem1,pAddNeuron,NetSize,GameType,Levels)) #Mutate random elements if list shrank
                NewAncestors.append(Ancestors[n])

    return NewAllWeights,Ps,NewAncestors
    
    
def Mutate(Ws,StepSize,pReinforce,NetSize,GameType,Levels):   #Add random array with max element abs of StepSize
    Weights=[]
    for W in Ws:
        W2=W.clone()
        W2 += torch.randn(list(W2.shape)[0], list(W2.shape)[1])*StepSize
        Weights.append(W2)

    
    r=np.random.rand()
    if r<pReinforce:
        NN=NeuralNet4(NetSize,Weights)
        NN=Reinforce(NN,GameType,Levels,20)
        Weights2=NN.return_parameters()
    else:
        Weights2=Weights
    return Weights2


def AddNeuron(Ws,layer):
    Wi=Ws[layer].clone()
    Extra=torch.randn(Wi.shape[0],1)
    Wi=torch.cat((Wi,Extra),dim=1)
    Wo=Ws[layer+1].clone()
    Extra=torch.randn(1,Wo.shape[1])
    Wo=torch.cat((Wo,Extra),dim=0)
    NW=deepcopy(Ws)
    NW[layer]=Wi
    NW[layer+1]=Wo
    return NW

def DeleteNeuron(Ws,layer):
    NW=CopyWeights(Ws)
    LS=WeightSize(Ws)
    nn=LS[layer+1]
    r=np.random.randint(0,nn)
    Wi=deepcopy(Ws[layer])
    NW[layer]=torch.cat((Wi[:,:r],Wi[:,r+1:]),dim=1)
    Wo=deepcopy(Ws[layer+1])
    NW[layer+1]=torch.cat((Wo[:r,:],Wo[r+1:,:]),dim=0)
    return NW

def CopyWeights(Ws):
    Weights=[]
    for W in Ws:
        Weights.append(W.clone())
    return Weights