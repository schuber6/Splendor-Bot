# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:49:36 2019

@author: huber.288
"""
import copy
import torch
import numpy as np
from NeuralNet2 import *

def NaturalSelection(AllWeights,Ancestors,Scores,NetSize,mutation,step,Nnets):
    #StepSize=.3
    #StepSizeAdd=1
    #StepSizem1=.3
    Padd=.1
    NewAllWeights=[]
    NewAncestors=[]
    Ps=[]
    VeryBest=np.percentile(Scores,3)
    for i in range(9):
        Ps.append(np.percentile(Scores,(i+1)*10))
    if mutation==3:
        StepSize=step
        StepSizeAdd=step
        for ind,i in enumerate(Scores):   #Keep best 10%, make mutant of top 50%, make 2 extra mutants of top 10%
            if i<=Ps[4]:
                NewAllWeights.append(MutateMult_SomeAdd(AllWeights[ind],StepSize,Padd,StepSizeAdd))
                NewAncestors.append(Ancestors[ind])
            if i<=Ps[0]:
                NewAllWeights.append(copy.deepcopy(AllWeights[ind]))
                NewAncestors.append(Ancestors[ind])
            if i<=Ps[0]:
                NewAllWeights.append(MutateMult_SomeAdd(AllWeights[ind],StepSize,Padd,StepSizeAdd))
                NewAllWeights.append(MutateMult_SomeAdd(AllWeights[ind],StepSize,Padd,StepSizeAdd))
                NewAncestors.append(Ancestors[ind])
                NewAncestors.append(Ancestors[ind])
    if mutation==1:
        StepSizem1=step
        for ind,i in enumerate(Scores):   #Keep best 10%, make mutant of top 50%, make 2 extra mutants of top 10%
            if i<=Ps[4]:
                NewAllWeights.append(Mutate(AllWeights[ind],StepSizem1))
                NewAncestors.append(Ancestors[ind])
            if i<=VeryBest:
                NewAllWeights.append(copy.deepcopy(AllWeights[ind]))
                NewAncestors.append(Ancestors[ind])
            if i<=Ps[0]:
                NewAllWeights.append(Mutate(AllWeights[ind],StepSizem1))
                NewAncestors.append(Ancestors[ind])
    for i in range(int(np.floor(Nnets/10))): #Make 10 completely new NNs
        Weights=[]
        NN=Neural_Network2(NetSize,Weights)
        NewAllWeights.append(NN.W)
        NewAncestors.append(max(Ancestors)+1)
    if len(NewAllWeights)>Nnets:
        for i in range(len(NewAllWeights)-Nnets):
            n=int(np.ceil(np.random.rand()*len(NewAllWeights)))-1
            del NewAllWeights[n] #Delete random elements if list grew
            del NewAncestors[n]
    if len(NewAllWeights)<Nnets:
        for i in range(Nnets-len(NewAllWeights)):
            n=int(np.ceil(np.random.rand()*len(NewAllWeights)))-1
            NewAllWeights.append(MutateMult_SomeAdd(NewAllWeights[n],StepSize,Padd,StepSizeAdd)) #Mutate random elements if list shrank
            NewAncestors.append(Ancestors[n])
    return NewAllWeights,Ps,NewAncestors
    
    
def Mutate(Ws,StepSize):   #Add random array with max element abs of StepSize
    Weights=copy.deepcopy(Ws)
    for W in Weights:
        W += torch.randn(list(W.shape)[0], list(W.shape)[1])*StepSize
    return Weights

def MutateMult(Ws,StepSize):   #Multiply by 2 ^ random array with max element abs of StepSize
    Weights=copy.deepcopy(Ws)
    for W in Weights:
        W *= 2**(torch.randn(list(W.shape)[0], list(W.shape)[1])*StepSize)

    return Weights

def MutateMult_SomeAdd(Ws,StepSize,Padd,StepSizeAdd):   #Multiply by 2 ^ random array with max element abs of StepSize
    Weights=copy.deepcopy(Ws)
    for W in Weights:
        W *= 2**(torch.randn(list(W.shape)[0], list(W.shape)[1])*StepSize)
        W += (torch.randn(list(W.shape)[0], list(W.shape)[1])>(1-Padd)).float()*(torch.randn(list(W.shape)[0], list(W.shape)[1])*StepSizeAdd)
    return Weights