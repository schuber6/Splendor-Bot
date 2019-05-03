# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:39:56 2019

@author: huber.288
"""

from SplendorCard import *
import pickle

Noble=[]
Noble.append(SplendorCard(0,3,[0,0,4,4,0]))
Noble.append(SplendorCard(0,3,[3,0,0,3,3]))
Noble.append(SplendorCard(0,3,[4,4,0,0,0]))
Noble.append(SplendorCard(0,3,[4,0,0,0,4]))
Noble.append(SplendorCard(0,3,[0,4,4,0,0]))
Noble.append(SplendorCard(0,3,[0,3,3,3,0]))
Noble.append(SplendorCard(0,3,[3,3,3,0,0]))
Noble.append(SplendorCard(0,3,[0,0,0,4,4]))
Noble.append(SplendorCard(0,3,[3,3,0,0,3]))
Noble.append(SplendorCard(0,3,[0,0,3,3,3]))


filename = 'Nobles'
outfile = open(filename,'wb')
pickle.dump(Noble,outfile)
outfile.close()