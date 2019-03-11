# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:09:01 2019

@author: huber.288
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:29:39 2019

@author: huber.288
"""

from SplendorCard import *
import pickle
import numpy as np
Gs=pickle.load(open( "GemCombos.p", "rb" ))

def MakeCards():
    Card=[]
    C=np.random.choice(len(Gs))
    Card.append(SplendorCard(0,15,Gs[C][0:5]))
    C=np.random.choice(len(Gs))
    Card.append(SplendorCard(1,3,Gs[C][0:5]))
    C=np.random.choice(len(Gs))
    Card.append(SplendorCard(2,2,Gs[C][0:5]))
    C=np.random.choice(len(Gs))
    Card.append(SplendorCard(3,1,Gs[C][0:5]))
    return Card

