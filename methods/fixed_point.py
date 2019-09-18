"""
Created on Sun Sep  8 20:11:38 2019
Implementation of fixed_point iteration.
https://en.wikipedia.org/wiki/Fixed-point_iteration

@author: Santiago Passos & Alejandro Rojas
"""

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

