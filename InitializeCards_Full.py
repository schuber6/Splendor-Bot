# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:41:22 2019

@author: huber.288
"""

from SplendorCard import *
import pickle

Card1=[]
Card1.append(SplendorCard(0,0,[0,2,2,0,1])) #White cards
Card1.append(SplendorCard(0,0,[0,0,0,2,1]))
Card1.append(SplendorCard(0,0,[0,1,1,1,1]))
Card1.append(SplendorCard(0,0,[0,3,0,0,0]))
Card1.append(SplendorCard(0,0,[0,2,0,0,2]))
Card1.append(SplendorCard(0,0,[0,1,2,1,1]))
Card1.append(SplendorCard(0,0,[3,1,0,0,1]))
Card1.append(SplendorCard(0,1,[0,0,4,0,0]))

Card1.append(SplendorCard(1,0,[1,0,0,0,2])) #Blue cards
Card1.append(SplendorCard(1,0,[1,0,1,2,1]))
Card1.append(SplendorCard(1,0,[1,0,1,1,1]))
Card1.append(SplendorCard(1,0,[0,1,3,1,0]))
Card1.append(SplendorCard(1,0,[0,0,0,0,3]))
Card1.append(SplendorCard(1,0,[1,0,2,2,0]))
Card1.append(SplendorCard(1,0,[0,0,2,0,2]))
Card1.append(SplendorCard(1,1,[0,0,0,4,0]))

Card1.append(SplendorCard(2,0,[3,1,0,0,0])) #Green cards
Card1.append(SplendorCard(2,0,[0,2,0,2,0]))
Card1.append(SplendorCard(2,0,[1,3,1,0,0]))
Card1.append(SplendorCard(2,0,[1,1,0,1,1]))
Card1.append(SplendorCard(2,0,[1,1,0,1,2]))
Card1.append(SplendorCard(2,0,[0,1,0,2,2]))
Card1.append(SplendorCard(2,0,[0,0,0,3,0]))
Card1.append(SplendorCard(2,1,[0,0,0,0,4]))

Card1.append(SplendorCard(3,0,[3,0,0,0,0])) #Red cards
Card1.append(SplendorCard(3,0,[1,0,0,1,3]))
Card1.append(SplendorCard(3,0,[0,2,1,0,0]))
Card1.append(SplendorCard(3,0,[2,0,1,0,2]))
Card1.append(SplendorCard(3,0,[2,1,1,0,1]))
Card1.append(SplendorCard(3,0,[1,1,1,0,1]))
Card1.append(SplendorCard(3,0,[2,0,0,2,0]))
Card1.append(SplendorCard(3,1,[4,0,0,0,0]))

Card1.append(SplendorCard(4,0,[1,1,1,1,0])) #Black cards
Card1.append(SplendorCard(4,0,[0,0,2,1,0]))
Card1.append(SplendorCard(4,0,[2,0,2,0,0]))
Card1.append(SplendorCard(4,0,[0,0,1,3,1]))
Card1.append(SplendorCard(4,0,[0,0,3,0,0]))
Card1.append(SplendorCard(4,0,[1,2,1,1,0]))
Card1.append(SplendorCard(4,0,[2,2,0,1,0]))
Card1.append(SplendorCard(4,1,[0,4,0,0,0]))

Card2=[]
Card2.append(SplendorCard(0,1,[0,0,3,2,2])) #White cards
Card2.append(SplendorCard(0,1,[2,3,0,3,0]))
Card2.append(SplendorCard(0,2,[0,0,1,4,2]))
Card2.append(SplendorCard(0,2,[0,0,0,5,0]))
Card2.append(SplendorCard(0,2,[0,0,0,5,3]))
Card2.append(SplendorCard(0,3,[6,0,0,0,0]))

Card2.append(SplendorCard(1,1,[0,2,2,3,0])) #Blue cards
Card2.append(SplendorCard(1,1,[0,2,3,0,3]))
Card2.append(SplendorCard(1,2,[5,3,0,0,0]))
Card2.append(SplendorCard(1,2,[0,5,0,0,0]))
Card2.append(SplendorCard(1,2,[2,0,0,1,4]))
Card2.append(SplendorCard(1,3,[0,6,0,0,0]))

Card2.append(SplendorCard(2,1,[3,0,2,3,0])) #Green cards
Card2.append(SplendorCard(2,1,[2,3,0,0,2]))
Card2.append(SplendorCard(2,2,[4,2,0,0,1]))
Card2.append(SplendorCard(2,2,[0,0,5,0,0]))
Card2.append(SplendorCard(2,2,[0,5,3,0,0]))
Card2.append(SplendorCard(2,3,[0,0,6,0,0]))

Card2.append(SplendorCard(3,1,[0,3,0,2,3])) #Red cards
Card2.append(SplendorCard(3,1,[2,0,0,2,3]))
Card2.append(SplendorCard(3,2,[1,4,2,0,0]))
Card2.append(SplendorCard(3,2,[3,0,0,0,5]))
Card2.append(SplendorCard(3,2,[0,0,0,0,5]))
Card2.append(SplendorCard(3,3,[0,0,0,6,0]))

Card2.append(SplendorCard(4,1,[3,2,2,0,0])) #Black cards
Card2.append(SplendorCard(4,1,[3,0,3,0,2]))
Card2.append(SplendorCard(4,2,[0,1,4,2,0]))
Card2.append(SplendorCard(4,2,[5,0,0,0,0]))
Card2.append(SplendorCard(4,2,[0,0,5,3,0]))
Card2.append(SplendorCard(4,3,[0,0,0,0,6]))

Card3=[]
Card3.append(SplendorCard(0,3,[0,3,3,5,3])) #White cards
Card3.append(SplendorCard(0,4,[0,0,0,0,7]))
Card3.append(SplendorCard(0,4,[3,0,0,3,6]))
Card3.append(SplendorCard(0,5,[3,0,0,0,7]))

Card3.append(SplendorCard(1,3,[3,0,3,3,5])) #Blue cards
Card3.append(SplendorCard(1,4,[7,0,0,0,0]))
Card3.append(SplendorCard(1,4,[6,3,0,0,3]))
Card3.append(SplendorCard(1,5,[7,3,0,0,0]))

Card3.append(SplendorCard(2,3,[5,3,0,3,0])) #Green cards
Card3.append(SplendorCard(2,4,[3,6,3,0,0]))
Card3.append(SplendorCard(2,4,[0,7,0,0,0]))
Card3.append(SplendorCard(2,5,[0,7,3,0,0]))

Card3.append(SplendorCard(3,3,[3,5,3,0,3])) #Red cards
Card3.append(SplendorCard(3,4,[0,0,7,0,0]))
Card3.append(SplendorCard(3,4,[0,3,6,3,0]))
Card3.append(SplendorCard(3,5,[0,0,7,3,0]))

Card3.append(SplendorCard(3,3,[3,3,5,3,0])) #Black cards
Card3.append(SplendorCard(3,4,[0,0,0,7,0]))
Card3.append(SplendorCard(3,4,[0,0,3,6,3]))
Card3.append(SplendorCard(3,5,[0,0,0,7,3]))

Card=[Card1,Card2,Card3]

filename = 'Cards_Full'
outfile = open(filename,'wb')
pickle.dump(Card,outfile)
outfile.close()