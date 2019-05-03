# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:18:10 2019

@author: huber.288
"""
Ngames=100
NN=Neural_Network2(NetSize,Chosen)
Turns=np.zeros(Ngames)
for i2 in range(Ngames):
    Game=Splendor(1,GameType)
    for i in range(MaxTurns):
                
        playern=0
        Player=Game.player[0]
        MakeMove(Game,playern,Player,NN,Levels)
        Game.CheckWin()
        if Game.winner:
            Turns[i2]=i+1# +Game.player[0].VPs/100
            break
