# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:39:44 2019

@author: admin
"""

import numpy as np
from copy import deepcopy
from scipy.linalg import solve_triangular

def lu_gauss_partial(A,b):
  #Ab = np.concatenate((A,b), axis = 1)
  L, U, P = reduce_matrix_partial(A)
  Pb = np.matmul(P, b)
  z = solve_triangular(L, Pb, lower=True) #Lz = b
  x = solve_triangular(U, z, lower=False) #Ux = z
  return x

def reduce_matrix_partial(M):
    cont = 0
    print(np.round(M,8))
    print('------------------------------------------------------')
    # Initialization of L and P matrix
    L = np.identity(M.shape[0])
    P = np.identity(M.shape[0])
    for j in range(M.shape[1]-1):
        M = exchange_rows_partial(M, P, L, cont, j)
        pivot = M[cont, j]
        pivot_row = M[cont, j:]
        for i in range(cont+1, M.shape[0]):
            num = M[i,j]
            multiplier = num/pivot
            L[i,j] = multiplier
            M[i,j:] = M[i,j:] - multiplier * pivot_row
        cont += 1
        print(np.round(M,8)) # U
        print(np.round(L,8))
        print(np.round(P,8))
        print('------------------------------------------------------')
    return L, M, P

def exchange_rows_partial(M, P, L, i, j):
    maxi = 0
    index = 0
    for idx in range(i, M.shape[0]):
        pivot = np.abs(M[idx, j])
        if pivot > maxi:
            maxi = pivot
            index = idx
	
  	# Swap M rows
    M = swap_matrix(M, index, i, j)
    # Swap P rows
    P = swap_matrix(P, index, i, j)
    # Swap L rows
    temp = deepcopy(L[index, 0:j])
    L[index, 0:j] = L[i, 0:j]
    L[i, 0:j] = temp
    return M

def swap_matrix(M, index, i, j):
  temp = deepcopy(M[index, j:])
  M[index, j:] = M[i, j:]
  M[i, j:] = temp
  return M