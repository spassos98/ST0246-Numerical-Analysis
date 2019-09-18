#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:11:38 2019

@author: yoksil
"""

import math


def incremental_search(function, delta, x0, max_iterations, side=1):
    """
    Look for an interval where a root for the function could exists.
    
    Parameters
    ----------
    function : function
        The function for which the interval will be searched.
    delta : numeric
        The step to use in each iteration.
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
    current_x = x0
    next_x = x0 + side*delta
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
    
    # IF side is -1 then next_x < current_x
    if side == -1:
        return next_x, current_x
    else:
        return current_x, next_x


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

def regula_falsi(function, left_point, right_point, max_iterations, error):
    """
    Find a root for the function in the interval [left_point, right_point]
    using regula falsi method.
    
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
    l = left_point; r = right_point; 
    f_l = function(l); f_r = function(r); 

    # Find the middle point of the line
    last_mid = (l * f_r - r * f_l) / (f_r - f_l) 
    f_last = function(last_mid)
    ########################################################
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
    mid = (l * f_r - r * f_l) / (f_r - f_l) 
    f_mid = function(mid)
    iterations = 1
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
        mid = (l * f_r - r * f_l) / (f_r - f_l)
        f_mid = function(mid)
        iterations += 1   
    
    return mid

def fixed_point(function, initial_approximation, max_iterations, error):
    """
    Find a fixed point for the function.
    
    Parameters
    ----------
    function : function
        The function to find the root.
    initial_approximation : numeric
        The value to start the method.
    max_iterations: int
        Maximum number of iterations before stopping the process.
    error : numeric
        The absolute error for the bisection. This is used to stop the
        method. The method stops when abs(x_n - x_n-1) < error. Where
        x_n are the sequence of point created trought the process.
        
    Returns
    -------
    numeric
        An approximate value x. For which f(x) = x (x is a fixed point).
    """

    # Set the first and second value for the process
    last_x = initial_approximation
    current_x = function(last_x)
    #######################################################
    print('Iteration    |    x    |    f(x)    |    Error  ')
    #######################################################
    iterations = 0
    ########################################################
    print('    %d      %.7f      %.7f      -' % (iterations,initial_approximation,current_x))
    #######################################################
    iterations = 1
    while abs(current_x - last_x) >= error:
        
        if iterations > max_iterations:
            return current_x
        last_x = current_x
        # Get the next value
        current_x = function(last_x)
        #######################################################    
        print('    %d      %.7f      %.7f      %.7f' % (iterations,last_x,current_x,abs(current_x - last_x)))
        #######################################################
        iterations += 1
    
    return current_x

def newton_raphson(function, derivate, initial_approximation, max_iterations, 
                   error):
    """
    Find a root for the function.
    
    Parameters
    ----------
    function : function
        The function to find the root.
    derivate : function
        The derivate of the function.
    initial_approximation : numeric
        The value to start the method.
    max_iterations: int
        Maximum number of iterations before stopping the process.
    error : numeric
        The absolute error for the bisection. This is used to stop the
        method. The method stops when abs(x_n - x_n-1) < error. Where
        x_n are the sequence of point created trought the process.
        
    Returns
    -------
    numeric
        An approximate value x. For which f(x) = 0 (x is a root).
    """
    # Set the first and second value for the process
    last_x = initial_approximation
    current_x = last_x - (function(last_x)/derivate(last_x))
    #######################################################
    print('Iteration    |    x    |    f(x)    |    Error  ')
    #######################################################
    iterations = 0
    ########################################################
    print('    %d      %.7f      %.7f      -' % (iterations,initial_approximation,current_x))
    #######################################################
    iterations = 1
    while abs(current_x - last_x) >= error:
        if iterations > max_iterations:
            return current_x
        last_x = current_x
        # Get the next value
        current_x = last_x - (function(last_x)/derivate(last_x))
        #######################################################    
        print('    %d      %.7f      %.7f      %.7f' % (iterations,last_x,current_x,abs(current_x - last_x)))
        #######################################################
        iterations += 1
    
    print(iterations)
    return current_x


def secant(function, initial_approximation_1, initial_approximation_2, 
           max_iterations, error):
    """
    Find a root for the function.
    
    Parameters
    ----------
    function : function
        The function to find the root.
    initial_approximation_1 : numeric
        The first value to start the method.
    initial_approximation_2 : numeric
        The second value to start the method.
    max_iterations: int
        Maximum number of iterations before stopping the process.
    error : numeric
        The absolute error for the bisection. This is used to stop the
        method. The method stops when abs(x_n - x_n-1) < error. Where
        x_n are the sequence of point created trought the process.
        
    Returns
    -------
    numeric
        An approximate value x. For which f(x) = 0 (x is a root).
    """
    # Set the first and second value for the process
    last_x = initial_approximation_1
    mid_x = initial_approximation_2
    iterations = 0
    print('Iteration |     x     |      f(x)      |     Error    ')
    print('    %d       %.7f      %.7f         -' % (iterations,last_x, function(last_x)))
    iterations += 1
    print('    %d       %.7f      %.7f         -' % (iterations,mid_x, function(last_x)))
    den = (function(mid_x)*(mid_x-last_x))/(function(mid_x) - function(last_x))
    current_x = mid_x - den
    abs_error = abs(current_x - mid_x)
    iterations += 1
    print('    %d       %.7f      %.7f      %.7f' % (iterations, current_x, 
                                                   function(current_x),abs_error))
    while abs(current_x - mid_x) >= error:
        if iterations > max_iterations:
            return current_x
        last_x = mid_x
        mid_x = current_x
        # Get the next value
        den = (function(mid_x)*(mid_x-last_x))/(function(mid_x) - function(last_x))
        current_x = mid_x - den
        iterations += 1
        abs_error = abs(current_x - mid_x)
        print('    %d       %.7f      %.7f      %.7f' % (iterations, current_x, 
                                                        function(current_x),abs_error))
    
    return current_x


def multiple_roots(function, first_derivative, second_derivative, 
                   initial_approximation, max_iterations, error):
    
    # Set the first and second value for the process
    last_x = initial_approximation
    
    iterations = 0
    print('Iteration |     x     |     f(x)     |     Error    ')
    print('    %d       %.7f      %.7f         -' % (iterations,last_x, function(last_x)))
    
    num = function(last_x)*first_derivative(last_x)
    den = (first_derivative(last_x)**2) - function(last_x)*second_derivative(last_x)
    fact = num/den
    current_x = last_x - fact
    iterations = 1
    abs_error = abs(current_x - last_x)
    print('    %d      %.7f      %.7f      %.7f' % (iterations, current_x, 
                                                   function(current_x),abs_error))
    while abs(current_x - last_x) >= error:
        if iterations > max_iterations:
            return current_x
        last_x = current_x
        # Get the next value
        num = function(last_x)*first_derivative(last_x)
        den = (first_derivative(last_x)**2) - function(last_x)*second_derivative(last_x)
        
        fact = num/den
        current_x = last_x - fact
        iterations += 1
        abs_error = abs(current_x - last_x)
        print('    %d      %.7f      %.7f      %.7f' % (iterations, current_x, 
                                                    function(current_x),abs_error))

    return current_x


def f_x(x):
    return math.log(math.sin(x)**2 + 1) - 1/2

def f_x_d(x):
    return 2*((math.sin(x)**2 + 1)**-1)*math.sin(x)*math.cos(x)

def f1_x(x):
    return math.log(math.sin(x)**2 + 1) - (1/2) - x

def g_x(x):
    return math.log(math.sin(x)**2 + 1) - (1/2)

def h_x(x):
    return math.exp(x) - x - 1

def h_x_d(x):
    return math.exp(x) - 1

def h_x_d2(x):
    return math.exp(x)

# Verification Zone

def incremental_search_verif():
    tol = 1e-7
    N = 100
    print(incremental_search(f_x, 0.5, -3, N, 1))
    
def bisection_verif():
    tol = 1e-7
    N = 100
    print(bisection(f_x, 0, 1, N, tol))
    
def regula_falsi_verif():
    tol = 1e-7
    N = 100
    print(regula_falsi(f_x, 0, 1, N, tol))

def newton_verif():
    tol = 1e-7
    N = 100
    x_0 = 0.5
    print(newton_raphson(f_x, f_x_d, x_0, N, tol))
    
def fixed_point_verif():
    x_0 = -0.5
    tol = 1e-7
    N = 100
    print(fixed_point(g_x, x_0, N, tol))
    
def multiple_roots_verif():
    tol = 1e-7
    N = 100
    print(multiple_roots(h_x, h_x_d, h_x_d2, 1, N, tol))
    
def secant_verif():
    tol = 1e-7
    N = 100
    print(secant(f_x, 0.5, 1, N, tol))
    