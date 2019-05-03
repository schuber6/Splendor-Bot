# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:29:39 2019

@author: huber.288
"""

from SplendorCard import *
import pickle

Card=[]
Card.append(SplendorCard(0,15,[1,1,1,0,0]))
Card.append(SplendorCard(1,3,[1,1,0,1,0]))
Card.append(SplendorCard(2,2,[1,0,1,0,1]))
Card.append(SplendorCard(3,1,[0,1,1,1,0]))

filename = 'Cards'
outfile = open(filename,'wb')
pickle.dump(Card,outfile)
outfile.close()