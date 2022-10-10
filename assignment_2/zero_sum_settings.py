"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #2 - Problem #1) 2-Person Zero Sum Games

This is a simple settings file that's designed to contain some hard coded payoff matrices. 

Later on the matrices will be generated using a function in the routines.py file for this problem. 
For any TAs or users who would like to add their own payoff matrices, feel free to do that here. 

"""

# imports 
import numpy as np

class PayoffMatrices():
    # define a simple example payoff matrix
    mat1 = np.array([[1, 2], [3, 4]])

    # define a non 2x2 matrix
    mat2 = np.array([[2, 3, 1, 5], [4, 1, 6, 0]])

    # define a matrix with a single saddle point
    mat3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
