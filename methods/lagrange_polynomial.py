# -*- coding: utf-8 -*-
"""
@author: Alejandro Rojas & Santiago Passos
"""

def lagrange_interpolation(x_v, f, coeffs = False):
    y = [f(a) for a in x_v]
    def P(x):
        total = 0
        n = len(x_v)
        for i in range(n):
            xi = x_v[i]
            yi = y[i]
            def g(i, n):
                tot_mul = 1
                for j in range(n):
                    if i==j: continue
                    xj = x_v[j]
                    # yj = y[j]
                    tot_mul *= (x - xj) / float(xi - xj)
                return tot_mul 
            total += yi * g(i, n)
        return total
    if coeffs:
        return P, coeffs
    return P
