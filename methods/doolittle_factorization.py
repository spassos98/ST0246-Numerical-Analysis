# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:45:32 2019

@author: admin
"""
import numpy as np

def doolittle_factorization(A): #lkk = 1
    n = A.shape[0]
    U = np.eye(n, dtype=np.float64)
    L = np.eye(n, dtype=np.float64)
    
    for k in range(n):
        suma1 = 0.0
        for p in range(k):
            suma1 += L[k,p] * U[p, k]
        U[k, k] = A[k, k] - suma1
        
        for i in range(k+1, n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i, p] * U[p, k]
            L[i, k] = (A[i, k] - suma2) / U[k, k]
        
        for j in range(k+1, n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k, p] * U[p, j]
            U[k, j] = (A[k, j] - suma3)
    return L, U