#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:10:24 2019

Author: Santiago Passos & Alejandro Rojas
"""

from math import inf

eps = 0.05
last = eps
cut = 1
true_eps = last
iterations = 0
while iterations < 100:
    iterations += 1
    while 1 != eps + 1:
        last = eps
        eps /= (1 + cut)
        if 1+cut == 1:
            break
    eps = last
    cut /= 2

print('Machine epsilon: %s' % last)

max_number = 2**4000
while max_number < inf:
    max_number*=2
    print(max_number)

print(max_number)
