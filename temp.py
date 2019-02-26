# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:15:45 2019

@author: huber.288
"""

from Splendor import *
import numpy as np
from InputVector import *
from MakeMove import *

Game=Splendor(1)
print(Game)
for i in range(15):
    IV=InputVector_Simple(Game)
    playern=0
    Player=Game.player[0]
    Weights=[]
    MakeMove(Game,playern,Player,Weights)
    Game.CheckWin()
    print(Game)
#print(Game)
#gems=np.array([1,1,0,1,0,0])
#Game.player[0].gems=np.array([5,5,0,0,0,0])
#print(Game)
#Game.ReserveCard(0,0,np.array([-2,1,0,0,0,1]))
#print(Game)
#Game.TakeGems(0,np.array([1,1,1,0,0,0]))
#print(Game)