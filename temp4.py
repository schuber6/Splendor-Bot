# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:27:54 2019

@author: huber.288
"""
from Splendor import *
import numpy as np
from NeuralNet2 import *

used=Scores==2
BestWeights=[i for ind,i in enumerate(AllWeights) if used[ind]]
NetSize=[46,30,26]
ss=np.zeros([len(BestWeights),100])
GameType=1
Levels=1
for ind,weights in enumerate(BestWeights):
    NN=Neural_Network2(NetSize,weights)
    ss[ind,:]=ThoroughCheck(NN,GameType,Levels)

