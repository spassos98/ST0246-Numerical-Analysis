"""
Created on Sun Sep  8 20:11:38 2019
Implementation of secant method.
https://en.wikipedia.org/wiki/Secant_method

@author: Santiago Passos & Alejandro Rojas
"""

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
