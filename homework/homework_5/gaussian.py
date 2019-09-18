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

def exchange_rows_partial(M, i, j):
    maxi = 0
    index = 0
    for idx in range(i+1, M.shape[0]):
        pivot = np.abs(M[idx, j])
        if pivot > maxi:
            maxi = pivot
            index = idx

    temp = deepcopy(M[index, j:])
    M[index, j:] = M[i, j:]
    M[i, j:] = temp
    return M

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


def reduce_matrix(M):
    cont = 0
    for j in range(M.shape[1]-1):
        pivot = M[cont, j]
        if pivot == 0:
            M = exchange_rows(M, cont, j)
        pivot = M[cont, j]
        if pivot == 0:
            raise Exception('It is not possible to reduce the matrix')
        pivot_row = M[cont, j:]
        for i in range(cont+1, M.shape[0]):
            num = M[i,j]
            multiplier = num/pivot
            M[i,j:] = M[i,j:] - multiplier * pivot_row
        cont += 1
    
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


def regressive_substitution(M):
    coefs = np.array([[1]])
    for idx in np.arange(M.shape[0]-1,-1,-1):
        col_coefs = np.flip(M[idx,idx+1:]).reshape(-1, 1)
        val = np.dot(coefs, col_coefs)
        val /= M[idx,idx]
        coefs = np.append(coefs, -1*val, axis=1)

    return -1*np.flip(coefs[0,1:]).transpose().reshape(-1,1)


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


def gauss_simple(A, b):
    Ab = np.concatenate((A,b), axis = 1)
    Ab_reduced = reduce_matrix(Ab)
    sol = regressive_substitution(Ab_reduced)
    return sol

def gauss_partial(A,b):
    Ab = np.concatenate((A,b), axis = 1)
    Ab_reduced = reduce_matrix_partial(Ab)
    sol = regressive_substitution(Ab_reduced)
    return sol

def gauss_total(A,b):
    Ab = np.concatenate((A,b), axis = 1)
    Ab_reduced, array_of_changes = reduce_matrix_total(Ab)
    sol = regressive_substitution_total(Ab_reduced, array_of_changes)
    
    return sol


# =============================================================================
# PRUEBA METÓDOS
# =============================================================================

A = np.array([[2, -1, 0, 3],
              [1, 0.5, 3, 8],
              [0, 13, -2, 11],
              [14, 5, -2, 3]])

b = np.array([[1, 1, 1, 1]], dtype='float64').transpose()


sol = gauss_total(A,b)
print(sol)
aprox_b = np.matmul(A, sol).reshape(-1,1)
print(np.linalg.norm(b - aprox_b, ord='fro'))
