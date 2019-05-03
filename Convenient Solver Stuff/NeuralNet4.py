# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:46:51 2019

@author: huber.288
"""

import torch
import torch.nn as nn
from copy import deepcopy
import numpy as np
from torch.nn.parameter import Parameter

class NeuralNet4(nn.Module):
    def __init__(self,LayerSizes,Weights):
        super(NeuralNet4, self).__init__()
        self.LayerSizes=LayerSizes
        self.linear1=nn.Linear(in_features=LayerSizes[0], out_features=LayerSizes[1], bias=True)
        self.relu=nn.ReLU()
        self.linear2=nn.Linear(in_features=LayerSizes[1], out_features=LayerSizes[2], bias=True)
        self.sig=nn.Sigmoid()
        if len(LayerSizes)>3:
            self.linear3=nn.Linear(in_features=LayerSizes[2], out_features=LayerSizes[3], bias=True)
        self.softmax=nn.Softmax(dim=0)
        if Weights:
            self.set_parameters(Weights)   
    
    def forward(self, inp_batch):
        res=deepcopy(inp_batch)
        res=self.linear1(res)
        res=self.relu(res)
        res=self.linear2(res)
        if len(self.LayerSizes)>3:
            res=self.relu(res)
            res=self.linear3(res)
        res=self.softmax(res)
        return res
    
    def return_parameters(self):
        Ws=[]
        W=self.linear1.weight
        B=self.linear1.bias
        Ws.append(torch.cat((B[:,None],W),dim=1))
        W=self.linear2.weight
        B=self.linear2.bias
        Ws.append(torch.cat((B[:,None],W),dim=1))
        if len(self.LayerSizes)>3:
            W=self.linear3.weight
            B=self.linear3.bias
            Ws.append(torch.cat((B[:,None],W),dim=1))
        return Ws
    
    def set_parameters(self,Ws):
        W=Ws[0]
        self.linear1.bias=Parameter(W[:,0])
        self.linear1.weight=Parameter(W[:,1:])
        W=Ws[1]
        self.linear2.bias=Parameter(W[:,0])
        self.linear2.weight=Parameter(W[:,1:])
        if len(self.LayerSizes)>3:
            W=Ws[2]
            self.linear2.bias=Parameter(W[:,0])
            self.linear2.weight=Parameter(W[:,1:])
