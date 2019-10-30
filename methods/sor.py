# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:54:55 2019

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:53:13 2019

@author: admin
"""

import numpy as np
import math

def norm2_vec(v):
    return np.linalg.norm(v)

def get_ldu_iterative(M):
    D = np.diag(np.diag(M))
    U = D - np.triu(M)
    L = D - np.tril(M)
    return D, L, U

def matrix_gauss_s(M, b, x0, tolerance, iterations, w = 1):
    # 0 < w < 1 -> Hacer que funciones que no convergían, que ahora si tengan
    # convergencia
    # 1 < w < 2 -> Acelerar convergencia
    D, L, U = get_ldu_iterative(M)
    T = np.matmul(np.linalg.inv(D-w*L),(1-w)*D + w*U)
    #T = np.matmul(np.linalg.inv(D-L),U)
    C = w*np.matmul(np.linalg.inv(D-w*L),b)
    #C = np.matmul(np.linalg.inv(D-L),b)
    err = math.inf
    i = 0
    while err > tolerance:
        print(x0)
        if i >= iterations:
            #raise Exception('maximum number of iterations reached')
            print('maximum number of iterations reached')
            return xn
        xn = np.matmul(T,x0) + C
        err = (norm2_vec(xn-x0))
        x0 = xn
        i += 1
    print('iterations {0}'.format(i))
    print('error {0}'.format(err))
    return xn