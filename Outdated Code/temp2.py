# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:41:13 2019

@author: huber.288
"""

from Splendor_Full import *
from Splendor import *
import numpy as np

Game=Splendor_Full(1)
Game.TakeGems(0,np.array([0,0,0,0, 2, 0]))
Game.TakeGems(0,np.array([0,0,1,1, 1, 0]))
Game.TakeGems(0,np.array([0,0,1,1, 1, 0]))
Game.BuyCard(0,0,0,np.array([0,0,0,0,4,0]))
print(Game)
