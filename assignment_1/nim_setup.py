"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #1 - Problem #5) Nim Player 

This script is used to represent the initial board state of the nim game that we want to solve. 
"""

class NimGame:
    """
    Here we store each board state as a tuple. Each element of the tuple represent the number of chips
    in the stack. The length of the tuple (n) represents the number of stacks in the Nim Game. 
    """
    board_1 = [1, 2]
    board_2 = [5, 12, 13]
    board_3 = [10, 20, 30, 40, 50]
    board_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board_5 = [5, 5, 5, 5]
    board_6 = [3, 4, 5]

# here we define a max number of winning moves we want to print. 
WINNING_MOVE_LIMIT: int = 100