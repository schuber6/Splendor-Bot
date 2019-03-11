# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:51:22 2019

@author: huber.288
"""
from Splendor import *
Game=Splendor(1,1)
N=Game.nobles
print(Game)

Turns=np.zeros((Nnets,Ngames))+MaxTurns+1
for i0 in range(Nnets):
    Weights=[]
    NN=Neural_Network2(NetSize,Weights)
    AllWeights.append(NN.W)
    for i2 in range(Ngames):
        Game=Splendor(1,GameType)
        for i in range(MaxTurns):
            #IV=InputVector_Simple(Game,46)
            playern=0
            Player=Game.player[0]
            MakeMove(Game,playern,Player,NN,Levels)
            Game.CheckWin()
            if Game.winner:
                Turns[i0,i2]=i+1# +Game.player[0].VPs/100
                break
Scores=np.mean(Turns,axis=1)
#print(Scores)




AllWeights,Ps=NaturalSelection(AllWeights,Scores,NetSize,mutation,step,Nnets)
print(Ps)
AvScores.append([min(Scores),Ps[0],Ps[4]])