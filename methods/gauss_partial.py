#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:18:43 2019

@author: Santiago Passos & Alejandro Rojas
"""

import numpy as np
from copy import deepcopy

def exchange_rows(M, i, j):
    for idx in range(i+1, M.shape[0]):
        pivot = M[idx, j]
        if pivot != 0:
            temp = deepcopy(M[idx, j:])
            M[idx, j:] = M[i, j:]
            M[i, j:] = temp
            return M
    return M


def reduce_matrix_partial(M):
    cont = 0
    for j in range(M.shape[1]-1):
        M = exchange_rows(M, cont, j)
        pivot = M[cont, j]
        pivot_row = M[cont, j:]
        for i in range(cont+1, M.shape[0]):
            num = M[i,j]
            multiplier = num/pivot
            M[i,j:] = M[i,j:] - multiplier * pivot_row
        cont += 1
    
    return M


def regressive_substitution(M):
    coefs = np.array([[1]])
    for idx in np.arange(M.shape[0]-1,-1,-1):
        col_coefs = np.flip(M[idx,idx+1:]).reshape(-1, 1)
        val = np.dot(coefs, col_coefs)
        val /= M[idx,idx]
        coefs = np.append(coefs, -1*val, axis=1)

    return -1*np.flip(coefs[0,1:]).transpose().reshape(-1,1)


def gauss_partial(A,b):
    Ab = np.concatenate((A,b), axis = 1)
    Ab_reduced = reduce_matrix_partial(Ab)
    sol = regressive_substitution(Ab_reduced)
    return sol
