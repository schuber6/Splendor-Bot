# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:42:53 2019

@author: huber.288
"""

from Splendor import *
import numpy as np
from InputVector import *
import torch

Game=Splendor(1,1)
IV=InputVector_Simple(Game,46)
IV=torch.FloatTensor(IV)
IV=torch.cat((torch.FloatTensor([1]),IV))

