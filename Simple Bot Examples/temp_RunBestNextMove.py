# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:51:52 2019

@author: Scott
"""

from MakeMove_Full import MakeMove_TreeSearch, MakeMove_GMove, ExchangeGems
import numpy as np

def NN(_):
    Out=np.random.rand(26+8)   #Replace NN output with random vector
    return Out

N=20
nturn=np.zeros(N) + 100
playern=0
Levels=1
TopMoves=np.inf
for g in range(N):
    Game = Splendor_Full(1)
    for n in range(100):
        BestScore,BestMove,BestTurnsToWin = MakeMove_TreeSearch(Game,playern,NN,Levels,TopMoves)
        if not BestMove:
            values = np.random.rand(6)
            gems=ExchangeGems(Game,playern,values)['Gems']
            Game.TakeGems(playern,gems)
        else:
            MakeMove_GMove(Game,playern,BestMove)
        #RandomMovesBot(Game,0)
        Game.CheckWin()
        if Game.winner:
            nturn[g] = n+1
            break
print(np.mean(nturn))
print(np.std(nturn))