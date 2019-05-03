# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:08:43 2019

@author: huber.288
"""

from Splendor_Full import *
import numpy as np
from InputVector import *
from MakeMove_Full import *
from NeuralNet2 import *
import torch
import copy
from NaturalSelection import *
import matplotlib.pyplot as plt

#Game=Splendor_Full(1)
#print(Game)
#playern=0
#Player=Game.player[playern]
#NN=[]
#Levels=-1
#for i in range(30):
#    MakeMove(Game,playern,Player,NN,Levels)
#print(Game)
NN=Neural_Network2(NetSize,AllWeights[0])
NN.addHiddenNeuron(0)
print(NN.W[0].shape)
print(NN.W[1].shape)