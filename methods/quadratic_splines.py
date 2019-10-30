# -*- coding: utf-8 -*-
"""
@author: Alejandro Rojas & Santiago Passos
"""

import numpy as np
from copy import deepcopy
from pylab import plot, show, grid, xlabel, ylabel, title
from math import exp
import math

def quadratic_spline(x, f):
    n = len(x)
    mat = np.zeros((3*n - 3, (n-1)*3))   
    # First iteration, initial interpolation restriction
    mat[0,0] = x[0]**2
    mat[0,1] = x[0]
    mat[0,2] = 1
    # We start adding all the remaining interpolation restrictions
    j = 0
    for i in range(1, n):
        mat[i, j] = x[i]**2
        mat[i,j+1] = x[i]
        mat[i,j+2] = 1
        j += 3

    # We add the continuity restrictions
    j = 0
    for i in range(1, n-1):
        index = i + n - 1
        mat[index, j] = x[i]**2
        mat[index, j+1] = x[i]
        mat[index, j+2] = 1
        mat[index, j+3] = -1*(x[i]**2)
        mat[index, j+4] = -1*x[i]
        mat[index, j+5] = -1
        j += 3
        
    # We add the derivate restrictions
    j = 0
    for i in range(1, n-1):
        index = 2*n + i - 3
        mat[index, j] = 2*x[i]
        mat[index, j+1] = 1
        mat[index, j+3] = -1*(2*x[i])
        mat[index, j+4] = -1
        j += 3
    
    # We add bound restriction
    mat[3*n - 4, 0]  = 2
    
    # y vector
    y = np.array([[f(a) for a in x] + [0]*(2*n-3)], dtype='float64').transpose()
    
    sol = np.linalg.solve(mat,y)
    
    return mat,y,sol
