# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:37:09 2019

@author: admin
"""

import numpy as np
from copy import deepcopy
from scipy.linalg import solve_triangular

def lu_gauss_simple(A, b):
    L, U = reduce_matrix_lu(A)
    z = solve_triangular(L, b, lower=True) #Lz = b
    x = solve_triangular(U, z, lower=False) #Ux = z
    return x

def reduce_matrix_lu(M):
    print(np.round(M,8))
    print('------------------------------------------------------')
    cont = 0
    # Initialization of L matrix
    L = np.identity(M.shape[0])
    for j in range(M.shape[1]-1):
        pivot = M[cont, j]
        # It is not possible to factorize a non invertible matrix
        if pivot == 0:
            raise Exception('It is not possible to factorize the matrix')
        pivot_row = M[cont, j:]
        for i in range(cont+1, M.shape[0]):
            num = M[i,j]
            multiplier = num/pivot
            L[i,j] = multiplier
            M[i,j:] = M[i,j:] - multiplier * pivot_row
        cont += 1
        print(np.round(M,8))
        print(np.round(L,8))
        print('------------------------------------------------------')
    
    return L, M

def exchange_rows(M, i, j):
    for idx in range(i+1, M.shape[0]):
        pivot = M[idx, j]
        if pivot != 0:
            temp = deepcopy(M[idx, j:])
            M[idx, j:] = M[i, j:]
            M[i, j:] = temp
            return M
    return M