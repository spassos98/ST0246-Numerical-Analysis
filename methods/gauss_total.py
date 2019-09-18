#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:18:43 2019

@author: Santiago Passos & Alejandro Rojas
"""

import numpy as np
from copy import deepcopy

def exchange_rows_total(M, idx_1, idx_2, j):
    temp = deepcopy(M[idx_2, j:])
    M[idx_2, j:] = M[idx_1, j:]
    M[idx_1, j:] = temp
    return M


def exchange_cols_total(M, idx_1, idx_2, j):
    temp = deepcopy(M[j:, idx_2])
    M[j:, idx_2] = M[j:, idx_1]
    M[j:, idx_1] = temp
    return M


def reduce_matrix_total(M):
    array_of_changes = np.array([[0,0]])
    for j in range(M.shape[1]-1):
        sub_matrix = deepcopy(M[j:, j:-1])
        idx_max = np.argmax(sub_matrix)
        idx_col = (idx_max % sub_matrix.shape[1]) + j
        idx_row = int(idx_max / sub_matrix.shape[0]) + j
        M = exchange_rows_total(M, j, idx_row, j)
        M = exchange_cols_total(M, j, idx_col, j)
        array_of_changes = np.append(array_of_changes, [[idx_col, j]], axis=0)
        pivot = M[j, j]
        pivot_row = M[j, j:]
        for i in range(j+1, M.shape[0]):
            num = M[i,j]
            multiplier = num/pivot
            M[i,j:] = M[i,j:] - multiplier * pivot_row
    
    return M, array_of_changes[1:,:]


def regressive_substitution_total(M, array_of_changes):
    coefs = np.zeros((1, M.shape[0] + 1))
    coefs[0,0] = 1
    for idx in np.arange(M.shape[0]-1,-1,-1):
        col_coefs = np.flip(M[idx,:]).reshape(-1, 1)
        val = np.dot(coefs, col_coefs)
        val /= M[idx,idx]
        coefs[0, M.shape[0]-idx] = -1*val
        idx_col_1 = M.shape[0] - array_of_changes[idx, 0]
        idx_col_2 = M.shape[0] - array_of_changes[idx, 1]
        coefs = exchange_cols_total(coefs, idx_col_1, idx_col_2, 0)

    return -1*np.flip(coefs[0,1:]).transpose().reshape(-1,1)


def gauss_total(A,b):
    Ab = np.concatenate((A,b), axis = 1)
    Ab_reduced, array_of_changes = reduce_matrix_total(Ab)
    sol = regressive_substitution_total(Ab_reduced, array_of_changes)
    return sol
