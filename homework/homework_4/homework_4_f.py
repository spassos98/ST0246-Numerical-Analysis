#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:11:38 2019

@author: yoksil
"""

import math


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
    # Set the left, right, and mid point and their respective values
    l = left_point; r = right_point; last_mid = (l + r)/2
    f_l = function(l); f_r = function(r); f_last = function(last_mid)
    
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
        
        # Update the last mid point
        last_mid = mid
        f_last = f_mid
        # Calculate and evaluate the new mid point
        mid = (r+l)/2
        f_mid = function(mid)
        iterations += 1
    
    print(f'Iterations : {iterations}')
    return mid

def bisection_relative(function, left_point, right_point, max_iterations, 
                       error):
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
        method. The method stops when abs(x_n - x_n-1)/x_n < error. Where
        x_n are the sequence of mid point created trought the process.
    
    Returns
    -------
    numeric
        An approximate value for which the function is zero.
    """
    # Set the left, right, and mid point and their respective values
    l = left_point; r = right_point; last_mid = (l + r)/2
    f_l = function(l); f_r = function(r); f_last = function(last_mid)
    
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
    iterations = 1
    while((abs(f_mid - f_last)/f_mid) >= error):
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
        
        # Update the last mid point
        last_mid = mid
        f_last = f_mid
        # Calculate and evaluate the new mid point
        mid = (r+l)/2
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

    iterations = 1
    while abs(current_x - last_x) >= error:
        if iterations > max_iterations:
            return current_x
        last_x = current_x
        # Get the next value
        current_x = function(last_x)
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

    iterations = 1
    while abs(current_x - last_x) >= error:
        if iterations > max_iterations:
            return current_x
        last_x = current_x
        # Get the next value
        current_x = last_x - (function(last_x)/derivate(last_x))
        iterations += 1
    
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
    den = (function(mid_x)*(mid_x-last_x))/(function(mid_x) - function(last_x))
    current_x = mid_x - den

    iterations = 1
    while abs(current_x - mid_x) >= error:
        if iterations > max_iterations:
            return current_x
        last_x = mid_x
        mid_x = current_x
        # Get the next value
        den = (function(mid_x)*(mid_x-last_x))/(function(mid_x) - function(last_x))
        current_x = mid_x - den
        iterations += 1
    
    print(f'Iterations : {iterations}')
    return current_x

def fcn_10_1(x):
    return math.log(x**2 + 1) + x*math.cos(6*x + 3) - 3*x - 10

def excercise_10_1():
    error = 5e-8
    # Root between -3.7 and -3,6
    a,b = incremental_search(fcn_10_1, 0.01, -3.7, 1000, side=1)
    print(f'[{a},{b}]')
    sol = bisection_relative(fcn_10_1, a, b, 1000, error)
    print(sol)
    print(fcn_10_1(sol))
    
    # Root between -3.6 and -3,5
    a,b = incremental_search(fcn_10_1, 0.01, -3.6, 1000, side=1)
    
    print(f'[{a},{b}]')
    sol = bisection_relative(fcn_10_1, a, b, 1000, error)
    print(sol)
    print(fcn_10_1(sol))
    
    # Root between -2.9 and -2.8
    a,b = incremental_search(fcn_10_1, 0.01, -2.9, 1000, side=1)
    
    print(f'[{a},{b}]')
    sol = bisection_relative(fcn_10_1, a, b, 1000, error)
    print(sol)
    print(fcn_10_1(sol))
    
    
    # Root between -2.2 and -2.1
    a,b = incremental_search(fcn_10_1, 0.01, -2.2, 1000, side=1)
    
    print(f'[{a},{b}]')
    sol = bisection_relative(fcn_10_1, a, b, 1000, error)
    print(sol)
    print(fcn_10_1(sol))
    
    # Root between -2.1 and -2.0
    a,b = incremental_search(fcn_10_1, 0.01, -2.1, 1000, side=1)
    
    print(f'[{a},{b}]')
    sol = bisection_relative(fcn_10_1, a, b, 1000, error)
    print(sol)
    print(fcn_10_1(sol))


def fcn_10_2(x):
    return math.exp(-x*x + 1) + x*math.sin(x-3) - x

    
