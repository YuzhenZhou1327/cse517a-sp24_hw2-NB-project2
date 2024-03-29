#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayes(x, y, x1):
# =============================================================================
#function logratio = naivebayes(x,y,x1);
#
#Computation of log P(Y|X=x1) using Bayes Rule
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#x1: input vector of d dimensions (dx1)
#
#Output:
#logratio: log (P(Y = 1|X=x1)/P(Y=-1|X=x1))
# =============================================================================


    
    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    X1= np.matrix(x1)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
# =============================================================================
# fill in code here
    # YOUR CODE HERE
    pos, neg = naivebayesPY(X, y)
    positive_prob, negative_prob = naivebayesPXY(X, y)
    temp1 = np.where(X1 == 0, 1, positive_prob)
    temp2 = np.where(X1 == 0, 1, negative_prob)
    poslog = np.prod(temp1 ** pos)
    neglog = np.prod(temp2 ** neg)
    logration = np.log(poslog/neglog)
    print(logration)
    return logration
# =============================================================================
