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
import random
import sys

# local imports 
from routines import intersection
from zero_sum_settings import PayoffMatrices


class ZeroSum():

    def __init__(self, payoff_matrix: np.array, VERBOSE: bool = False):
        self.payoff_matrix = payoff_matrix
        self.VERBOSE = VERBOSE

        print(f'_____PAYOFF MATRIX_____ \n {self.payoff_matrix}')

    @staticmethod
    def is_symmetric(A: np.array):
        """
        Utility function that returns true if the input matrix is symmetric 
        """
        # create a new matrix B that represents the transpose of A 
        B = A.T
        if np.array_equal(A, B):
            return True
        else:
            return False



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
                elif isinstance(v, list):
                    v_round = [round(x, 2) for x in v]
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

                # generate the solution vectors
                p_vec = [p, 1-p]
                q_vec = [q, 1-q]

                # print the solution
                self.pretty_print_solution(solution_dict={"p": p_vec, "q": q_vec, "v": v, "method": "Method 2 - 2x2 Formulas"})                  

                return {"p": p_vec, "q": q_vec, "v": v, "solved": True}
            
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
                print(f'Reduced (intermediate) matrix: \n {reduced_matrix}')
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
            print('Method 3 successful! The matrix has been reduced to a 2 x 2. Passing the reduced matrix to Method 2.')
            self.method_two(A=reduced_matrix)
            print(f'Reduced Matrix: \n {reduced_matrix}')

    def method_four(self, A: np.array):
        """
        Here we use the graphical approach to solve (2 x n) or (m x 2) games. 

        :param: A - np.array representing the input matrix
        :return: dict - dictionary containing the equilibrium strategies and the value of the game 
        """
        if (((A.shape[0] == 2) & (A.shape[1] != 2)) | ((A.shape[0] != 2) & (A.shape[1] == 2))):
            
            # first we deal with the case that there are two rows and n columns where n>2, so player 1 only has two options (p, 1-p)
            if A.shape[0] == 2:

                # iterate over the columns ot make a system of linear equations
                lines = []
                for i in range(A.shape[1]):
                    p1 = (0, A[1, i])
                    diff = A[0, i] - A[1, i]
                    p2 = (1, (diff + A[1, i]))
                    line = (p1, p2)
                    lines.append(line)

                intersect_points = []
                line_combos = self.comb_generator(i=len(lines))
                for line_combo in line_combos: 
                    line1 = lines[line_combo[0]]
                    line2 = lines[line_combo[1]]
                    intersection_point = intersection(line1, line2)
                    if intersection_point != ['parallel']:
                        intersect_points.append(intersection_point)

                if len(intersect_points) == 0:
                    print('Method 4 has failed - the lines do not intersect.')
                    return False
                else:

                    min_intersects = []
                    for point in intersect_points:
                        min_intersection: bool = True
                        curr_y = point[1]
                        curr_x = point[0]
                        line_to_test = ((curr_x, 0),(curr_x, 1000))
                        # we only want to keep the points if they lie on the min-value line
                        for line in lines:
                            sub_intersection = intersection(line1, line_to_test)
                            if sub_intersection != ['parallel']:
                                sub_y = sub_intersection[1]

                            if sub_y < curr_y:
                                min_intersection = False

                        if min_intersection: 
                            min_intersects.append(point)

                    # now we just get the maximum point from this list:
                    max_y = min_intersects[0][1]
                    for point in min_intersects:
                        new_y = point[1]
                        if new_y > max_y:
                            max_y = new_y

                    # extract the point that sits at the maximum of al minimums 
                    max_min_point = 0
                    for point in min_intersects:
                        if point[1] == max_y:
                            max_min_point = point

                    # generate p, q and v from this information! 
                    p = [max_min_point[0], (1-max_min_point[0])]
                    q = []  # <-- placeholder 
                    v = 0   # <-- placeholder 
                    self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 4 - (n x 2) or (2 x m)"})

            # now we deal with the case that there are two columns and m rows where m>2, so player 2 only has two options (q, 1-q)
            elif A.shape[1] == 2:
                pass

            else:
                raise Exception('We should never get here - check the dimensions of the input matrix...')
        else:
            print (f'Method 4 can only be used on (n x 2) or (2 x m) matrices, not ({A.shape[0]} x {A.shape[1]}) matrices. Passing...')


    @staticmethod
    def indifference_method_solve(A: np.array):
        """
        Helper function to solve the system of equations generated from a payoff matrix 
        Usde for the principal fo indifference (Method 5)

        The solution will be of the format: 
            [p_1, p_1, ..., p_(n-1), p_(n), v]
            or 
            [q_1, q_1, ..., q_(n-1), q_(n), v]
        depending on whether or not we are calculating the p or q vector. Either way the 
        final value in the array will be the value of the game. 
        """
        right_col = np.array([np.ones(A.shape[0])])*-1
        A_with_col = np.concatenate((A, right_col.T), axis=1)
        bottom_row = np.array([np.ones(A.shape[1]+1)])
        A_new = np.concatenate((A_with_col, bottom_row), axis=0)
        A_new[-1][-1] = 0

        B = np.zeros(A_new.shape[0])
        B[-1] = 1
        solution = np.linalg.solve(A_new,B)

        return solution


    def method_five(self, A: np.array, boost: int=0):
        """
        Principle of Indifference 

        Here we create a system of linear equations from the payoff matrix and solve to get 
        the payoff vectors and the resulting value of the game. 

        This method assumes that each element of the p and q vectors are non-zero, that is each 
        element is between 0 and one. In other words, Player1 assumes that all the strategis for 
        Player2 are "active." 
        """

        # CHECK: ensure the matrix is square
        if A.shape[0] != A.shape[1]:
            print(f'Method 5 can only be used on (n x n) matrices, not ({A.shape[0]} x {A.shape[1]}) matrices. Passing...')
        else:

            boost = 0
            test_threshold: int = 10
            while np.linalg.cond(A) >= 1/sys.float_info.epsilon: 
                # the input matrix A is singular, so we add one to it
                boost += 1
                A += 1

                if boost > test_threshold:
                    print(f'Method 5 has failed - all {test_threshold} incremented matrices are singular. Passing...')
                    return False

            # construct linear equation matrix and solve
            solution = self.indifference_method_solve(A=A)
            v = solution[-1] - boost
            p = solution[:-1]

            # test to see if the matrix is symmetric. If so, then q = p, and we're done. 
            if self.is_symmetric(A=A):
                q = p.copy()
            else:
                # here we know q does not equal p, so we use the principle of indifference to find it. 
                # construct linear equation matrix
                solution = self.indifference_method_solve(A=A.T)
                q = solution[:-1]

            self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, 
                                    "method": "Method 5 - Principal of Indifference"})

            return {"p": p, "q": q, "v": v, "solved": True}



    def method_six(self, A: np.array, counter: int = 0):
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
                    counter += 1
                    return self.method_six(A=(A+1), counter=counter)

                # here we know that our matrix is nonsingular, so we can move forward with the computation
                # Calculate v
                a_inv = inv(A)
                n = A.shape[0]
                ones = np.ones(n)
                v_denom = np.dot(np.dot(ones.T, a_inv), ones)
                v_denom_check = np.matrix(ones) * np.matrix(a_inv) * np.matrix(ones).T
                v = 1 / v_denom
                
                # CHECK: if the matrx has a game value of zero, then we increment by 1 and run again
                if v < 0.000001:
                    counter += 1
                    return self.method_six(A=(A+1), counter=counter)
                
                else:
                    # Calculate p
                    p = v * (np.dot(ones.T, a_inv))

                    # Calculate v
                    q = v * (np.dot(a_inv, ones))
                    
                    # print the solution
                    v = v - counter
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
        # first we define the vectors that will be used as indices for this problem 
        X = [f'x({i})' for i in range(A.shape[0])]
        Y = [f'y({i})' for i in range(A.shape[1])]

        # we can't deal with a matrix that has a value of zero, so we need to do some preprocessing 
        matrix_min_val = np.min(A)
        if matrix_min_val < 0: 
            A = A - matrix_min_val  # <-- we add the magnitude of matrix_min_val to each element of A

        # Step 1: Write matrix in Tableau form
        right_col = np.array([np.ones(A.shape[0])])
        A_with_col = np.concatenate((A, right_col.T), axis=1)
        bottom_row = np.array([np.ones(A.shape[1]+1)])*-1
        A_tableau = np.concatenate((A_with_col, bottom_row), axis=0)
        A_tableau[-1][-1] = 0

        # print(A_tableau)
        A_tableau_pivot = A_tableau.copy()

        idx = 0
        while min(A_tableau_pivot[-1, :]) < 0:

            # create copy to reference later
            A_tableau_pivot_copy = A_tableau_pivot.copy()

            # Step 2: Find the pivot column - here we just select the column with the min value of the (m+1)th row
            min_val = min(A_tableau_pivot[-1, :-1])
            pivot_col_index_list = []
            for i, val in enumerate(list(A_tableau_pivot[-1, :-1])):
                if val == min_val:
                    pivot_col_index_list.append(i)
            # we use random.choice here because if more than one column is a suitable candidate, we just pick one and move on
            pivot_col_index: int = random.choice(pivot_col_index_list)

            
            # Step 3: Find the pivot row - we now need to divide the rightmost column by our pivot column 
            r_col = A_tableau_pivot[:-1, -1]  
            pivot_col = A_tableau_pivot[:-1, pivot_col_index] 

            pivot_row_dict: dict[int: float] = {}
            for row_index, (right_val, pivot_val) in enumerate(zip(r_col, pivot_col)):
                # now let's find the pivot row
                if pivot_val > 0: 
                    pivot_row_dict[row_index] = (right_val/pivot_val)
                elif pivot_val == 0:
                    pivot_row_dict[row_index] = np.inf

            # now we get the pivot row index by choosing the key from the dict with the smallest value 
            min_test_ratio = min(pivot_row_dict.values())
            min_test_ratio_indices = []
            for index, val in pivot_row_dict.items():
                if val == min_test_ratio:
                    min_test_ratio_indices.append(index)

            # remember we need to do this because there might be more than one candidate row 
            pivot_row_index: int = random.choice(min_test_ratio_indices)

            # so now we have our pivot column and pivot row 
            # print(f'Pivot col: {pivot_col_index}, pivot row: {pivot_row_index}')

            # Step 2.5: Switch the indices of the pivot row and column for the final step 
            pivot_row_index_val = X[pivot_row_index]
            pivot_col_index_val = Y[pivot_col_index]
            # now we swap these values
            X[pivot_row_index] = pivot_col_index_val
            Y[pivot_col_index] = pivot_row_index_val
            
            # Step 3: Perform the pivot 
            pivot_value = A_tableau_pivot[pivot_row_index, pivot_col_index]
            A_tableau_pivot[:, pivot_col_index] = np.divide(A_tableau_pivot[:, pivot_col_index], -pivot_value) 
            A_tableau_pivot[pivot_row_index, :] = np.divide(A_tableau_pivot[pivot_row_index, :], pivot_value) 

            for i in range(A_tableau_pivot.shape[0]):
                for j in range(A_tableau_pivot.shape[1]):
                    if ((i != pivot_row_index) & (j != pivot_col_index)):
                        q = A_tableau_pivot_copy[i, j]
                        r = A_tableau_pivot_copy[pivot_row_index, j]
                        c = A_tableau_pivot_copy[i, pivot_col_index]
                        new_val = q - ((r*c)/pivot_value)
                        A_tableau_pivot[i, j] = new_val
            
            # flip the sign of the pivot value 
            A_tableau_pivot[pivot_row_index, pivot_col_index] = -A_tableau_pivot[pivot_row_index, pivot_col_index]

            # print(A_tableau_pivot.round(3))

            idx += 1
        
        # now we take the resulting A_tableau_pivot matrix and find the value of the game (p, q, and v)
        # print(f'Success! Final Tableau: \n {A_tableau_pivot}')
        print(f'Method 7 Success - Simplex method converged after {idx} pivots.')

        # we can now move onto the calculation of p, q, and v. 
        # This is where matrix_min_val comes back into play: 
        corner_val = A_tableau_pivot[-1, -1]
        v = (1/corner_val)
        if matrix_min_val < 0: 
            v = v + matrix_min_val

        # calculate p
        p = []
        for i in range(A.shape[0]):
            # if the probability vector already adds up to one, then we just add a probability of zero.
            if sum(p) == 1:
                p.append(0)

            else:
                # Here we search through the Y vector to get the indices of the x(i) values that were shifted up 
                index_str = f'x({i})'

                # we only add a non-zero value if the row was rotated up 
                if index_str in Y: 
                    list_idx = Y.index(index_str)

                    # use the value in the last row with the list_indx'th column 
                    p_n = A_tableau_pivot[-1, list_idx]/corner_val
                    p.append(round(p_n, 2))
                else:
                    p.append(0)

        # calculate q
        q = []
        for i in range(A.shape[1]):
            # if the probability vector already adds up to one, then we just add a probability of zero.
            if sum(q) == 1:
                q.append(0)

            else:
                # Here we search through the X vector to get the indices of the y(i) values that were shifted down to the left 
                index_str = f'y({i})'

                # we only add a non-zero value if the row was rotated down to the left 
                if index_str in X: 
                    list_idx = X.index(index_str)

                    # use the value in the last column with the list_indx'th row 
                    q_n = A_tableau_pivot[list_idx, -1]/corner_val
                    q.append(round(q_n, 2))
                else:
                    q.append(0)

        # print the solution
        self.pretty_print_solution(solution_dict={"p": p, "q": q, "v": v, "method": "Method 7 - Simplex"})

        return {"p": p, "q": q, "v": v, "solved": True}


