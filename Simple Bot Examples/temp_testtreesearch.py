# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:03:43 2019

@author: Scott
"""

from MakeMove_Full import MakeMove_TreeSearch, MakeMove_GMove, ExchangeGems
from Splendor_Full import Splendor_Full
from RandomMovesBot import RandomMovesBot
import numpy as np



def NN(_):
    Out=np.random.rand(26+8)   #Replace NN output with random vector
    return Out

np.random.seed(623)
Game = Splendor_Full(1)
playern=0
Levels=0
TopMoves=np.inf
for _ in range(20):
    RandomMovesBot(Game,0)
print(Game)
#RandomMovesBot(Game,0)
#print('\n')
#print(Game)
np.random.seed()
for i in range(1):
    score,move,turns=MakeMove_TreeSearch(Game,playern,NN,Levels-i,TopMoves)
    if not BestMove:
        values = np.random.rand(6)
        gems=ExchangeGems(Game,playern,values)['Gems']
        Game.TakeGems(playern,gems)
    else:
        MakeMove_GMove(Game,playern,move)
    print('\n')
    print(Game)
