# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:37:15 2019

@author: Santiago Passos & Alejandro Rojas
"""
import numpy as np
   
def is_diagonal_dominant(M):
    # array of elements in diagonal
    d = np.diag(M)
    # Matrix full of 0 except for the diagonal
    D = np.diag(d)
    # M Matrix with 0 in diagonal
    Md = M - D
    # Sum of rows of Md
    row_sum = np.sum(Md, axis = 1)
    # Sum of columns of Md
    col_sum = np.sum(Md, axis = 0)
    # If each element of the diagonal is greater that the sum of elements of 
    # the row
    if np.all(abs(d) > row_sum):
        return True
    # If each element of the diagonal is greater that the sum of elements of 
    # the column
    elif np.all(abs(d) > col_sum):
        return True
    return False

def is_pos_def(M):
    if np.array_equal(M, M.T):
        val, vec = np.linalg.eig(M)
        d = val > 0
        if np.all(d):
            return True
    return False

def eigv(M):
    return np.linalg.eig(M)

def determinant_recursive(A):
  if(A.shape==(1,1)): return A[0,0]
  sum = 0
  rows = A.shape[0]
  for i in range(rows):
      new_matrix = None
      if i == 0:
          new_matrix = A[1:,1:]
      elif i == rows-1:
          new_matrix = A[1:,:-1]
      else:
          new_matrix = np.concatenate((A[1:, :i], A[1:, i+1:]), axis=1)
      sum += ((-1)**i) *A [0,i] * determinant_recursive(new_matrix)
  return sum