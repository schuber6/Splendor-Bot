# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:54:29 2019

@author: Scott
"""

from MakeMove_Full import MakeMove_TreeSearch, MakeMove_GMove, ExchangeGems
import numpy as np
from TreeSearchBot import TreeSearchBot

def NN(_):
    Out=np.random.rand(26+8)   #Replace NN output with random vector
    return Out

N=20
nturn=np.zeros(N) + 100
playern=0
Levels=4
TopMoves=np.inf
TSB = TreeSearchBot(Levels)
for g in range(N):
    Game = Splendor_Full(1)
    for n in range(100):
        TSB.MakeMove(Game,0)
# =============================================================================
#         BestScore,BestMove,BestTurnsToWin = MakeMove_TreeSearch(Game,playern,NN,Levels-(n%(Levels+1)),TopMoves)
#         if not BestMove:
#             values = np.random.rand(6)
#             gems=ExchangeGems(Game,playern,values)['Gems']
#             Game.TakeGems(playern,gems)
#         else:
#             MakeMove_GMove(Game,playern,BestMove)
# =============================================================================
        Game.CheckWin()
        if Game.winner:
            nturn[g] = n+1
            break
print(np.mean(nturn))
print(np.std(nturn))