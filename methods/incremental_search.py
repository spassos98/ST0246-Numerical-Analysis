#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:11:38 2019
Implementation of incremental search.
https://en.wikipedia.org/wiki/Incremental_search

@author: Santiago Passos & Alejandro Rojas
"""


def incremental_search(function, delta, x_0, max_iterations, side=1):
    """
    Look for an interval where a root for the function could exists.
    
    Parameters
    ----------
    function : function
        The function for which the interval will be searched.
    delta : numeric
        The step to use in each iteration.
    x_0 : numeric
        The point to start the search.
    max_iterations: int
        Maximum number of iterations before stopping the process.
    side : int, -1, 1
        Use 1 if you want to do the search from 0 to infinity. Use -1 if you
        want to do the search from 0 to -infinity.

    Returns
    -------
    l,r
        The left and right values for the interval where at least a root 
        exists.
    """
    current_x = x_0
    next_x = current_x + side*delta
    current_f = function(current_x)
    next_f = function(next_x)
    iterations = 0
    # While there is no change in the signs
    while current_f*next_f >= 0:
        if iterations > max_iterations:
            raise Exception('Maximum iterations reached.')
        current_x = next_x
        current_f = next_f
        # Update the interval
        next_x = next_x + side*delta
        next_f = function(next_x)
        iterations += 1
    
    # IF side is -1 then next_x < current_x
    if side == -1:
        return next_x, current_x
    else:
        return current_x, next_x