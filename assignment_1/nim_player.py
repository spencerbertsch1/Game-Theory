"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #1 - Problem #5) Nim Player 

The goal of this problem is to take an initial board state for a nim game (c1, c2, ..., cn) and generate 
one or all of the possible best plays that would help the player win the game. 

We can think of this by taking the initial board state and examining every possible first move and 
determining whether or not that move places the player into an N position or a P position. If the move
places the player into a P position, then that's a winning move so we log it. If not, then we pass and 
move on. 

Note that, depending on the size of the initial board, there could be thousands or millions of winning 
moves. In order to avoid over logging, a limit of 100 possible moves has been applied. This limit can 
be increased or removed for testing by TAs if need be. 

This script can be run at the command line by running the following: $ python3 nim_player.py
"""

# imports
import numpy as np
import re

# local imports 
from nim_setup import NimGame, WINNING_MOVE_LIMIT

# choose the board we want to solve: 
nim_board: tuple = NimGame.board_2


def nim_sum(input: tuple) -> int:
    """
    This is a function that takes a tuple of values and returns the nim sum of all those values. 
    
    --- 

    :param: input - tuple of input values 
    :return: int - integer representing the nim summed values in the input tuple 
    """

    # here we generate a list containing numpy arrays of binary values of each of our inputs 
    numpy_arrays = []
    for i in input:
        binary_i: str = format(i, "b")
        comma_b = (','.join(binary_i))
        b = np.fromstring(comma_b, dtype=int, sep=',')
        numpy_arrays.append(b)

    # here we fill in the ragged arrays to get a matrix 
    # first we find the length of the longest binary number 
    max_len_binary = 0
    for bin in numpy_arrays:
        if bin.size > max_len_binary:
            max_len_binary = bin.size
    # we now need to left fill the smaller numpy vectors with zeros 
    padded_arrays = []
    for arr in numpy_arrays:
        zeros_to_pad = max_len_binary - arr.size
        if zeros_to_pad != 0: 
            pad_arr = np.pad(arr, (zeros_to_pad, 0), 'constant', constant_values=(0, 0))
            padded_arrays.append(pad_arr)
        else: 
            padded_arrays.append(arr)
    # now we stack the list into a big numpy matrix 
    binary_matrix: np.array = np.vstack(padded_arrays)
    # now we can take the column sum of the matrix of binary values 
    col_sum = np.sum(binary_matrix, axis=0)
    # and now we can mod all the values in this vector by 2
    mod_col_sum = np.remainder(col_sum, 2)

    # and lastly we need to convert our new binary string back into an integer, then return that int
    arr_string = np.array_str(mod_col_sum)
    # we now need to ensure we remove any spaces or brackets from our string - we can use regex for this
    clean_string = re.sub("[^0-9]", "", arr_string)
    # and finally we convert the cleaned binary string back into an int
    nim_sum_int = int(clean_string, 2)

    return nim_sum_int


def nim_game(): 
    """
    Here we iterate through all the possible moves and see which of these moves give us P positions. 
    """

    # first we iterate through each of the (n) piles 
    win_move_limit = 0
    for i in range(len(nim_board)): 
        # then we iterate through each of the chips in each pile
        for j in range(nim_board[i]): 
            aux_nim_board = nim_board.copy()
            aux_nim_board[i] = aux_nim_board[i] - (j+1) 

            # we can now get the nim sum of the new board 
            ns = nim_sum(input=aux_nim_board)

            # here we log the move if it places us into a p-position
            if (ns == 0) & (win_move_limit < WINNING_MOVE_LIMIT): 
                solution = [0] * len(nim_board)
                solution[i] = solution[i] - (j+1)
                print(f'The following move places us in a P position: {solution}')

def main():
    print(f'Solving the following Nim Game board: {nim_board}')
    nim_game()

if __name__ == "__main__":
    main()
