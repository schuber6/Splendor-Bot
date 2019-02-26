# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:10:52 2019

@author: huber.288
"""
from SplendorCard import *
from Player import *
import pickle
import numpy as np

filename = 'Cards'
infile = open(filename,'rb')
Card = pickle.load(infile)
infile.close()


class Splendor:
    def __init__(self, nplayers):
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
        for i in range(4):
            self.DealCard()
        self.ShuffleNobles()
        for i in range(3):
            self.DealNoble()
        self.PickFirstPlayer()
        
        
    def ShuffleNobles(self):
        self.nobledeck=np.random.permutation(10)
    def ShuffleCards(self):
        self.deck=np.random.permutation(4)
    def DealCard(self):
        if len(self.deck)>0:
            self.cards.append(Card[self.deck[0]])
            self.deck=self.deck[1:]
    def DealNoble(self):
        self.nobles.append(self.nobledeck[0])
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
    def ReserveCard(self,playern,cardn,gems):
        if self.CheckReserve(playern,gems):
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
        if min(self.player[playern].gems-gems)<0: return 0
        if not min(gems%1==[0,0,0,0,0,0]): return 0
        if min(gems)<0: return 0
        Req=self.cards[cardn].cost-self.player[playern].bonuses
        Dif=Req-gems[:5]
        Dif=np.maximum(Dif,[0,0,0,0,0])
        if sum(Dif)-gems[5]>0: return 0
        return 1
    def CheckReserve(self,playern,gems):
        if len(gems)!=6: return 0
        if gems[5]>1: return 0 
        if min(self.gems-gems)<0: return 0
        if min(self.player[playern].gems+gems)<0: return 0
        if sum(self.player[playern].gems+gems)>10: return 0
        if not min(gems%1==[0,0,0,0,0,0]): return 0           #Check if numbers are integers
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
            return 'Gems: %s ; Cards: %s ; Players: %s' % (self.gems,st,self.player)
        else:
            return 'Player %s Wins!' % (self.winner)
    
        