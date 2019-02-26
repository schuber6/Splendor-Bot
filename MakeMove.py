# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:29:54 2019

@author: huber.288
"""
from InputVector import *
import numpy as np
import pickle
Gs=pickle.load(open( "GemCombos.p", "rb" ))
MType=pickle.load(open( "MoveType.p", "rb" ))

def MakeMove(Game,playern,Player,Weights):
    IV=InputVector_Simple(Game)
    Out=np.random.rand(26)#np.zeros(26)#NeuralNet(IV,Weights)
    GMoves=RankMoves(Out,Game,Player,playern)
    if not GMoves:
        print('No possible moves')
        return Game
    if GMoves[0][0]==1:
        Game.TakeGems(playern,GMoves[0][2])
        return Game
    if GMoves[0][0]==2:
        Game.BuyCard(playern,GMoves[0][1],GMoves[0][2])
        return Game
    if GMoves[0][0]==3:
        Game.ReserveCard(playern,GMoves[0][1],GMoves[0][2])
        return Game
    pass
    
def RankMoves(Out,Game,Player,playern): #Ranks top 10 moves based on "Out" values.  For each move, entry 0 is move type, entry 1 is the card, entry 2 is the gems
    Probs=Out[7:]
    BestInds=np.argsort(Probs)[::-1]
    GMoves=[]
    for i in BestInds:
        A=[]
        A.append(MType[i])
        if MType[i]==1:  #Take Gems
            gems=Gs[i-4]
            if Game.CheckGems(playern,gems):
                A.append([])
                A.append(gems)
                GMoves.append(A)
        if MType[i]==2 and i<len(Game.cards):  #Buy Card
            cardn=i
            gems=list(Game.cards[i].cost)
            gems.append(0)
            gems=np.array(gems)
            if Game.CheckBuy(playern,cardn,gems):
                A.append(cardn)
                A.append(gems)
                GMoves.append(A)
    return GMoves
    