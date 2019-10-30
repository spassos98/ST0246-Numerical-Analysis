# -*- coding: utf-8 -*-
"""
@author: Alejandro Rojas & Santiago Passos
"""

import numpy as np
from copy import deepcopy
from pylab import plot, show, grid, xlabel, ylabel, title
from math import exp
import math

def linear_spline(x, f):
    n = len(x)
    mat = np.zeros((2*n - 2, (n-1)*2))   
    # First iteration, initial interpolation restriction
    mat[0,0] = x[0]
    mat[0,1] = 1
    
    # We start adding all the remaining interpolation restrictions
    j = 0
    for i in range(1, n):
        mat[i, j] = x[i]
        mat[i,j+1] = 1
        j += 2

    # We add the continuity restrictions
    j = 0
    for i in range(1, n-1):
        index = i + n - 1
        mat[index, j] = x[i]
        mat[index, j+1] = 1
        mat[index, j+2] = -x[i]
        mat[index,j + 3] = -1
        j += 2
    
    # y vector
    y = np.array([[f(a) for a in x] + [0]*(n-2)], dtype='float64').transpose()
    
    sol = np.linalg.solve(mat,y)
    
    return mat,y,sol
