# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:01:38 2019

@author: huber.288
"""
import numpy as np

class Player:
    def __init__(self):
        self.gems=np.array([0,0,0,0,0,0])
        self.bonuses=np.array([0,0,0,0,0])
        self.VPs=0
        self.reserved=[]

    def __repr__(self):
        return 'VPs %s, gems %s, cards %s, reserved %s' % (self.VPs,self.gems,self.bonuses, self.reserved)