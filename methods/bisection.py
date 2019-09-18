#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:11:38 2019
Implementation of bisection.
https://en.wikipedia.org/wiki/Bisection_method

@author: Santiago Passos & Alejandro Rojas
"""
def bisection(function, left_point, right_point, max_iterations, error):
    """
    Find a root for the function in the interval [left_point, right_point].
    
    Parameters
    ----------
    function : function
        The function to find the root.
    left_point : numeric
        The left end of the interval.
    right_point : numeric
        The right end of the interval.
    max_iterations: int
        Maximum number of iterations before stopping the process.
    error : numeric
        The absolute error for the bisection. This is used to stop the
        method. The method stops when abs(x_n - x_n-1) < error. Where
        x_n are the sequence of mid point created trought the process.
    
    Returns
    -------
    numeric
        An approximate value for which the function is zero.
    """
    #######################################################
    print('Iteration    |    x    |    f(x)    |    Error  ')
    #######################################################
    iterations = 0
    # Set the left, right, and mid point and their respective values
    l = left_point; r = right_point; last_mid = (l + r)/2
    f_l = function(l); f_r = function(r); f_last = function(last_mid)
    #######################################################
    print('    %d      %.7f      %.7f      -' % (iterations,last_mid,f_last))
    #######################################################
    # Check if any of them make the function zero
    if abs(f_l) == 0:
        return l
    
    if abs(f_r) == 0:
        return r
    
    if abs(f_last) == 0:
        return last_mid
    
    # Do the first iteration of the method to find the next mid point
    if f_l*f_last <= 0:
        r = last_mid
        f_r = f_last
    else:
        l = last_mid
        f_l = f_last
    
    # Calculate the mid point
    mid = (l+r)/2
    f_mid = function(mid)
    iterations += 1
    while(abs(f_mid - f_last) >= error):
        if iterations > max_iterations:
            break
        # If the change of sign is on the left side then the new right point
        # is the mid point.
        if f_l*f_mid <=0:
            r = mid
            f_r = f_mid
        # If the change of sign is on the right side then the new left point
        # is the mid point.
        else:
            l = mid
            f_l = f_mid
            
        #######################################################    
        print('    %d      %.7f      %.7f      %.7f' % (iterations,last_mid,f_last,abs(f_mid - f_last)))
        #######################################################
        # Update the last mid point
        last_mid = mid
        f_last = f_mid
        # Calculate and evaluate the new mid point
        mid = (r+l)/2
        f_mid = function(mid)
        iterations += 1
    
    #print(iterations)
    return mid

