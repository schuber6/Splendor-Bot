# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:09:38 2019

@author: huber.288
"""

import torch
import torch.nn as nn
from copy import deepcopy
import numpy as np
from torch.nn.parameter import Parameter

class NeuralNet3(nn.Module):
    def __init__(self,LayerSizes,Weights):
        super(NeuralNet3, self).__init__()
        self.linear=[]
        self.relu=nn.ReLU()
        self.sig=nn.Sigmoid()
        for ind in range(len(LayerSizes)-1):
            self.linear.append(nn.Linear(in_features=LayerSizes[ind], out_features=LayerSizes[ind+1], bias=True))
        if Weights:
            set_parameters(Weights)   
    
    def forward(self, inp_batch):
        res=deepcopy(inp_batch)
        for ind in range(len(self.linear)):
            res=self.linear[ind](res)
            if ind==len(self.linear):
                res=self.sig(res)
            else:
                res=self.relu(res)
        return res
    
    def return_parameters(self):
        Ws=[]
        for ind in range(len(self.linear)):
            W=self.linear[ind].weight
            B=self.linear[ind].bias
            Ws.append(torch.cat((B[:,None],W),dim=1))
        return Ws
    
    def set_parameters(self,Ws):
        for ind,W in enumerate(Ws):
            self.linear[ind].bias=Parameter(W[:,0])
            self.linear[ind].weight=Parameter(W[:,1:])
