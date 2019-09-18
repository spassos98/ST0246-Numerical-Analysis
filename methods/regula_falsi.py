"""
Created on Sun Sep  8 20:11:38 2019
Implementation of regula falsi method.
https://en.wikipedia.org/wiki/Regula_falsi

@author: Santiago Passos & Alejandro Rojas
"""
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
