# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:52:00 2019

@author: huber.288
"""

from sklearn.neural_network import MLPClassifier

def NeuralNet(IV,Weights):
    X = IV.reshape(1,-1)
    y = np.random.rand(26).reshape(1,-1)
    clf = MLPClassifier(alpha=1e-5,hidden_layer_sizes=(30, 26), random_state=1)
    clf.fit(X,y)
    clf.coefs_=Weights[0]
    clf.intercepts_=Weights[1]
    return clf.predict(IV)


