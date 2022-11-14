"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #4 - Problem #2(b) Bimatrix TU Games

The goal of this problem is to solve any 2x2 TU game. 
The steps of finding the solution to any 2x2 TU game are as foloows: 

1. Find sigma (the total payoff) using the following expression: sigma = MAX(a_ij + b_ij)
2. Find delta using the following expression: delta = val(A - B)
    Here (A-B) represents the matrix that we get if we subtract all P1 payoffs from P2 payoffs (a_ij - b_ij)
3. Find phi (the payoff split) using the following expression: ((sigma + delta)/2, (sigma - delta)/2)
4. And we're done! Now we just log the total payoff (sigma) and the payoff split (phi). 

This script can be run at the command line by running the following: $ python3 bimatrix_tu_game.py
"""

# imports 
import numpy as np
import random

# local imports 
from tu_games import BimatrixGames
from zero_sum import ZeroSum


def pretty_print_solution(sigma: int, phi: tuple, bimatrix: list[np.array, np.array], VERBOSE: bool):
    """
    Simple function to pretty print the solution of the bimatrix TU game 
    """
    s = '-'*25
    if VERBOSE:
        print(f'Original Bimatrix:')
        for i, mat in enumerate(bimatrix):
            print(f'Payoff matrix for P{i}: \n {mat}')
    else:
        print(f'Shape of randomly generated Bimatrix: {bimatrix[0].shape}')
    print(f'SOLUTION: \n {s} \n Total Payoff Sigma: {sigma} \n Payoff Split Phi: {phi} \n {s}')


def solve_bimatrix(bimatrix: list[np.array, np.array], VERBOSE: bool):
    """
    Function to solve bimatrix games given a list of 2 numpy arrays

    :params: bimatrix - list containing two 2x2 np arrays that each represent the payoffs for P1 and P2
    :return: NA - the solution is printed, nothing needs to be returned here. 
    """
    
    # 1. Find sigma (the total payoff) using the following expression: sigma = MAX(a_ij + b_ij)
    mat_sum: np.array = bimatrix[0] + bimatrix[1]
    sigma: int = np.max(mat_sum)
   
    # 2. Find delta using the following expression: delta = val(A - B)
        # Here (A-B) represents the matrix that we get if we subtract all P1 payoffs from P2 payoffs (a_ij - b_ij)
    a_minus_b: np.array = bimatrix[0] - bimatrix[1]
    # here we can use our simplex method implementation from PSET 2 to get the value of this resulting 2x2 matrix 
    game = ZeroSum(payoff_matrix=a_minus_b)
    game_dict = game.method_seven(A=a_minus_b)
    delta = round(game_dict['v'], 3)

    # 3. Find phi (the payoff split) using the following expression: ((sigma + delta)/2, (sigma - delta)/2)
    phi: tuple = ((sigma + delta)/2, (sigma - delta)/2)

    # 4. And we're done! Now we just log the total payoff (sigma) and the payoff split (phi). 
    pretty_print_solution(sigma=sigma, phi=phi, bimatrix=bimatrix, VERBOSE=VERBOSE)


def main(VERBOSE: bool):

    # define the game to solve
    bimatrix = BimatrixGames.mat3

    # pass the bimatrix into the solve function
    solve_bimatrix(bimatrix=bimatrix, VERBOSE=VERBOSE)


def bimatrix_generator():
    """
    Utility function to generate numpy bimatrices with the following specifications: 

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
    mat1 = np.zeros((m, n))
    mat2 = np.zeros((m, n))

    # now we fill the matrix with random values chosen from the element_list
    for i in range(m): 
        for j in range(n):
            mat1[i, j] = random.choice(element_list)
            mat2[i, j] = random.choice(element_list)
    
    return [mat1, mat2]


def generator_test(VERBOSE: bool, num_test_matrices: int):
    """
    Function to test a few random matrices and see the solutions for each of the bimatrix games
    """

    for i in range(num_test_matrices):
        # use the matrix generator funciton to define a random bimatrix 
        bimatrix = bimatrix_generator()

        solve_bimatrix(bimatrix=bimatrix, VERBOSE=VERBOSE)
        print('\n')

if __name__ == "__main__":

    # main function that tests individual matrices from the tu_games.py file 
    main(VERBOSE=True)
    print('\n\n')

    # function that shows outputs for the randomly generated matrices 
    generator_test(VERBOSE=False, num_test_matrices=3)
