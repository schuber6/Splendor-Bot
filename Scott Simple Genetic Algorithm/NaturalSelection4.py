# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:35:18 2019

@author: huber.288
"""


import copy
import torch
import numpy as np
from NeuralNet4 import *
from copy import deepcopy
from helper import *

def NaturalSelection4(AllWeights,Ancestors,Scores,NetSize,mutation,step,Nnets,pAddNeuron):
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
                NewAllWeights.append(CopyWeights(AllWeights[ind]))
                NewAncestors.append(Ancestors[ind])

            if i<=Ps[0]:
                NewAllWeights.append(MutateMult_SomeAdd(AllWeights[ind],StepSize,Padd,StepSizeAdd))
                NewAllWeights.append(MutateMult_SomeAdd(AllWeights[ind],StepSize,Padd,StepSizeAdd))
                NewAncestors.append(Ancestors[ind])
                NewAncestors.append(Ancestors[ind])

    if mutation==1:
        StepSizem1=step
        for ind,i in enumerate(Scores):   #Keep best 3%, make mutant of top 50%, make 1 extra mutants of top 10%
            if i<=Ps[4]:
                NewAllWeights.append(Mutate(AllWeights[ind],StepSizem1,pAddNeuron))
                NewAncestors.append(Ancestors[ind])

            if i<=VeryBest:
                NewAllWeights.append(CopyWeights(AllWeights[ind]))
                NewAncestors.append(Ancestors[ind])

            if i<=Ps[0]:
                NewAllWeights.append(Mutate(AllWeights[ind],StepSizem1,pAddNeuron))
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

    if mutation==3:
        if len(NewAllWeights)<Nnets:
            for i in range(Nnets-len(NewAllWeights)):
                n=int(np.ceil(np.random.rand()*len(NewAllWeights)))-1
                NewAllWeights.append(MutateMult_SomeAdd(NewAllWeights[n],StepSize,Padd,StepSizeAdd)) #Mutate random elements if list shrank
                NewAncestors.append(Ancestors[n])
                NewAllLayers.append(AllLayers[n])    
    if mutation==1:
        if len(NewAllWeights)<Nnets:
            for i in range(Nnets-len(NewAllWeights)):
                n=int(np.ceil(np.random.rand()*len(AllWeights)))-1
                NewAllWeights.append(Mutate(AllWeights[n],StepSizem1,pAddNeuron)) #Mutate random elements if list shrank
                NewAncestors.append(Ancestors[n])

    return NewAllWeights,Ps,NewAncestors
    
    
def Mutate(Ws,StepSize,pAdd):   #Add random array with max element abs of StepSize
    Weights=[]
    for W in Ws:
        W2=W.clone()
        W2 += torch.randn(list(W2.shape)[0], list(W2.shape)[1])*StepSize
        Weights.append(W2)
    r=np.random.rand()
    NL=len(Ws)-1
    if r<pAdd:
        Weights=AddNeuron(Weights,np.random.randint(0,NL))
    if r>1-pAdd:
        Weights=DeleteNeuron(Weights,np.random.randint(0,NL))
        
    return Weights

def MutateMult(Ws,StepSize):   #Multiply by 2 ^ random array with max element abs of StepSize
    Weights=[]
    for W in Ws:
        W2=W.clone()
        W2 *= 2**(torch.randn(list(W2.shape)[0], list(W2.shape)[1])*StepSize)
        Weights.append(W2)

    return Weights

def MutateMult_SomeAdd(Ws,StepSize,Padd,StepSizeAdd):   #Multiply by 2 ^ random array with max element abs of StepSize
    Weights=[]
    for W in Ws:
        W2=W.clone()
        W2 *= 2**(torch.randn(list(W2.shape)[0], list(W2.shape)[1])*StepSize)
        W2 += (torch.randn(list(W2.shape)[0], list(W2.shape)[1])>(1-Padd)).float()*(torch.randn(list(W2.shape)[0], list(W2.shape)[1])*StepSizeAdd)
        Weights.append(W2)
    return Weights

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