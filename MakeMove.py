# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:29:54 2019

@author: huber.288
"""
from InputVector import *
import numpy as np
import pickle
from NeuralNet import *
import torch
from copy import deepcopy
Gs=pickle.load(open( "GemCombos.p", "rb" ))
MType=pickle.load(open( "MoveType.p", "rb" ))

def MakeMove(Game,playern,Player,NN,Levels):
    #IV=InputVector_Simple(Game,46)
    #NN=Neural_Network([len(IV),30,26],Weights)
    #Out=NN(torch.FloatTensor(IV))
    #Out=np.array(Out)
    #Out=np.random.rand(26)   #Replace NN output with random vector
    #GMoves=RankMoves(Out,Game,Player,playern)
    #if GMoves:
    #    MakeMove_GMove(Game,playern,GMoves[0])
    #else:
    #    MakeMove_GMove(Game,playern,[])

    _,GMove=MakeMove_TreeSearch(Game,playern,Player,NN,Levels)
    MakeMove_GMove(Game,playern,GMove)
        
def MakeMove_GMove(Game,playern,GMove):  
    if not GMove:
        #print('No possible moves')
        return Game
    if GMove[0]==1:
        Game.TakeGems(playern,GMove[2])
        return Game
    if GMove[0]==2:
        Game.BuyCard(playern,GMove[1],GMove[2])
        return Game
    if GMove[0]==3:
        Game.ReserveCard(playern,GMove[1],GMove[2])
        return Game
    
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

        
        