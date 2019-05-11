# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:55:06 2019

@author: Scott
"""

from MakeMove_Full import MakeMove_TreeSearch, MakeMove_GMove, ExchangeGems
import numpy as np

def NN(_):
    Out=np.random.rand(26+8)   #Replace NN output with random vector
    return Out

class TreeSearchBot():
    def __init__(self,max_depth):
        '''max_depth sets the number of turns in the future for it to search (min 1)'''
        self.max_depth=max_depth
        self.depth=max_depth-1
        self.TopMoves=np.inf  #Can set a finite limit to number of moves searched per layer
    def MakeMove(self,Game,playern):
        BestScore,BestMove,BestTurnsToWin = MakeMove_TreeSearch(Game,playern,NN,self.depth,self.TopMoves)
        if not BestMove:
            values = np.random.rand(6)
            gems=ExchangeGems(Game,playern,values)['Gems']
            Game.TakeGems(playern,gems)
        else:
            MakeMove_GMove(Game,playern,BestMove)
        self.depth -= 1  # if the depth is contstant, it will keep making long term plans each turn and never executing them
        self.depth = self.depth % self.max_depth