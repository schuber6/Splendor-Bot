# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:03:12 2019

@author: Scott
"""

import sys
sys.path.append('../Game implementation')
sys.path.append('../Convenient Solver Stuff')
from Splendor_Full import *
import numpy as np
import unittest
from MakeMove_Full import ExchangeGems


class ExchangeTest(unittest.TestCase):
    def setup(self):
        np.random.seed(1234)
        self.Game = Splendor_Full(1)
        gems = np.array([1,1,1,0,0,0])
        for _ in range(3):
            self.Game.TakeGems(0,gems)
    def test_SimpleExchange(self):
        self.setup()
        values = np.array([1,1,0,0,0,0])
        answer = [1,1,-1,0,0,0]
        playern = 0
        self.assertEqual(list(ExchangeGems(self.Game,playern,values)['Gems']),answer)
        self.assertEqual(ExchangeGems(self.Game,playern,values)['Value'],8)
    def test_SimpleExchange2(self):
        self.setup()
        values = np.array([1,1,0,1,0,0])
        answer = [1,1,-2,1,0,0]
        playern = 0
        self.assertEqual(list(ExchangeGems(self.Game,playern,values)['Gems']),answer)
        self.assertEqual(ExchangeGems(self.Game,playern,values)['Value'],9)
    def test_SimpleExchange3(self):
        self.setup()
        values = np.array([0,0,0,1,0,0])
        answer = [-1,0,0,2,0,0]
        playern = 0
        self.assertEqual(list(ExchangeGems(self.Game,playern,values)['Gems']),answer)
        self.assertEqual(ExchangeGems(self.Game,playern,values)['Value'],2)
    def test_SimpleExchange4(self):
        self.setup()
        self.Game.gems = np.array([0,0,0,1,1,1])
        values = np.array([0,1,1,1,1,0])
        answer = [-1,0,0,1,1,0]
        playern = 0
        self.assertEqual(list(ExchangeGems(self.Game,playern,values)['Gems']),answer)
        self.assertEqual(ExchangeGems(self.Game,playern,values)['Value'],8)