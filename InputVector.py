# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:56:33 2019

@author: huber.288
"""

import numpy as np
from Splendor import *
from SplendorCard import *
from Player import *

def InputVector_Simple(Game):
    IVlist=[]
    IVlist.extend(Game.gems)
    IVlist.extend(Game.player[0].gems)
    IVlist.extend(Game.player[0].bonuses)
    IVlist.append(Game.player[0].VPs)
    for card in Game.cards:
        IVlist.extend(card.cost)
        IVlist.append(card.bonus)
        IVlist.append(card.VPs)
    IV=np.array(IVlist)
    return IV