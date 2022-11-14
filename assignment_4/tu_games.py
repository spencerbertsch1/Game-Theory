"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #4 - Problem #2(b) Bimatrix TU Games

This script holds a few examples of bimatrix TU games. 

These matrices should be imported and solved by the bimatrix_tu_game.py script. 
"""

# imports
import numpy as np

class BimatrixGames():

    # game #1
    P1_matrix_1 = np.array([[0, 3], [4, 2]])
    P2_matrix_1 = np.array([[4, 2], [0, 3]])
    mat1 = [P1_matrix_1, P2_matrix_1]

    # game #2
    P1_matrix_2 = np.array([[3, 1], [0, 2]])
    P2_matrix_2 = np.array([[1, 2], [3, 0]])
    mat2 = [P1_matrix_2, P2_matrix_2]

    # game #3
    P1_matrix_3 = np.array([[1, 2, 0], [4, 1, 2], [5, 2, 0]])
    P2_matrix_3 = np.array([[5, 2, 1], [2, 0, 1], [0, 3, 0]])
    mat3 = [P1_matrix_3, P2_matrix_3]




