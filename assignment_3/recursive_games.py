"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #3 - Problem #1(b) Recursive Games

The goal of this problem is to solve two example recursive games and produce the solutions that match 
solutions we get from solving the same problem by hand. Of course we can use recursive functions to 
find the solutions programatically, so that is the purpose of this script. 

This script can be run at the command line by running the following: $ python3 recursive_games.py
"""

# imports 
import numpy as np

# local imports 
from game_boards import Game1
from zero_sum import ZeroSum

class RecursiveGame:

    def __init__(self, Game):
        self.boards = Game.boards
        self.num_boards = self.boards.shape[0]
        self.board_x = self.boards.shape[1]
        self.board_y = self.boards.shape[2]

    def game_tree_search(self, mat):

        # --- BASE CASE ---
        board_int_list = [isinstance(x, (np.int64, int, float)) for x in list(mat.flatten())]
        if all(x is True for x in board_int_list):
            # here we can use the simplex implementation from the last homework assignment to find the value of the matrix
            game = ZeroSum(payoff_matrix=mat, VERBOSE=False)
            # here we have a matrix that is entirely composed of integers, so we can use the simplex method to solve 
            game_dict = game.method_seven(A=mat)
            return game_dict['v']

        # --- RECURSIVE CASE ---
        # now we know that we need to dig through the tree and recursively solve the game 
        else:

            for i in range(self.board_x):
                for j in range(self.board_y):
                    
                    curr_element = mat[i, j]
                    if isinstance(curr_element,(np.int64, int, float)): 
                        # we don't need to worry here because we already have an int value in the matrix 
                        pass

                    else:
                        # here we need to step into the recursive function 
                        mat_index: int = int(curr_element[-1])
                        matrix_to_solve: np.array = self.boards[mat_index].copy()
                        local_matrix_value: float = self.game_tree_search(mat = matrix_to_solve)
                        mat[i, j] = local_matrix_value

        print(f'Final Matrix: \n {mat}')
        game = ZeroSum(payoff_matrix=mat, VERBOSE=True)
        # here we have a matrix that is entirely composed of integers, so we can use the simplex method to solve 
        game_dict = game.method_seven(A=mat)
        v = game_dict['v']
        p = game_dict['p']
        q = game_dict['q']
        print(f'RECURSIVE SOLUTION \n Value: {round(v, 3)} \n p: {p} \n q: {q}')

        return v

def main_i():

    G = RecursiveGame(Game=Game1)
    G.game_tree_search(mat = Game1.boards[0])

    # print('double check game value')
    # big_board = Game1.big_board
    # game = ZeroSum(payoff_matrix=big_board, VERBOSE=True)
    # # here we have a matrix that is entirely composed of integers, so we can use the simplex method to solve 
    # game_value = game.method_seven(A=big_board)['v']
    # print(f'Final Value: {round(game_value, 3)}')


def main_ii():

    pass  # TODO 


if __name__ == "__main__":
    main_i()
    main_ii()
