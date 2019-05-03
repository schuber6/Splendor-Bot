# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:29:02 2019

@author: huber.288
"""

from NeuralNet4 import *
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable

slope=5
ys=[]
xs=[]
Xs=torch.arange(0,10,dtype=torch.float)


NN=NeuralNet4([1,1,1],[])
for i in Xs:
    ys.append(i*slope+np.random.rand()*6)
  
xs=Variable(torch.FloatTensor(Xs[:,None]))   
out=NN(xs)
outL=[float(i) for i in out]
ys=np.array(ys)
ys=ys[:,None]  
ys=Variable(torch.FloatTensor(ys))
plt.scatter(xs,ys)
plt.scatter(xs,outL)


loss_fn = torch.nn.MSELoss()
optim = torch.optim.Adam(NN.parameters(),lr=.01)
L=[]
for epoch in range(1000):
    optim.zero_grad()
    out=NN(xs)
    loss = loss_fn(out, ys)
    
    loss.backward()
    A=NN.parameters()

    for p in A:
        p.grad.data*=0
    optim.step()
    outL=[float(i) for i in out]
    if epoch % 10==0:
        L.append(float(loss))
    if epoch % 100==0:
        plt.scatter(xs,ys)
        plt.scatter(xs,outL)
        plt.show()
        

plt.plot(L)
plt.show()


