# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:27:50 2019

@author: huber.288
"""


import torch
import torch.nn as nn

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
            if ind<len(self.W):
                res = self.Relu(res) # activation function
            else:
                res = self.sigmoid(res)
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


