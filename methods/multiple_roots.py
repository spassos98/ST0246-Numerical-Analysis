"""
Created on Sun Sep  8 20:11:38 2019
Implementation of secant method.

@author: Santiago Passos & Alejandro Rojas
"""

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
