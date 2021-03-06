# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:27:50 2019

@author: huber.288
"""


import torch
import torch.nn as nn
from copy import deepcopy
import numpy as np

class Neural_Network2(nn.Module):
    def __init__(self, LayerSizes, Weights):
        super(Neural_Network2, self).__init__()
        # parameters
        # TODO: parameters can be parameterized instead of declaring them here
        self.LayerSizes = LayerSizes
        
        # weights
        if not Weights:
            W=[]
            for i in range(len(LayerSizes)-1):
                W.append(torch.randn(self.LayerSizes[i]+1, self.LayerSizes[i+1])) # 3 X 2 tensor
            self.W=W
        else:
            self.W=Weights
            
    def forward(self, X):
        res=X
        for ind, i in enumerate(self.W):
            res = torch.matmul(torch.cat((torch.FloatTensor([1]),res)), i) # Add offset value
            if ind<len(self.W)-1:
                res = self.Relu(res) # activation function
            #else:
                #res = self.sigmoid(res)
        return res
        
    def sigmoid(self, s):
        return 1 / (1 + torch.exp(-s))
    
    def Relu(self,s):
        return (s+abs(s))/2
    
    def sigmoidPrime(self, s):
        # derivative of sigmoid
        return s * (1 - s)
    
    def backward(self, X, y, o):
        self.o_error = y - o # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o) # derivative of sig to error
        self.z2_error = torch.matmul(self.o_delta, torch.t(self.W2))
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += torch.matmul(torch.t(X), self.z2_delta)
        self.W2 += torch.matmul(torch.t(self.z2), self.o_delta)
        
    def train(self, X, y):
        # forward + backward pass for training
        o = self.forward(X)
        self.backward(X, y, o)
        
    def saveWeights(self, model):
        # we will use the PyTorch internal storage functions
        torch.save(model, "NN")
        # you can reload model with all the weights and so forth with:
        # torch.load("NN")
        
    def predict(self):
        print ("Predicted data based on trained weights: ")
        print ("Input (scaled): \n" + str(xPredicted))
        print ("Output: \n" + str(self.forward(xPredicted)))
        
    def addHiddenNeuron(self,layer):  #Adds randomely initialized hidden neuron to chosen layer (layer 0 is the first hidden layer)
        Wi=self.W[layer]
        Extra=torch.randn(Wi.shape[0],1)
        Wi=torch.cat((Wi,Extra),dim=1)
        self.W[layer]=Wi
        Wo=self.W[layer+1]
        Extra=torch.randn(1,Wo.shape[1])
        Wo=torch.cat((Wo,Extra),dim=0)
        self.W[layer+1]=Wo
        self.LayerSizes[layer+1]=self.LayerSizes[layer+1]+1
        
    def deleteHiddenNeuron(self,layer):
        nn=self.LayerSizes[layer+1]
        r=np.random.randint(0,nn)
        Wi=deepcopy(self.W[layer])
        self.W[layer]=torch.cat((Wi[:,:r],Wi[:,r+1:]),dim=1)
        Wo=deepcopy(self.W[layer+1])
        self.W[layer+1]=torch.cat((Wo[:r,:],Wo[r+1:,:]),dim=0)
        self.LayerSizes[layer+1]=self.LayerSizes[layer+1]-1