def main():
    """
    Create an instance of the 2 player zero sum game and attempt to solve the game and find
    p, q, and v using various differnt methods to see what works and what doesn't. 
    
    :param: - NA
    :return: - NA
    """
    # define the parameters we will use 
    VERBOSE = False  # <-- set to true if you want all the output printed to the console 
    mat = PayoffMatrices.mat12

    # create a 2 player zero sum game instance 
    game = ZeroSum(payoff_matrix=mat, VERBOSE=VERBOSE)

    # --- METHOD #1: Check for saddle points --- 
    game.method_one(A=mat.copy())

    # --- METHOD #2: Use the 2 x 2 matrix formula --- 
    # game.method_two(A=mat.copy())

    # --- METHOD #3: Recursive Reduction using Dominant Strategies --- 
    # game.method_three(A=mat.copy())
    # remember method 3 might yield different solutions if th matrix is larger than a 2x2 because it REDUCES to a 2x2, then solves. 

    # --- METHOD #4: n x 2 or 2 x n --- 
    # game.method_four(A=mat.copy())

    # --- METHOD #5: n x 2 or 2 x n --- 
    # game.method_five(A=mat.copy())

    # --- METHOD #6: Formula for non-degenerate n x n
    # game.method_six(A=mat.copy())

    # --- METHOD #7: Simplex
    game.method_seven(A=mat.copy())


if __name__ == "__main__":
    main()

