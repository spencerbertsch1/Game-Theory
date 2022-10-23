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
    mat1 = np.array([[9, 2], [3, 5]])

    # define a non 2x2 matrix
    mat2 = np.array([[2, 3, 1, 5], [4, 1, 6, 0]])

    # define a matrix with a single saddle point
    mat3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # define 2x2 matrix with a saddle point
    mat4 = np.array([[1, 2], [3, 4]])

    # define a matrix that we can pair down to a 2x2 using dominant strategies
    mat5 = np.array([[2, 0], [1, 2], [4, 1]])

    # define a singular (non-invertible) matrix used to trick method 6
    mat6 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # add a matrix where v=0 to test method 6
    mat7 = np.array([[0, 1, -2], [1, -2, 3], [-2, 3, -4]])

    # another matrix to test method 6
    mat8 = np.array([[1, 7, 3], [13, 5, 6], [7, 8, 9]])

    # another matrix that's a good test for the simplex method 
    mat9 = np.array([[4, 1, 8], [2, 3, 1], [0, 4, 3]])

    # another matrix that's a good test for the simplex method 
    mat10 = np.array([[2, -1, 6], [0, 1, -1], [-2, 2, 1]])

    # another matrix that's a good test for the simplex method 
    mat11 = np.array([[0, 1, -2], [1, -2, 3], [-2, 3, -4]])

    # ---------- EXAMPLES FROM THE ASSIGNMENT -----------
    A_i = np.array([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]])
    A_ii = np.array([[1, -2, 3, -4], [0, 1, -2, 3], [0, 0, 1, -2], [0, 0, 0, 1]])
    A_iii = np.array([[1, 2, -1], [2, -1, 4], [-1, 4, -3]])
    A_iv = np.array([[0, 2, 1], [-2, 0, -4], [-1, 4, 0]])
    A_v = np.array([[10, 0, 7, 0], [0, 6, 4, 0], [0, 0, 3, 3]])
