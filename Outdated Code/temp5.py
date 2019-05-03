# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:42:53 2019

@author: huber.288
"""

from Splendor import *
import numpy as np
from InputVector import *
import torch
from NeuralNet2 import *
from copy import deepcopy

NetSize=[46,30,26]
NN=Neural_Network2(deepcopy(NetSize),deepcopy(AllWeights[2]))
print(NN.LayerSizes)
print(np.mean(ThoroughCheck(NN,1,1)))
for i in range(10):
    NN.deleteHiddenNeuron(0)
print(np.mean(ThoroughCheck(NN,1,1)))
print(NN.LayerSizes)
print(NetSize)
print(NN.W[0])



