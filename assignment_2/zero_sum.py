"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #2 - Problem #1) 2-Person Zero Sum Games

The goal of this problem is to take an input matrix and generate the equilibrium strategies for 
player 1 and player 2, and also the value of the game. 

This script can be run at the command line by running the following: $ python3 zero_sum.py
"""

# imports 
import numpy as np
from pyparsing import col

# local imports 
from zero_sum_settings import PayoffMatrices

class ZeroSum():

    def __init__(self, payoff_matrix: np.array, VERBOSE: bool = False):
        self.payoff_matrix = payoff_matrix
        self.VERBOSE = VERBOSE

    @staticmethod
    def pretty_print_solution(solution_dict: dict):
        """
        Simple utility function to print the two equilibrium strategies and the game value to the 
        console in a nice, readable way. 
        """
        s = "-"*5
        method = solution_dict["method"]
        for k, v in solution_dict.items():
            if k != "method":
                print(f'{method} {s} {k}: {v} {s}')

    def method_one(self):
        """
        Find the saddle point(s) in the input matrix if there are any. 

        NOTE: p and q are 1 indexed here! I thought this made more sense given the context from class. 
        :param: - NA
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        # initialize the equilibrium strategies and also the value of the game 
        p, q, v = np.nan, np.nan, np.nan

        # find the row minimums and column maximums 
        row_min_vec: np.array = self.payoff_matrix.min(axis=1)
        col_max_vec: np.array = self.payoff_matrix.max(axis=0)

        # find any saddle points and log them 
        for i in range(self.payoff_matrix.shape[0]):
            for j in range(self.payoff_matrix.shape[0]):
                if row_min_vec[i] == col_max_vec[j]:
                    # saddle point found 
                    v = row_min_vec[i]
                    p = i+1
                    q = j+1
                    print(f'Saddle point found! p: {p}, q: {q}, game value: {v}')

        # print the solution
        if self.VERBOSE:
            self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 1 - Saddle Points"})

        return {"p": p, "q": q, "v": v}

    def method_two():
        pass


def main():
    """
    Create an instance of the 2 player zero sum game and attempt to solve the game and find
    p, q, and v using various differnt methods to see what works and what doesn't. 
    
    :param: - NA
    :return: - NA
    """
    # define the parameters we will use 
    VERBOSE = True  # <-- set to true if you want all the output printed to the console 
    mat = PayoffMatrices.mat3

    # create a 2 player zero sum game instance 
    game = ZeroSum(payoff_matrix=mat, VERBOSE=VERBOSE)

    # --- METHOD #1: Check for saddle points --- 
    game.method_one()

    # --- METHOD #2: Use the 2 x 2 matrix formula --- 
    # game.method_two()



if __name__ == "__main__":
    main()

