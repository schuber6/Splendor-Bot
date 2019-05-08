# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:13:51 2019

@author: Scott
"""

from MakeMove_Full import MakeMove
import numpy as np

def NN(_):
    Out=np.random.rand(26+8)   #Replace NN output with random vector
    return Out

def RandomMovesBot(Game,playern):
    '''Makes one random move on Game as player number "playern"'''
    Levels = 0
    MakeMove(Game,playern,NN,Levels)