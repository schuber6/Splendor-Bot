# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:58:10 2019

@author: Scott
"""

import sys
sys.path.append('../Game implementation')
sys.path.append('../Convenient Solver Stuff')
from MakeMove_Full import MakeMove
from RandomMovesBot import RandomMovesBot
from Splendor_Full import Splendor_Full
import numpy as np

N=100
nturn = np.zeros(N)
for gs in range(N):
    Game = Splendor_Full(1)
    for n in range(100):
        #MakeMove(Game,0,Game.player[0],[],0)
        RandomMovesBot(Game,0)
        Game.CheckWin()
        if Game.winner:
            nturn[gs] = n+1
            break
print(np.mean(nturn))
print(np.std(nturn))
    