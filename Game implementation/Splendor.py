# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:10:52 2019

@author: huber.288
"""

import sys
sys.path.append('../Game implementation')
sys.path.append('../Convenient Solver Stuff')
from SplendorCard import *
from Player import *
import pickle
import numpy as np
from InitializeRandomCards import *
from MakeMove import *
import os
cur_path = os.path.dirname(__file__)
new_path1 = os.path.relpath('..\\Game Data\\Nobles', cur_path)
new_path2 = os.path.relpath('..\\Game Data\\Cards', cur_path)

infile = open(new_path1,'rb')
Noble = pickle.load(infile)
infile.close()




class Splendor:
    def __init__(self, nplayers, CType):
        if CType==0:
            infile = open(new_path2,'rb')
            self.Card = pickle.load(infile)
            infile.close()
        if CType==1:
            self.Card=MakeCards()
        self.nplayers=nplayers
        if nplayers==1:
            self.gems=np.array([4,4,4,4,4,5])
        if nplayers==2:
            self.gems=np.array([4,4,4,4,4,5])
        if nplayers==3:
            self.gems=np.array([5,5,5,5,5,5])
        if nplayers==4:
            self.gems=np.array([7,7,7,7,7,5])
        self.player=[]
        self.winner=[]
        for i in range(nplayers):
            self.player.append(Player())
        self.cards=[]
        self.nobles=[]
        self.ShuffleCards()
        self.ShuffleNobles()
        for i in range(4):
            self.DealCard()
        for i in range(nplayers+1):
            self.DealNoble()
        self.ShuffleNobles()
        self.PickFirstPlayer()
        
        
    def ShuffleNobles(self):
        self.nobledeck=np.random.permutation(10)
    def ShuffleCards(self):
        self.deck=np.random.permutation(4)
    def DealCard(self):
        if len(self.deck)>0:
            self.cards.append(self.Card[self.deck[0]])
            self.deck=self.deck[1:]
    def DealNoble(self):
        self.nobles.append(Noble[self.nobledeck[0]])
        self.nobledeck=self.nobledeck[1:]
    def PickFirstPlayer(self):
        self.first=np.random.randint(self.nplayers)
        
        
    #Actions    
    def BuyCard(self,playern,cardn,gems):  
        if self.CheckBuy(playern,cardn,gems)==0:
            print('Can\'t Buy That')
            return
        self.gems+=gems
        self.player[playern].gems-=gems
        self.player[playern].bonuses[self.cards[cardn].bonus]+=1
        self.player[playern].VPs+=self.cards[cardn].VPs
        del self.cards[cardn]
        self.DealCard()
        nob=self.CheckNoble(playern)
        if nob:
            self.player[playern].VPs+=self.nobles[nob[0]].VPs   #TODO:  Allow choosing of noble in case of multiple
            del self.nobles[nob[0]]
    def ReserveCard(self,playern,cardn,gems):
        if self.CheckReserve(playern,cardn,gems):
            self.gems-=gems
            self.player[playern].gems+=gems
        else:
            print('Illegal Reserve')
            return
        self.player[playern].reserved.append(self.cards[cardn])
        del self.cards[cardn]
        self.DealCard()
    def TakeGems(self,playern,gems):
        if self.CheckGems(playern,gems)==0:
            print('Illegal Gems')
            return
        self.gems-=gems
        self.player[playern].gems+=gems
        
    def CheckBuy(self,playern,cardn,gems):
        print(len(self.cards))
        print(cardn+1)
        if len(self.cards)<cardn+1: return 0
        if min(self.player[playern].gems-gems)<0: return 0
        if not min(gems%1==[0,0,0,0,0,0]): return 0
        if min(gems)<0: return 0
        Req=self.cards[cardn].cost-self.player[playern].bonuses
        Dif=Req-gems[:5]
        Dif=np.maximum(Dif,[0,0,0,0,0])
        if sum(Dif)-gems[5]>0: return 0
        return 1
    
    def CheckReserve(self,playern,cardn,gems):
        if len(gems)!=6: return 0
        if gems[5]>1: return 0 
        if min(self.gems-gems)<0: return 0
        if min(self.player[playern].gems+gems)<0: return 0
        if sum(self.player[playern].gems+gems)>10: return 0
        if not min(gems%1==[0,0,0,0,0,0]): return 0           #Check if numbers are integers
        if len(self.cards)<cardn+1: return 0
        s=np.sort(gems[0:5])
        if s[-1]>0: return 0
        return 1
    def CheckGems(self,playern,gems):
        if len(gems)!=6: return 0
        if gems[5]>0: return 0             #Can't take gold this way
        if min(self.gems-gems)<0: return 0
        if min(self.player[playern].gems+gems)<0: return 0
        if not min(gems%1==[0,0,0,0,0,0]): return 0           #Check if numbers are integers
        if max(gems)>2: return 0
        if max(gems)==2:                   #2 of one type
            s=np.sort(gems)
            if s[-2]>0: return 0
            if self.gems[np.argmax(gems)]<4: return 0
            return 1
        s=np.sort(gems)
        if s[-4]>0: return 0              #1 of three types
        return 1
    
    def CheckNoble(self,playern):
        Bons=self.player[playern].bonuses
        Earned=[]
        for ind,noble in enumerate(self.nobles):
            if min(Bons-noble.cost)>=0:
                Earned.append(ind)
        return Earned
    def CheckWin(self):
        if self.winner:
            return
        points=[]
        bonuses=[]
        for i in range(self.nplayers):
            points.append(self.player[i].VPs)
            bonuses.append(sum(self.player[i].bonuses))
        if max(points)>=15:
            points=np.array(points)
            bonuses=np.array(bonuses)
            if sum(points==max(points))==1:
                self.winner.append(np.argmax(points))
            else:
                losers=points!=max(points)
                bonuses[losers]=1000
                for i in range(self.nplayers):
                    if bonuses[i]==min(bonuses):
                        self.winner.append(i)
        
    def __repr__(self):
        if not self.winner:
            st=''
            for i in range(len(self.cards)):
                st+=str(self.cards[i]) + '; '
            nst=''
            for i in self.nobles:
                nst+=str(i)+'; '
            return 'Gems: %s ; Cards: %s ; Nobles: %s ; Players: %s' % (self.gems,st,nst,self.player)
        else:
            return 'Player %s Wins!' % (self.winner)
        
def ThoroughCheck(NN,GameType,Levels):
    
    Ngames=100
    MaxTurns=10
    Turns=np.zeros(Ngames)+MaxTurns
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
    return Turns
    
        