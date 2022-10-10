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
import statistics
import numpy as np
from itertools import combinations
from numpy.linalg import inv

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
                print(f'{method} {s} {k}: {round(v, 2)} {s}')

    @staticmethod
    def comb_generator(i: int):
        """
        Small utility function designed to return all of the 2-number combinations up to an integer value (i)

        :param: i - int representing the maximum value to retrieve combinations for
        :return: list of 2-length tuples representing combinations
        """
        # first we generate a list out of the range up to the input int (i)
        l = list(range(i))
        # next we get all of the 2-length combinations and store them in a list
        combos = list(combinations(l, 2))

        return combos 


    def method_one(self, A: np.array):
        """
        Find the saddle point(s) in the input matrix if there are any. 

        NOTE: p and q are 1 indexed here! I thought this made more sense given the context from class. 
        :param: - NA
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        solved = False
        # initialize the equilibrium strategies and also the value of the game 
        p, q, v = np.nan, np.nan, np.nan

        # find the row minimums and column maximums 
        row_min_vec: np.array = A.min(axis=1)
        col_max_vec: np.array = A.max(axis=0)

        smaller_dim = min(A.shape[0], A.shape[1])

        # find any saddle points and log them 
        for i in range(smaller_dim):
            for j in range(smaller_dim):
                if row_min_vec[i] == col_max_vec[j]:
                    # saddle point found 
                    v = row_min_vec[i]
                    p = i+1
                    q = j+1
                    print(f'Saddle point found! p: {p}, q: {q}, game value: {v}')
                    solved = True

        # print the solution
        if (self.VERBOSE) & (v is not np.nan):
            self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 1 - Saddle Points"})
        elif (self.VERBOSE) & (v is np.nan):
            print('Method 1 complete... No saddle point found.')

        return {"p": p, "q": q, "v": v, "solved": solved}

    def method_two(self, A: np.array):
        """
        Use the formulas for the 2x2 matrix case here. p and q are 1 indexed here! I thought this made more sense given the context from class. 
        :param: - NA
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """

        assert ((A.shape[0] == 2) & (A.shape[1]==2)), "Method 2 can only be used on 2x2 matrices!"

        # test for saddle points
        d = self.method_one(A=A)
        if d['solved'] is True:
            print('Method 2 should not be used - this payoff matrix has a saddle point! Using Method 1 instead.')
            self.pretty_print_solution(solution_dict={"p": d['p'], "q": d['q'], "v": d['v'], "method": "Method 1 - Saddle Points"})
        else:

            # define each element of the 2x2 matrix
            a = A[0][0]
            b = A[0][1]
            c = A[1][1]
            d = A[1][0]

            # use the formulas from class to define the optimal strategies
            p = (c-d)/((a-b) + (c-d))
            q = (c-b)/((a-b) + (c-d))
            det_A = np.linalg.det(A)
            v = det_A/((a-b) + (c-d))

            # print the solution
            if self.VERBOSE:
                self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 2 - 2x2 Formulas"})

            return {"p": p, "q": q, "v": v, "solved": True}
        

    def dominant_recursion(self, input_matrix: np.array):
        """
        Recursive function to reduce a matrix down by eliminating rows/columns that represent dominant strategies

        Here we are assuming that there will always be a dominant strategy for the input matrix... 
        TODOs: 
            1. break if we hit a point where there are NO dominant strategies and the matrix is still not reduced to 2x2
            2. sweep through all possible weights ((0.1, 0.9), (0.2, 0.8), ...) for the rows/columns to find dominant strategies
        """
        # base case - there are no dominant strategies, or the matrix is a 2x2 and can be solved through other means
        if ((input_matrix.shape[0] == 2) & (input_matrix.shape[1]==2)):
            if self.VERBOSE:
                print(f'Dominant strategies have reduced the input matrix to a 2x2! Now we can call on Method 2 to get the solution.')
            return input_matrix

        else:
            # now we need to find the dominant strategy and remove the weak column or row
            column_combos: list = self.comb_generator(i=input_matrix.shape[1])
            row_combos: list = self.comb_generator(i=input_matrix.shape[0])

            # iterate over all column combinations
            for col_combo in column_combos:
                col1 = list(input_matrix[:, col_combo[0]])
                col2 = list(input_matrix[:, col_combo[1]])

                # test to see if one side is dominant
                greater_list = [[x, y] for x, y in zip(col1, col2) if x > y]
                fewer_list = [[x, y] for x, y in zip(col1, col2) if x < y]

                # remove columns that are totally dominated by other columns
                if len(greater_list) == input_matrix.shape[0]:
                    print(f'Dominant strategy found! We can now remove column {col_combo[1]} from the matrix and continue.')
                    if input_matrix.shape[1]>2:  # <-- we don't want to reduce to a single column here 
                        reduced_matrix = np.delete(input_matrix, (col_combo[1]), axis=1)

                elif len(fewer_list) == input_matrix.shape[0]:
                    print(f'Dominant strategy found! We can now remove column {col_combo[0]} from the matrix and continue.')
                    if input_matrix.shape[1]>2:  # <-- we don't want to reduce to a single column here 
                        reduced_matrix = np.delete(input_matrix, (col_combo[0]), axis=1)

            # iterate over all row combinations
            for row_combo in row_combos:
                row1 = list(input_matrix[row_combo[0], :])
                row2 = list(input_matrix[row_combo[1], :])

                # test to see if one side is dominant
                greater_list = [[x, y] for x, y in zip(row1, row2) if x > y]
                fewer_list = [[x, y] for x, y in zip(row1, row2) if x < y]

                # remove rows that are totally dominated by other rows
                if len(greater_list) == input_matrix.shape[1]:
                    print(f'Dominant strategy found! We can now remove row {row_combo[1]} from the matrix and continue.')
                    if input_matrix.shape[0]>2:  # <-- we don't want to reduce to a single row here 
                        reduced_matrix = np.delete(input_matrix, (row_combo[1]), axis=0)

                elif len(fewer_list) == input_matrix.shape[1]:
                    print(f'Dominant strategy found! We can now remove row {row_combo[0]} from the matrix and continue.')
                    if input_matrix.shape[0]>2:  # <-- we don't want to reduce to a single row here 
                        reduced_matrix = np.delete(input_matrix, (row_combo[0]), axis=0)

            # make the recursive call passing in the newly reduced matrix 
            return self.dominant_recursion(input_matrix=reduced_matrix)


    def method_three(self, A: np.array):
        """
        p and q are 1 indexed here! I thought this made more sense given the context from class. 
        :param: - NA
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        # Step 1: use our recursive function to get the 2x2 matrix using dominant strategies
        reduced_matrix = self.dominant_recursion(input_matrix=A)

        # Step 2: Use methods 1 or 2 to get the solution for the new 2x2 matrix
        self.method_two(A=reduced_matrix)

    def method_four(self, A: np.array):
        pass

    def method_five(self, A: np.array):
        pass

    def method_six(self, A: np.array):
        """
        Here we use a formula to calculate p, q, and v as long as A is an invertible (non-degenerate) matrix. 
        :param: A - np.array representing the input matrix
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        try: 
            a_inv = inv(A)
        except:
            a_inv = np.nan

        if a_inv is np.nan: 
            print(f'The input matrix is singular (non-invertible), so method 6 cannot be used. Passing...')
        else:
            # here we know that our matrix is nonsingular, so we can move forward with the computation
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
    mat = PayoffMatrices.mat6

    # create a 2 player zero sum game instance 
    game = ZeroSum(payoff_matrix=mat, VERBOSE=VERBOSE)

    # --- METHOD #1: Check for saddle points --- 
    game.method_one(A=mat)

    # --- METHOD #2: Use the 2 x 2 matrix formula --- 
    # game.method_two(A=mat)

    # --- METHOD #3: Recursive Reduction using Dominant Strategies --- 
    # game.method_three(A=mat)

    # --- METHOD #6: Formula for non-degenerate n x n
    game.method_six(A=mat)



if __name__ == "__main__":
    main()

