"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #3 - Problem #1(b) Recursive Games

This script is just here to hold the game boards that will be solved in problem 1(b). 

This script can be run at the command line by running the following: $ python3 game_boards.py
"""

# imports 
import numpy as np

class Game1:

    G = np.array([[0, 'G1'], ['G2', 'G3']], dtype=object)

    G1 = np.array([[4, 3], [1, 2]])

    G2 = np.array([[0, 6], [5, 1]])

    G3 = np.array([[0, -2], [-2, 0]])

    boards = np.array([G, G1, G2, G3])

    big_board = np.array([
        [0, 0, 4, 3], 
        [0, 0, 1, 2], 
        [0, 6, 0, -2], 
        [5, 1, -2, 0]
    ])
