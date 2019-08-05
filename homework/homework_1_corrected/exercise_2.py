#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Author: Santiago Passos & Alejandro Rojas
"""

import Binary_machine as bm

if __name__ == '__main__':
    # Create a machine of 32 bits. 23 for the mantissa and 7 for the exponent
    maquinita = bm.Binary_machine(23, 7)
    original_value = 0.8
    machine_representation = maquinita.dec_to_machine(original_value)
    decimal_representation = float(maquinita.machine_to_dec(machine_representation))
    
    print('Original value: %s' % original_value)
    print('Machine representation: %s' % machine_representation)
    print('Decimal representation: %s' % decimal_representation)
    
    print('')
    absolute_error = abs(original_value -  decimal_representation)
    relative_error = (absolute_error)/original_value
    
    print('Absolute error: %.10f' % absolute_error)
    print('Relative error: %.10f' % relative_error)
