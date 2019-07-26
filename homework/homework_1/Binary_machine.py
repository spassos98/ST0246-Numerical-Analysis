#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Santiago Passos & Alejandro Rojas
"""

class Binary_machine:
    """
    Class to handle machine number representation, this is, convert from
    a real number to a machine number and vice versa.
    
    Attributes
    ----------
    mantissa_len : int
        The number of bits that the mantissa can store.
    exponent_bits : int
        The number of bits to represent the exponent in base 2.
    """
    mantissa_len = None
    exponent_bits = None
    # The order of the bits is the following
    # [mantissa sign bit] [exponent sign bit] [exponent] [mantissa]
    def __init__(self, mantissa_len=8, exponent_bits=4):
        self.mantissa_len = mantissa_len
        self.exponent_bits = exponent_bits
    
    def dec_to_bin(self, dec_num):
        """
        Get the binary representation of the integer an decimal part of a
        number.
        
        Parameters
        ----------
        dec_num : numeric
            Number to get integer and decimal part from.
            
        Returns
        -------
        tuple
            integer part, decimal part
        """
        # Get the interger and decimal part in decimal representation
        int_part, dec_part = split_number(dec_num)
        
        # Calculate the integer and decimal part in binary form
        int_part = int_to_base_k(int_part, 2)
        dec_part = dec_to_base_k(dec_part, 2, 
                                 self.mantissa_len + 2**(self.exponent_bits) 
                                 - 1)
        return (int_part, dec_part)


    def dec_to_machine(self, num):
        """
        Given a decimal number in base 10 it returns it representation as
        machine number using the exponent mantissa standard.
        
        Parameters
        ----------
        num : numeric
            Real number that will be represented as machine number.
            
        Returns
        -------
        str
            The machine representation of the given number.
        """
        # Get the binary representation of the number
        int_part, dec_part = self.dec_to_bin(num)
        mantissa_number = ''
        # 1 when the exponent sign is positive
        exponent_bit = '1'
        sign_bit = str(int((num>0)))
        # Exponent is positive when int part is greater than zero
        if int(int_part) != 0:
            exponent = int_to_base_k(len(int_part), 2)
            mantissa_number = int_part[1:] + dec_part
        else:
            exponent_bit = '0'
            exponent = 0
            for x in dec_part:
                if int(x) != 0:
                    break
                exponent += 1
            mantissa_number = dec_part[exponent+1:]
            exponent = int_to_base_k(exponent, 2)
        
        # Fill the mantissa number with zeros if necessary
        while len(mantissa_number) < self.mantissa_len:
                mantissa_number += '0'
        # Cut the mantisa number
        mantissa_number = mantissa_number[0:self.mantissa_len]
        
        # Fill the exponent with zeros if necessary
        while len(exponent) < self.exponent_bits:
            exponent = '0' + exponent
        
        # Get the last numbers in the exponent
        exponent = exponent[-self.exponent_bits:]
        
        machine_number = sign_bit + exponent_bit + exponent + mantissa_number
        return machine_number


    def machine_to_dec(self,machine_number):
        """
        Given a machine number it returns it representation in base 10.
        
        Parameters
        ----------
        num : numeric
            Machine number that will be represented as real number.
            
        Returns
        -------
        str
            The decimal representation of the given number.
        """
        machine_number = str(machine_number)
        sign_bit = machine_number[0]
        exponent_bit = machine_number[1]
        exponent = machine_number[2:2+self.exponent_bits]
        mantissa_number = '1' + machine_number[-self.mantissa_len:]
        
        # Get the exponent in base 10
        exponent = int(base_k_to_int(exponent, 2))
        
        int_part = None
        dec_part = None
        if exponent_bit == '0':
            # If the exponent sign is negative append zeros to the left of
            # the mantissa number
            for x in range(exponent):
                mantissa_number = '0' + mantissa_number
            # The int part is zero because it is a number of the form
            # 0.d1d2d3...
            int_part = '0'
            dec_part = mantissa_number
        else:
            # If the exponent sign is positive use the first numbers as the
            # integer part
            int_part = ''
            for x in range(exponent):
                if x < len(mantissa_number):
                    int_part += mantissa_number[x]
                else:
                    int_part += '0'
            
            if len(mantissa_number) > len(int_part):
                dec_part = mantissa_number[exponent:]
            else:
                dec_part = '0'
        
        # Get the integer and decimal part in base 10
        int_part = base_k_to_int(int_part, 2)
        dec_part = base_k_to_dec(dec_part, 2)
        
        base_10_number = int_part + '.' + dec_part
        if sign_bit == '0':
            base_10_number = '-' + base_10_number
        return base_10_number


def int_to_base_k(num, base):
    """
    Get the representation in base k of an integer in base 10.
    
    Parameters
    ----------
    num : int
        Integer to be converted to base k.
    base : int
        The base that will be used in the conversion.
        
    Returns
    -------
    str
        The representation in base k of the given number.
    """
    num = int(num)
    new_number = ''
    while num >= base:
        remainder = int(num%base)
        new_number += str(remainder)
        num = int(num/base)
    new_number += str(num)
    return new_number[::-1]


def dec_to_base_k(dec, base, mantissa_len=40):
    """
    Get the representation in base k of an decimal number (0.d1d2d3..) 
    in base 10.
    
    Parameters
    ----------
    num : int
        Integer to be converted to base k. Note that if you want to convert,
        for example, 0.234 you should pass it as 234.
    base : int
        The base that will be used in the conversion.
        
    Returns
    -------
    str
        The representation in base k of the given number.
    """
    dec = float('0.' + str(dec))
    new_number = ''
    i = 0
    # Multiply the number and get the int part, then continue to multiply
    # only the decimal part
    for i in range(mantissa_len+1):
        val = dec*base
        int_part = int(val)
        new_number += str(int_part)
        dec = val - int_part
    return  new_number

def base_k_to_int(num, base):
    """
    Get the representation in base 10 of an integer in base k.
    
    Parameters
    ----------
    num : int
        The  integer number in the given base.
    base : int
        The base that the number is in.

    Returns
    -------
    numeric
        The representation of the number in base 10.
    """
    str_num = str(num)
    base_10_num = 0
    exp = 0
    str_num = str_num[::-1]
    for val in str_num:
        base_10_num += int(val)*(base**exp)
        exp += 1
    return str(split_number(base_10_num)[0])


def base_k_to_dec(num, base):
    """
    Get the representation in base 10 of an decimal number (0.d1d2d3...) 
    in base k.
    
    Parameters
    ----------
    num : int
        The decimal number without the 0. For instance if you want to convert
        0.1110 in base 2, you should pass 1110
    base : int
        The base that the number is in.
        
    Returns
    -------
    numeric
        The representation of the number in base 10.
    """
    str_num = str(num)
    base_10_num = 0
    exp = -1
    for val in str_num:
        base_10_num += int(val)*(base**exp)
        exp -= 1
    return str(split_number(str(base_10_num))[1])
    

def split_number(num):
    """
    Split a number in the integer and decimal part.
    
    Parameters
    ----------
    num : numeric
        The number to be splitted.
        
    Returns
    -------
    tuple
        integer part, decimal part
    """
    str_num = str(num)
    # String to store the number
    temp = ''
    int_part = None
    dec_part = 0
    # All the numbers before a '.' area the int part, the numberse after
    # '.' are the decimal part
    for c in str_num:
        if c == '.':
            int_part = temp
            temp = ''
            continue
        temp += c
    if int_part == None:
        int_part = temp
    else: 
        dec_part = temp
        
    return int_part, dec_part

def real_to_base_k(num, k):
    """
    Convert a real number to its representation in base k.
    
    Parameters
    ----------
    num : numeric
        A real number.
    base : int
        The base that will be used in the conversion.
        
    Returns
    -------
    str
        The representation of the number in base k. 
    """
    # Split the number in the integer and decimal part
    int_part, dec_part = split_number(num)
    # Convert the integer and decimal part to the base k representation
    int_part = int_to_base_k(int_part, k)
    dec_part = dec_to_base_k(dec_part, k, 10)
    return int_part + '.' + dec_part


if __name__ == '__main__':
    # Create a machine of 32 bits. 23 for the mantissa and 7 for the exponent
    maquinita = Binary_machine(23, 7)
    #maquinita = Binary_machine()
    original_value = 0.1
    machine_representation = maquinita.dec_to_machine(original_value)
    decimal_representation = float(maquinita.machine_to_dec(machine_representation))
    
    print('Original value: %s' % original_value)
    print('Machine representation: %s' % machine_representation)
    print('Decimal representation: %s' % decimal_representation)
    
    print('')
    absolute_error = abs(original_value -  decimal_representation)
    relative_error = (absolute_error)/decimal_representation
    
    print('Absolute error: %.10f' % absolute_error)
    print('Relative error: %.10f' % relative_error)