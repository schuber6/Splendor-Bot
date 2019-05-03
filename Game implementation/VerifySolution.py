# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:08:54 2019

@author: huber.288
"""

import pickle
import numpy as np
from Splendor import *
from NeuralNet4 import *
NetSize=[46,30,26]
Levels=0
GameType=0

filename = 'SolvedGT0'
infile = open(filename,'rb')
BestW = pickle.load(infile)
infile.close()
NN=NeuralNet4(NetSize,[])
NN.set_parameters(BestW)
TT=ThoroughCheck(NN,GameType,Levels)
print(np.max(TT))