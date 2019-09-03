#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Alejandro Rojas & Santiago Passos
"""

import numpy as np

def function_3d(point):
    """
    A function in R3
    
    Parameters
    ----------
    point : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    
    Returns
    -------
    numeric
        The value of the function for that point.
    """
    return point[0]**2 + point[1]**2 + point[2]**2 - 1


def line_param(point_a, point_b, t):
    """
    Given two point in R3 and a real number. This functions returns a point
    that is on the line that passes trough a and b. Let x be a point in that
    line, then: x = point_b + t(point_a - point_b). Where t is a real number.
    With this parametrization we can represent any number in the line by
    just changing the value of t.
    
    Parameters
    ----------
    point_a : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    point_b : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    t : numeric
        The value to consider in the parametrization.
    
    Returns
    -------
    ndarray
        The point that representesthe given value for the parametrization.
    """
    new_point = point_a - point_b
    return point_b + t*new_point


def bisection_3d(function, point_a, point_b, tol, max_iterations):
    """
    Given a function in R3 and two points in R3 representing a line and the
    there exist a point between that to points for which the function is zero.
    This function find that point.
    
    Parameters
    ----------
    function : function
        A function which recieves a (3,) or (3,1) shaped numpy array, 
        representing a curve in the space.
    point_a : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    point_b : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    step : numeric
        The step that will be used in the incremental search process.
    tol : numeric
        A tolerance value for the approximation.
    max_interations : int
        Maximum number of iteration to get the solution. If no solution is 
        found then the process is terminated.
    
    Returns
    -------
    ndarray
        A point for which the function is zero.
    """
    # We are going to use a parametrization for the line between point_a and
    # point_b. In this case all the point between a and b can be represented
    # as: x = point_b + t(point_a - point_b), where t in a Real number. For
    # 0 <= t <=1 we get all the points between a and b.
    # This is why the first value for the ends int the bisection are 0 and 1.
    l = 0; r = 1
    mid = (l+r)/2

    # Evaluate the function in the left and mid point
    f_l = function( line_param(point_a, point_b, l) )
    f_r = function( line_param(point_a, point_b, r) )
    f_mid = function( line_param(point_a, point_b, mid) )

    # Check if cright end of the interval is zero
    if abs(f_r) < tol:
        return line_param(point_a, point_b, r)

    # Check if the function evaluated in the right end of the interval is zero
    if abs(f_r) < tol:
        return line_param(point_a, point_b, l)
    
    iterations = 0
    # While the value for the mid point is not zero
    while(abs(f_mid) >= tol):
        if iterations > max_iterations:
            break
        # If the change of sign is on the left side then the new right point
        # is the mid point.
        if f_l*f_mid <=0:
            r = mid
        # If the change of sign is on the right side then the new left point
        # is the mid point.
        else:
            l = mid
            f_l = function( line_param(point_a, point_b, l) )
        
        # Calculate and evaluate the new mid point
        mid = (r+l)/2
        f_mid = function( line_param(point_a, point_b, mid) )
        iterations += 1
        
    return line_param(point_a, point_b, mid)


def search_interval_3d(function, point_a, point_b, step, tol, max_iterations):
    """
    Given a function in R3 and two points in R3 representing a line, this 
    function returns two points in that line representing an interval where
    the function is zero.
    
    Parameters
    ----------
    function : function
        A function which recieves a (3,) or (3,1) shaped numpy array, 
        representing a curve in the space.
    point_a : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    point_b : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    step : numeric
        The step that will be used in the incremental search process.
    tol : numeric
        A tolerance value for the approximation.
    max_interations : int
        Maximum number of iteration to get the solution. If no solution is 
        found then the process is terminated.
    
    Returns
    -------
    ndarray
        A point for which the function is zero.
    """
    # The first interval is created with the values [0, step]
    t = step
    # We use a parametrization for the line based on the two points given.
    # It is possible to get all point in the line changing the parameters t.
    # For t=0 we get the point_b and for t=1 we get the point_a.
    last_val = function( line_param(point_a, point_b, 0) )
    current_val = function( line_param(point_a, point_b, t) )
    
    # While the signs of the function evaluated in the ends of the interval is
    # the same.
    iterations = 0
    while last_val*current_val > 0:
        if iterations > max_iterations:
            raise Exception('Maximum iterations reached. But no solution was found.')
        # Update the step
        last_val = current_val
        t += step
        # Calculate the new value
        current_val = function( line_param(point_a, point_b, t) )
        iterations += 1
    
    # These point represent the interval for which a change is the signs exist.
    # This means that there is a point in this interval for which the function
    # is zero. We use bisection in this interval to find that point.
    left_point = line_param(point_a, point_b, t - step)
    right_point = line_param(point_a, point_b, t)
    
    return left_point, right_point


def find_root(function, point_a, point_b, step, tol, max_iterations):
    """
    Given a function in R3 and two points in R3 representing a line, this 
    function find (if exists) a point in that line for which the 
    function is zero.
    
    Parameters
    ----------
    function : function
        A function which recieves a (3,) or (3,1) shaped numpy array, 
        representing a curve in the space.
    point_a : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    point_b : ndarray
        A point in the space represented by a (3,) or (3,1) shaped numpy array.
    step : numeric
        The step that will be used in the incremental search process.
    tol : numeric
        A tolerance value for the approximation.
    max_interations : int
        Maximum number of iteration to get the solution. If no solution is 
        found then the process is terminated.
    
    Returns
    -------
    ndarray
        A point for which the function is zero.
    """
    left_point , right_point = search_interval_3d(function, point_a, point_b, 
                                                  step, tol, max_iterations)
    
    point_where_zero = bisection_3d(function, left_point, right_point, tol, 
                                    max_iterations)
    
    return point_where_zero


if __name__ == '__main__':
    a = np.array([1.5, 0, 0])
    b = np.array([-1.5, 0, 0])
    tol = 1e-10
    max_iter = 1000
    step  = 0.1
    root = find_root(function_3d, a, b, step, tol, max_iter)
    print(list(root))
    print(function_3d(root))
