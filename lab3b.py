#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
#  Author ID: rkhan2


def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    return number1 + number2
    
def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
  return number1 - number2
        
def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return number1 * number2

import lab3b

if __name__ == '__main__':
    print(str(lab3b.sum_numbers(10, 5)))
    add = lab3b.sum_numbers
    print(str(lab3b.subtract_numbers(10, 5)))
    print(str(lab3b.multiply_numbers(10, 5)))
