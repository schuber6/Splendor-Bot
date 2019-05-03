# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:07:56 2019

@author: huber.288
"""

import pickle


filename = 'Score291GT1'
outfile = open(filename,'wb')
pickle.dump(BestW,outfile)
outfile.close()