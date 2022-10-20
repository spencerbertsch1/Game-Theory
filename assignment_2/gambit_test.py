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
import pygambit

# local imports 
from routines import matrix_generator
from zero_sum import ZeroSum


def get_gambit_strategies(A: np.array):
    """
    Helper function used to generate strategies of a matrix using Gambit 
    """
    # first we need to change the data type
    A = A.astype(pygambit.Rational)

    # PROBLEM - All specified arrays must have the same shape
    g = pygambit.Game.from_arrays(A, np.transpose(A))

    # get the mixed strategy profiles 
    p = g.mixed_strategy_profile()

    # get the p vector 
    p_vec = p[g.players[0]]
    # get the q vector 
    q_vec = p[g.players[1]]

    print(f'p: {p_vec}, q: {q_vec}')

    p[g.players[0].strategies[0]]


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
    # gambit_matrix_test()

    get_gambit_strategies(A=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
