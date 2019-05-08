# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:37:47 2019

@author: huber.288
"""

from InputVector import *
import numpy as np
import pickle
from NeuralNet import *
import torch
from copy import deepcopy
import os
cur_path = os.path.dirname(__file__)
new_path1 = os.path.relpath('..\\Game Data\\GemCombos.p', cur_path)
Gs=pickle.load(open( new_path1, "rb" ))
MType=pickle.load(open( cur_path + '\\MType_Full.p', "rb" ))

def MakeMove(Game,playern,NN,Levels):
    Player = Game.player[playern]
    IV=InputVector_Full(Game,102)
    Out=NN(torch.FloatTensor(IV))
    Out=np.array(Out)
    np.random.seed()
    
    GMoves=RankMoves(Out,Game,Player,playern)
    if GMoves:
        MakeMove_GMove(Game,playern,GMoves[0])
    else:
        values = Out[1:7]
        gems=ExchangeGems(Game,playern,values)['Gems']
        Game.TakeGems(playern,gems)
        
def ExchangeGems(Game,playern,values):
    BestVal = 0
    BestCombo = np.array([0,0,0,0,0,0])
    gems = Game.player[playern].gems
    for combo in Gs:
        legal_combo = np.minimum(deepcopy(combo),Game.gems)
        if max(legal_combo) > 1 and Game.gems[np.argmax(legal_combo)] < 4:  #Don't bother checking 2 of same kind if not legal
            continue
        c = legal_combo + gems
        for _ in range(4):
            val = np.dot(c,values)  #value of taking all gems
            num = sum(c)
            if num <= 10:
                if val > BestVal:
                    BestVal = val
                    BestCombo = c - gems
                break
            LeastVal = 2
            LeastInd = 0
            for ind, n in enumerate(c):
                if n>0 and values[ind]<LeastVal:
                    LeastVal = values[ind]
                    LeastInd = ind
            change = np.zeros(6)
            change[LeastInd] += 1
            c -= change.astype(int)
    Answer = {}
    Answer['Gems']=BestCombo
    Answer['Value']=BestVal
    return Answer
        
def MakeMove_GMove(Game,playern,GMove):  
    if not GMove:
        #print('No possible moves')
        return Game
    if GMove[0]==1:
        Game.TakeGems(playern,GMove[2])
        return Game
    if GMove[0]>=2 and GMove[0]<=4:
        Game.BuyCard(playern,GMove[1][0],GMove[1][1],GMove[2])
        return Game
    if GMove[0]==5:
        Game.ReserveCard(playern,GMove[1][0],GMove[1][1],GMove[2])
        return Game
    
def RankMoves(Out,Game,Player,playern): #Ranks top 10 moves based on "Out" values.  For each move, entry 0 is move type, entry 1 is the card, entry 2 is the gems
    Probs=Out[7:]
    BestInds=np.argsort(Probs)[::-1]
    GMoves=[]
    for i in BestInds:
        A=[]
        A.append(MType[i])
        if MType[i]==1:  #Take Gems
            gems=Gs[i-12]
            if Game.CheckGems(playern,gems):
                A.append([])
                A.append(gems)
                GMoves.append(A)
        if MType[i]==2 and i-8<len(Game.cards[0]):  #Buy Card
            deckn=0
            cardn=i-8
            gems=np.maximum(Game.cards[deckn][cardn].cost - Player.bonuses, np.zeros(5))  #TODO:  Allow purchase with gold
            gems = list(gems)
            gems.append(0)
            gems=np.array(gems).astype(int)
            if Game.CheckBuy(playern,deckn,cardn,gems):
                A.append([deckn,cardn])
                A.append(gems)
                GMoves.append(A)
        if MType[i]==3 and i-4<len(Game.cards[1]):  #Buy Card
            deckn=1
            cardn=i-4
            gems=np.maximum(Game.cards[deckn][cardn].cost - Player.bonuses, np.zeros(5))
            gems = list(gems)
            gems.append(0)
            gems=np.array(gems).astype(int)
            if Game.CheckBuy(playern,deckn,cardn,gems):
                A.append([deckn,cardn])
                A.append(gems)
                GMoves.append(A)
        if MType[i]==4 and i<len(Game.cards[2]):  #Buy Card
            deckn=2
            cardn=i
            gems=np.maximum(Game.cards[deckn][cardn].cost - Player.bonuses, np.zeros(5))
            gems = list(gems)
            gems.append(0)
            gems=np.array(gems).astype(int)
            if Game.CheckBuy(playern,deckn,cardn,gems):
                A.append([deckn,cardn])
                A.append(gems)
                GMoves.append(A)
    return GMoves
    
def MakeMove_TreeSearch(Game,playern,Player,NN,Levels):
    TopMoves=5
    IV=InputVector_Simple(Game,46)
    #NN=Neural_Network([len(IV),30,26],Weights)
    Out=NN(torch.FloatTensor(IV))
    Out=np.array(Out)
    #Out=np.random.rand(26)   #Replace NN output with random vector
    GMoves=RankMoves(Out,Game,Player,playern)
    if Levels==-1:   #A way to generalize to non-tree searched models
        if GMoves:
            return 0,GMoves[0]
        else:
            return 0,[]
    BestScore=-1
    BestMove=[]
    for i in range(np.min([TopMoves,len(GMoves)])):
        G=deepcopy(Game)
        G=MakeMove_GMove(G,playern,GMoves[i])
        score=G.player[playern].VPs
        if Levels!=0 and BestScore<15 and score<15:
            score,Move=MakeMove_TreeSearch(G,playern,Player,NN,Levels-1)
        if score>BestScore:
            BestScore=score
            BestMove=GMoves[i]
    return BestScore,BestMove

        
        