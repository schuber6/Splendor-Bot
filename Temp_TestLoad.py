# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:08:07 2019

@author: huber.288
"""

import pickle
filename = 'Cards_Full'
filename2 = 'Nobles'
infile = open(filename,'rb')
cards1,cards2,cards3 = pickle.load(infile)
