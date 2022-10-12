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
from scipy.optimize import linprog

# local imports 
from zero_sum_settings import PayoffMatrices

class ZeroSum():

    def __init__(self, payoff_matrix: np.array, VERBOSE: bool = False):
        self.payoff_matrix = payoff_matrix
        self.VERBOSE = VERBOSE

        print(f'_____PAYOFF MATRIX_____ \n {self.payoff_matrix}')

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
                if isinstance(v, float):
                    v_round = round(v, 2)
                elif isinstance(v, int):
                    v_round = v
                else:
                    v_round = v.round(2)  # <-- used for np arrays
                print(f'{method} {s} {k}: {v_round} {s}')

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
        if isinstance(A, bool):
            print('something')
        # initialize the equilibrium strategies and also the value of the game 
        p, q, v = np.zeros(A.shape[0]), np.zeros(A.shape[1]), np.nan

        # find the row minimums and column maximums 
        row_min_vec: np.array = A.min(axis=1)
        col_max_vec: np.array = A.max(axis=0)

        for i, row_min in enumerate(row_min_vec):
            for j, col_max in enumerate(col_max_vec):
                if row_min == col_max: 
                    # saddle point found 
                    v = row_min_vec[i]
                    p[i] = 1
                    q[j] = 1
                    if self.VERBOSE:
                        print(f'Saddle point found! p: {p}, q: {q}, game value: {v}')
                    solved = True

        # print the solution
        if solved:
            self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 1 - Saddle Points"})
        else:
            print('Method 1 complete. No saddle point found. Passing...')

        return {"p": p, "q": q, "v": v, "solved": solved}


    def method_two(self, A: np.array):
        """
        Use the formulas for the 2x2 matrix case here. p and q are 1 indexed here! I thought this made more sense given the context from class. 
        :param: - NA
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """

        # test for saddle points
        d = self.method_one(A=A)
        if d['solved'] is True:
            print('Method 2 should not be used - this payoff matrix has a saddle point! Using Method 1 instead.')
            self.pretty_print_solution(solution_dict={"p": d['p'], "q": d['q'], "v": d['v'], "method": "Method 1 - Saddle Points"})
        else:

            # method 2 can only ever be used on 2x2 matrices
            if ((A.shape[0] == 2) & (A.shape[1]==2)): 

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
            
            else:
                print("Method 2 can only be used on 2x2 matrices. Passing...")
        

    def dominant_recursion(self, input_matrix: np.array):
        """
        Recursive function to reduce a matrix down by eliminating rows/columns that represent dominant strategies

        Here we are assuming that there will always be a dominant strategy for the input matrix... 

        TODOs: 
            1. iterate through 3 column / 3 row combinations as well as 2 row / 2 col combinations
            2. sweep through 10 possible weights ((0.1, 0.9), (0.2, 0.8), ...) for the rows/columns to find dominant strategies
        """
        if input_matrix is False:
            return False

        # base case - there are no dominant strategies, or the matrix is a 2x2 and can be solved through other means
        if ((input_matrix.shape[0] == 2) & (input_matrix.shape[1]==2)):
            if self.VERBOSE:
                print(f'Dominant strategies have reduced the input matrix to a 2x2! Now we can call on Method 2 to get the solution.')
            return input_matrix

        else:
            # now we need to find the dominant strategy and remove the weak column or row
            column_combos: list = self.comb_generator(i=input_matrix.shape[1])
            row_combos: list = self.comb_generator(i=input_matrix.shape[0])

            # add a check here to see if we need to break out of the recursion
            # this occurs when the matrix is NOT 2x2, but no dominant strategies exist... 
            dom_strategy = False

            # iterate over all column combinations
            for col_combo in column_combos:
                col1 = list(input_matrix[:, col_combo[0]])
                col2 = list(input_matrix[:, col_combo[1]])

                # test to see if one side is dominant
                greater_list = [[x, y] for x, y in zip(col1, col2) if x > y]
                fewer_list = [[x, y] for x, y in zip(col1, col2) if x < y]

                # remove columns that are totally dominated by other columns
                if len(greater_list) == input_matrix.shape[0]:
                    if self.VERBOSE:
                        print(f'Dominant strategy found! We can now remove column {col_combo[1]} from the matrix and continue.')
                    if input_matrix.shape[1]>2:  # <-- we don't want to reduce to a single column here 
                        reduced_matrix = np.delete(input_matrix, (col_combo[1]), axis=1)
                        dom_strategy = True

                elif len(fewer_list) == input_matrix.shape[0]:
                    if self.VERBOSE:
                        print(f'Dominant strategy found! We can now remove column {col_combo[0]} from the matrix and continue.')
                    if input_matrix.shape[1]>2:  # <-- we don't want to reduce to a single column here 
                        reduced_matrix = np.delete(input_matrix, (col_combo[0]), axis=1)
                        dom_strategy = True

            # iterate over all row combinations
            for row_combo in row_combos:
                row1 = list(input_matrix[row_combo[0], :])
                row2 = list(input_matrix[row_combo[1], :])

                # test to see if one side is dominant
                greater_list = [[x, y] for x, y in zip(row1, row2) if x > y]
                fewer_list = [[x, y] for x, y in zip(row1, row2) if x < y]

                # remove rows that are totally dominated by other rows
                if len(greater_list) == input_matrix.shape[1]:
                    if self.VERBOSE:
                        print(f'Dominant strategy found! We can now remove row {row_combo[1]} from the matrix and continue.')
                    if input_matrix.shape[0]>2:  # <-- we don't want to reduce to a single row here 
                        reduced_matrix = np.delete(input_matrix, (row_combo[1]), axis=0)
                        dom_strategy = True

                elif len(fewer_list) == input_matrix.shape[1]:
                    if self.VERBOSE:
                        print(f'Dominant strategy found! We can now remove row {row_combo[0]} from the matrix and continue.')
                    if input_matrix.shape[0]>2:  # <-- we don't want to reduce to a single row here 
                        reduced_matrix = np.delete(input_matrix, (row_combo[0]), axis=0)
                        dom_strategy = True

            # make the recursive call passing in the newly reduced matrix 
            if dom_strategy:
                return self.dominant_recursion(input_matrix=reduced_matrix)
            else:
                print(f'Method 3 has failed - there are no dominant strategies, but the payoff matrix is ({input_matrix.shape[0]} x {input_matrix.shape[1]}) not (2 x 2). Passing...')
                return False


    def method_three(self, A: np.array):
        """
        p and q are 1 indexed here! I thought this made more sense given the context from class. 
        :param: - NA
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        # Step 1: use our recursive function to get the 2x2 matrix using dominant strategies
        reduced_matrix = self.dominant_recursion(input_matrix=A)

        # Step 2: Use methods 1 or 2 to get the solution for the new 2x2 matrix
        if isinstance(reduced_matrix, bool):
            pass
        else:
            self.method_two(A=reduced_matrix)

    def method_four(self, A: np.array):
        """
        Here we use the graphical approach to solve (2 x n) or (m x 2) games. 

        :param: A - np.array representing the input matrix
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        if (((A.shape[0] == 2) & (A.shape[1] != 2)) | ((A.shape[0] != 2) & (A.shape[1] == 2))):
            
            # first we deal with the case that there are two rows and n columns where n>2, so player 1 only has two options (p, 1-p)
            if A.shape[0] == 2:
                pass

            # now we deal with the case that there are two columns and m rows where m>2, so player 2 only has two options (q, 1-q)
            elif A.shape[0] == 2:
                pass

            else:
                raise Exception('We should never get here - check the dimensions of the input matrix...')
        else:
            print (f'Method 4 can only be used on (n x 2) or (2 x m) matrices, not ({A.shape[0]} x {A.shape[1]}) matrices. Passing...')

    def method_five(self, A: np.array):
        pass

    def method_six(self, A: np.array):
        """
        Here we use a formula to calculate p, q, and v as long as A is an invertible (non-degenerate) matrix. 
        :param: A - np.array representing the input matrix
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        # CHECK: ensure the matrix is square
        if A.shape[0] != A.shape[1]:
            print(f'Method 6 can only be used on (n x n) matrices, not ({A.shape[0]} x {A.shape[1]}) matrices. Passing...')
        else:

            # CHECK: test the matrix for saddle points
            d = self.method_one(A=A)
            if (d['solved'] is True): 
                print('Method 6 should not be used - this payoff matrix has a saddle point! Using Method 1 instead.')
                self.pretty_print_solution(solution_dict={"p": d['p'], "q": d['q'], "v": d['v'], "method": "Method 1 - Saddle Points"})
            
            else:
                # now we know there are NO saddle points and the matrix is square so we can continue with Method 6
                try: 
                    a_inv = inv(A)
                except:
                    a_inv = np.nan

                # CHECK: if the matrix turns out to be singular, then we increment all values of A by 1 to produce a matrix that is NOT singular
                if a_inv is np.nan: 
                    if self.VERBOSE:
                        print(f'The input matrix is singular (non-invertible), so we need to modify the payoff matrix slightly and try again')
                    return self.method_six(A=(A+1))

                # here we know that our matrix is nonsingular, so we can move forward with the computation
                # Calculate v
                a_inv = inv(A)
                n = A.shape[0]
                ones = np.ones(n)
                v_denom = np.dot(np.dot(ones.T, a_inv), ones)
                v = 1 / v_denom
                
                # CHECK: if the matrx has a game value of zero, then we increment by 1 and run again
                if v < 0.000001:
                    return self.method_six(A=(A+1))
                
                else:
                    # Calculate p
                    p = v * (np.dot(ones.T, a_inv))

                    # Calculate v
                    q = v * (np.dot(a_inv, ones))
                    
                    # print the solution
                    self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 6 - Formula for non-degenerate n x n"})

                    return {"p": p, "q": q, "v": v, "solved": True}


    def method_seven(self, A: np.array):
        """
        Use the simplex algorithm to generate the solution

        SOURCES - I found several sources very helpful in understanding the simplex algorithm, mostly wikipedia
        1. https://en.wikipedia.org/wiki/Simplex_algorithm

        :param: A - np.array representing the input matrix
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        # Step 1: Write matrix in Tableau form
        right_col = np.array([np.ones(A.shape[0])])
        A_with_col = np.concatenate((A, right_col.T), axis=1)
        bottom_row = np.array([np.ones(A.shape[1]+1)])*-1
        A_tableau = np.concatenate((A_with_col, bottom_row), axis=0)
        A_tableau[-1][-1] = 0

        print(A_tableau)

        # Step 2: Find the pivot 
        # TODO

        # Step 3: Perform the pivot 



def main():
    """
    Create an instance of the 2 player zero sum game and attempt to solve the game and find
    p, q, and v using various differnt methods to see what works and what doesn't. 
    
    :param: - NA
    :return: - NA
    """
    # define the parameters we will use 
    VERBOSE = False  # <-- set to true if you want all the output printed to the console 
    mat = PayoffMatrices.A_ii

    # create a 2 player zero sum game instance 
    game = ZeroSum(payoff_matrix=mat, VERBOSE=VERBOSE)

    # --- METHOD #1: Check for saddle points --- 
    game.method_one(A=mat)

    # --- METHOD #2: Use the 2 x 2 matrix formula --- 
    game.method_two(A=mat)

    # --- METHOD #3: Recursive Reduction using Dominant Strategies --- 
    game.method_three(A=mat)

    # --- METHOD #4: n x 2 or 2 x n --- 
    # game.method_four(A=mat)

    # --- METHOD #6: Formula for non-degenerate n x n
    game.method_six(A=mat)

    # --- METHOD #7: Simplex
    game.method_seven(A=mat)


if __name__ == "__main__":
    main()

