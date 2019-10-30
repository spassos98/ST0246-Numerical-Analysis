# -*- coding: utf-8 -*-
"""
@author: Alejandro Rojas & Santiago Passos
"""

import numpy as np
from copy import deepcopy
from pylab import plot, show, grid, xlabel, ylabel, title
from math import exp
import math

def qubic_spline(x, f):
    n = len(x)
    mat = np.zeros((4*n - 4, (n-1)*4))
    # First iteration, initial interpolation restriction
    mat[0,0] = x[0]**3
    mat[0,1] = x[0]**2
    mat[0,2] = x[0]
    mat[0,3] = 1
    # We start adding all the remaining interpolation restrictions
    j = 0
    for i in range(1, n):
        mat[i, j] = x[i]**3
        mat[i,j+1] = x[i]**2
        mat[i,j+2] = x[i]
        mat[i,j+3] = 1
        j += 4

    # We add the continuity restrictions
    j = 0
    for i in range(1, n-1):
        index = i + n - 1
        mat[index, j] = x[i]**3
        mat[index, j+1] = x[i]**2
        mat[index, j+2] = x[i]
        mat[index, j+3] = 1
        
        mat[index, j+4] = -1*(x[i]**3)
        mat[index, j+5] = -1*(x[i]**2)
        mat[index, j+6] = -1*(x[i])
        mat[index, j+7] = -1
        j += 4
        
    # We add the first derivate restrictions
    j = 0
    for i in range(1, n-1):
        index = 2*n + i - 3
        mat[index, j] = 3*x[i]**2
        mat[index, j+1] = 2*x[i]
        mat[index, j+2] = 1
        mat[index, j+3] = 0
        
        mat[index, j+4] = -1*(3*x[i]**2)
        mat[index, j+5] = -1*(2*x[i])
        mat[index, j+6] = -1
        mat[index, j+7] = 0
        j += 4
        
    # We add the second derivate restrictions
    j = 0
    for i in range(1, n-1):
        index = 3*n + i - 5
        mat[index, j] = 6*x[i]
        mat[index, j+1] = 2
        mat[index, j+2] = 0
        mat[index, j+3] = 0
        
        mat[index, j+4] = -1*(6*x[i])
        mat[index, j+5] = -1*(2)
        mat[index, j+6] = 0
        mat[index, j+7] = 0
        j += 4
    
    # We add bound restriction
    mat[4*n - 6, 0]  = 6
    mat[4*n - 6, 1]  = 2
    mat[4*n - 5, -4]  = 6
    mat[4*n - 5, -3]  = 2
    
    # y vector
    y = np.array([[f(a) for a in x] + [0]*(3*n-4)], dtype='float64').transpose()
    print(mat)
    sol = np.linalg.solve(mat,y)
    
    return mat,y,sol
