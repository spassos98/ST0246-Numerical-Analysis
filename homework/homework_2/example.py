#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Author: Santiago Passos & Alejandro Rojas
"""

import Binary_machine as bm

if __name__ == '__main__':
    # Create a machine of 32 bits. 23 for the mantissa and 7 for the exponent
    maquinita = bm.Binary_machine(23, 7)
    greatest_number = maquinita.greatest_number()
    smallest_number = maquinita.smallest_number()
    epsilon = maquinita.machine_epsilon()
    
    print('Greatest number: %s' % greatest_number)
    print('Smallest number: %s' % smallest_number)
    print('Machine Epsilon: %s' % epsilon)
    
    print('')
    print('-------------------------------------------------------------')
    print('')
    
    # Numbers to view in the machine
    list_of_numbers = [33.5869, 4.56835]
    for i in list_of_numbers:
        original_value = i
        machine_representation = maquinita.dec_to_machine(original_value)
        decimal_representation = float(maquinita.machine_to_dec(
                machine_representation))
        
    
        print('Original value: %s' % original_value)
        print('Machine representation: %s' % machine_representation)
        print('Decimal representation: %s' % decimal_representation)

    
        print('')
        absolute_error = abs(original_value -  decimal_representation)
        relative_error = (absolute_error)/original_value
        
        print('Absolute error: %.10f' % absolute_error)
        print('Relative error: %.10f' % relative_error)
    
        print('')
        print('-------------------------------------------------------------')
        print('')
    
    original_value = 33.5869
    second_value = 4.56835
    print('Numbers to operate {} and {}'.format(original_value, second_value))
    print('')
    print('-------------------------------------------------------------')
    print('')
    list_of_fun = [bm.aux_sum, bm.aux_subs, bm.aux_times]
    for f in list_of_fun:
        summ = maquinita.operate_two_decimals(original_value,
                                          second_value,
                                          f)
        summ_decimal_representation = float(maquinita.machine_to_dec(summ))
        original_summ = f(original_value, second_value)
        
        absolute_error_sum = abs(original_summ -  summ_decimal_representation)
        relative_error_sum = (absolute_error_sum)/original_summ
        
        print('Function %s' % f)
        print('Original value: %s' % original_summ)
        print('Machine representation: %s' % summ)
        print('Decimal representation: %s' % summ_decimal_representation)
    
        
        print('')
        
        print('Absolute error: %.10f' % absolute_error_sum)
        print('Relative error: %.10f' % relative_error_sum)
        
        print('')
        print('-------------------------------------------------------------')
        print('')
    
#    # Sum both numbers
#    summ = maquinita.operate_two_decimals(original_value,
#                                          second_value,
#                                          bm.aux_sum)
#    summ_decimal_representation = float(maquinita.machine_to_dec(summ))
#    original_summ = original_value + second_value
#    
#    absolute_error_sum = abs(original_summ -  summ_decimal_representation)
#    relative_error_sum = (absolute_error_sum)/original_summ
#    
#    print('Original sum value: %s' % original_summ)
#    print('Machine representation: %s' % machine_representation)
#    print('Decimal representation: %s' % decimal_representation)
#
#    
#    print('')
#
#    
#    print('Absolute error: %.10f' % absolute_error)
#    print('Relative error: %.10f' % relative_error)
#    
#    # Subs both numbers
#    subs = maquinita.operate_two_decimals(original_value,
#                                          second_value,
#                                          bm.aux_subs)
#    
#    subs_decimal_representation = float(maquinita.machine_to_dec(summ))
#    original_subs = original_value - second_value
#    
#    absolute_error_subs = abs(original_subs -  subs_decimal_representation)
#    relative_error_subs = (absolute_error_subs)/original_subs
#    
#    # First number times the second one
#    times = maquinita.operate_two_decimals(original_value,
#                                          second_value,
#                                          bm.aux_times)
#    times_decimal_representation = float(maquinita.machine_to_dec(summ))
#    original_times = original_value * second_value
#
#    absolute_error_times = abs(original_times -  times_decimal_representation)
#    relative_error_times = (absolute_error_times)/original_times   
