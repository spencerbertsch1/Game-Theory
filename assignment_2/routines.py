"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #2 - Routines file 

The goal of this script is to store routine and utility functions for use in assignment #2. 

This script can be run at the command line by running the following: $ python3 routines.py
"""

# imports
import numpy as np
import random


def intersection(l1: tuple, l2: tuple):

    # define our 4 points that make up the 2 lines 
    p1 = l1[0]
    p2 = l1[1]
    p3 = l2[0]
    p4 = l2[1]

    # define all 8 values that make up the 2 lines
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    x4 = p4[0]
    y4 = p4[1]

    # according to en.wikipedia.org/wiki/Line%E2%80%93line_intersection, we can use the following expression
    if (((x1-x2)*(y3-y4)) -  ((y1-y2)*(x3-x4))) != 0:
        x_intercept = ((((x1*y2) - (y1*x2))*(x3-x4)) - ((x1-x2)*((x3*y4) - (y3*x4))))/(((x1-x2)*(y3-y4)) -  ((y1-y2)*(x3-x4)))

        y_intercept = ((((x1*y2) - (y1*x2))*(y3-y4)) - ((y1-y2)*((x3*y4) - (y3*x4))))/(((x1-x2)*(y3-y4)) -  ((y1-y2)*(x3-x4)))

        return [x_intercept, y_intercept]
    else:
        return ['parallel']


def matrix_generator():
    """
    Utility function to generate numpy matrices with the following specifications: 

    Random values of m rows where 1 <= m <= 100
    Random values of n columns where 1 <= n <= 100
    Random element values where -1000 <= a_ij <= 1000
    """
    row_col_list = [x for x in range(1, 101, 1)]
    element_list = [x for x in range(-1000, 1001, 1)]

    # randomly generate the dimensions of the matrix
    m = random.choice(row_col_list)
    n = random.choice(row_col_list)

    # create an empty numpy array filled with zeros 
    mat = np.zeros((m, n))

    # now we fill the matrix with random values chosen from the element_list
    for i in range(m): 
        for j in range(n):
            mat[i, j] = random.choice(element_list)
    
    return mat


# some test code
if __name__ == "__main__":
    m = matrix_generator()
    print(m.shape)