def excercise_10_2():
    error = 1e-7
    # Root from -15
    a,b = incremental_search(fcn_10_2, 0.01, -15, 10000, side=1)
    print(f'[{a},{b}]')
    
    sol = bisection(fcn_10_2, a, b, 1000, error)
    sol = secant(fcn_10_2, (b+a)/3, (b+a)/2, 1000, error)
    print(sol)
    
    # Root from 1
    a,b = incremental_search(fcn_10_2, 0.0001, 1, 10000, side=1)
        
    sol = bisection(fcn_10_2, a, b, 1000, 1e-8)
    print(sol)
    
    # Root from 5
    a,b = incremental_search(fcn_10_2, 0.001, 5, 1000, side=1)
 
def fcn_10_4(x):
    return math.sqrt(x*x + 1) - 5*x*math.exp(-1*x) -4*x*x + 31*x+ 12


def excercise_10_4():
    # Root from -2 to -1
    a,b = incremental_search(fcn_10_4, 0.001, -2, 10000, side=1)
            
    sol = bisection(fcn_10_4, a, b, 1000, 1e-8)
    print(a,b,sol)
    
    # Root from -1 to 9
    a,b = incremental_search(fcn_10_4, 0.001, -1, 10000, side=1)
            
    sol = bisection(fcn_10_4, a, b, 1000, 1e-8)
    print(a,b,sol)
    
    # Root from 8 to 9
    a,b = incremental_search(fcn_10_4, 0.001, 8, 10000, side=1)
            
    sol = bisection(fcn_10_4, a, b, 1000, 1e-8)
    print(a,b,sol)


def fcn_10_5(x):
    return math.tanh(x) - x**2 - 0.22

def exercise_10_5():
    # Root from 0 to 1
    a,b = incremental_search(fcn_10_5, 0.001, 0, 10000, side=1)
    
    sol = bisection(fcn_10_5, a, b, 1000, 0.5e-9)
    print(a,b,sol)
    

def fcn_10_7(x):
    return math.exp(1) - x + 95 - 2*math.tanh(x) - 5


def exercise_10_7():
    # Root from 80 to 100
    a,b = incremental_search(fcn_10_7, 0.1, 80, 10000, side=1)
    # Use the new interval to imporve the search interval
    a,b = incremental_search(fcn_10_7, 0.001, a, 10000, side=1)
    
    sol = bisection(fcn_10_7, a, b, 1000, 0.5e-9)
    print(sol)
    
def exercise_1():
    fun_1 = lambda x: exp(x+3) + (pow(x,3)/3) - 10
    error = 1e-06
    left_num = -1
    right_num = 0
    max_iterations = 10000
    root = bisection(fun_1, left_num, right_num, max_iterations, error)
    print('root found {0}'.format(root))
    
def exercise_10_3():
    fun_10_3 = lambda x: exp(-1*pow(x,2) + 4) + 3*x*math.cos(x - 3) - 2*x + 16
    
    # We obtain the 2 intervals, both x0 were obtained from the graphic
    max_neg_interval = incremental_search(fun_10_3,0.001,-25,10000,1)
    min_pos_interval = incremental_search(fun_10_3,0.001,0,10000,1)
    
    
    # We obtain the roots from the intervals
    min_neg_root = bisection(fun_10_3,max_neg_interval[0],max_neg_interval[1], 
                             10000, 1e-08)
    
    max_pos_root = bisection(fun_10_3,min_pos_interval[0],min_pos_interval[1], 
                             10000, 1e-08)
    print('intervals found \n [ {0} , {1}] \n [ {2}, {3}]'.format(
            max_neg_interval[0], max_neg_interval[1], min_pos_interval[0],
            min_pos_interval[1]))
    
    print('min negative root = {0} \n max positive root = {1}'.format(
            min_neg_root, max_pos_root))

def exercise_10_6():
    fun_10_6 = lambda x: x - x*math.tan(x)
    max_iter = 10000
    error = 0.5*1e-09
    ro = 9
    # From the graphic method, 10 roots were found.
    list_of_starting_points = [0,2.5,5,10,11,15,19,22,25,28]
    
    for point in list_of_starting_points:
        # We get the interval
        interval = incremental_search(fun_10_6,0.001,point,max_iter)
        root = bisection(fun_10_6, interval[0],interval[1],max_iter, error)
        
        print('starting point = {0} \n interval found = [{1}, {2}] \n root = {3}'.format(
                point,round(interval[0],ro),round(interval[1],ro),round(root,ro)))
        
  