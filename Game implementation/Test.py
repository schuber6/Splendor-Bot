# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:19:23 2019

@author: huber.288
"""

from Splendor import Splendor
import numpy as np
np.random.seed(236)
Game = Splendor(1,0)
print(Game)
playern = 0
cardn = 0
gems = np.array([0,0,0,0,0,1])
print(Game.CheckReserve(playern,cardn,gems))
Game.ReserveCard(playern,cardn,gems)
print(Game)