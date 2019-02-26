# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:24:04 2019

@author: huber.288
"""
import numpy as np

class SplendorCard:
    def __init__(self,Bonus,VPs,Cost):
        self.bonus=Bonus
        self.VPs=VPs
        self.cost=np.array(Cost)
        
    def __repr__(self):
        return 'VPs %s, Bonus %s, cost %s' % (self.bonus,self.VPs,self.cost)