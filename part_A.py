# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:43:56 2024

@author: hmwas

TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.



PART1: USING SOLELY FOR LOOPS, COLLEAGUES SUGGESTION

"""
import math

def std_loops(x):
    num_lst = [1,2,3,4,5]
    
    x = num_lst
    
    N = len(x)
    
    tot_sum = 0
#Compute the mean, use += instead of sum function. 
    
    for num1 in x:
        
        tot_sum += num1
    
    mean1 = tot_sum / N
    
#Compute the mean of squares

#Create an empty list and create a new variable for the squared list 
#Append the squared list to the empty list and use += to get the sum of this list in a new variable.
    emp_list = [ ]

    for num2 in x:
        sqr1 = num2**2
        
        emp_list.append(sqr1)
        
        sum_sqr = 0
        for num3 in emp_list:
            
            sum_sqr += num3
#Divide this by the number of items in the list to get the mean of squares

    s = sum_sqr / N
    
#Compute the squared standard deviation by subtracting the squared mean from the mean of squares.
    Std_sqr = s - (mean1**2)
    
#Compute the square root of this new variable to get the standard deviation

    from math import sqrt
    Std = sqrt(Std_sqr)
    
    return Std
            
    
"""

PART 2: USE LEN AND SUM FUNCTION, BOSS'S SUGGESTION

"""


def std_builtin(x):
    
    
#Compute the mean

    num_lst = [1,2,3,4,5]
    
    x = num_lst


    N = len(x)


    mean2 = (1/N) * sum(x)

#Compute the sum of squares

#Create an empty list we can append the squares of the values
    sqr_lst = [ ]

#Append the squares to a new list
    for i in x:
        sqr = (i**2)
    
        sqr_lst.append(sqr)
   
#Compute the sum of squares by the formula: Use sum function to get the sum of the squared list.

    S = (1/N) * sum(sqr_lst)

#Compute the variance Sd_sqr = S - (mean1)^2 

    Sd_sqr = S - (mean2**2)

    from math import sqrt

    Sd = sqrt(Sd_sqr)
 
    return Sd


"""

PART 3: USE NUMPY FUNCTION, MY SUGGESTION

"""

import numpy 

from numpy import std

def std_numpy(x):
    num_lst = [1,2,3,4,5]

    x = num_lst
    
    std(x)
    
    return std(x)





