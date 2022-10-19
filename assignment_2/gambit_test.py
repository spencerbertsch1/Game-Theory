"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #2 - Problem #1) 2-Person Zero Sum Games

The goal of this script is to test the solutions given by my own code against those given by 
Gambit for one hundred randomly generated matrices. 

This script can be run at the command line by running the following: $ python3 gambit_test.py
"""

# imports 
import statistics
import numpy as np
from itertools import combinations
from numpy.linalg import inv
import random

# local imports 
from routines import matrix_generator
from zero_sum import ZeroSum

def gambit_matrix_test():
    """
    Test one hundred randomly generated matrices to see if my solution matches that of Gambit 
    """

    for i in range(1, 101, 1):
        mat: np.array = matrix_generator()
        # create a 2 player game object and pass in the randomly generated matrix 
        game = ZeroSum(payoff_matrix=mat, VERBOSE=False)
        # now we can use simplex to solve the game 
        solution_dict: dict = game.method_seven(A=mat)
        p_simplex = solution_dict['p']
        q_simplex = solution_dict['q']
        v_simplex = solution_dict['v']

        # now we need to find the same solutions using Gambit
        v_gambit = 0.0

        # finally, we compare the solutions
        v_simplex_round = v_simplex.round(1)
        v_gambit = v_gambit.round(1)

        if v_simplex == v_gambit:
            print(f'Our solution matches Gambit for matrix #{i}, continuing to the next matrix.')
        else:
            print(f'Solutions do not match for matrix #{i}: Our game value: {v_simplex}, Gambit\'s game value: {v_gambit}')

if __name__ == "__main__":
    gambit_matrix_test()