"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #3 - Problem #1(a) Guess It

The goal of this problem is to solve the Guess It two player bluffing card game using a recursive function. 
Remember that the payoff matrix for this game is as follows: 

[  (n/(n+1))*(1-G_n-1,m)+(1/(n+1))    (n/(n+1))*(1-G_n-1,m)  ]
[           (1-G_n,m-1)                          1           ]
[            (1/(n+1))                       (1/(n+1))       ]

This script can be run at the command line by running the following: $ python3 recursive_games.py
"""

# imports
import numpy as np
from zero_sum import ZeroSum


def guess_it(n: int, m: int, VERBOSE: bool = False):

    if VERBOSE:
        print(f'Calculating G_{n}{m}')
    
    # --- BASE CASE ---
    if ((m > 0) & (n == 0)):
        return {'v': 1, 'p': [], 'q': []}
    elif ((m == 0) & (n > 0)):
        return {'v': (1/(1+n)), 'p': [], 'q': []}
    else:

        # --- RECURSIVE CASE --- 

        # construct the board (the numpy array representing the current payoff matrix)
        board = np.zeros((2,2))

        # here we fill in all the values in the board by making three distinct recursive calls

        # Upper Left # 
        solution_dict = guess_it(n=n, m=m-1)
        upper_left_g_val = 1 - solution_dict['v']
        upper_left_val = (1/(n+1)) + ((n/(n+1)) * upper_left_g_val)
        board[0,0] = upper_left_val

        # Upper Right # 
        solution_dict = guess_it(n=n, m=m-1)
        upper_right_g_val = 1 - solution_dict['v']
        upper_right_val = ((n/(n+1)) * upper_right_g_val)
        board[0,1] = upper_right_val

        # Lower Left # 
        solution_dict = guess_it(n=n-1, m=m)
        lower_left_g_val = 1 - solution_dict['v']
        lower_left_val = ((n/(n+1)) * lower_left_g_val)
        board[1,0] = lower_left_val

        # Lower Right # 
        board[1,1] = 1

        # now we get the value of the 2x2 board
        print(f'Final Matrix: \n {board}')
        game = ZeroSum(payoff_matrix=board)
        
        # use the simplex method to solve this 2x2 game 
        game_dict = game.method_seven(A=board)
        v = round(game_dict['v'], 2)
        p = game_dict['p']
        q = game_dict['q']
        if VERBOSE: 
            print(f'RECURSIVE SOLUTION \n Value: {round(v, 3)} \n p: {p} \n q: {q}')

        return {'v': v, 'p': p, 'q': q}


def test_guess_it():
    """
    Simple utility function used to test the guess it function
    """
    n,m = 1,1
    # get the value of the current game
    game_val_dict = guess_it(m=m, n=n)
    v = game_val_dict['v']

    print(f'Value of G(n={n},m={m})= {v}')


def pretty_print_solution(solution_dict: dict):
    """
    Utility function to help visualize the solution
    """
    for m_n_tuple, value_dict in solution_dict.items():
        v = value_dict['v']
        p = value_dict['p']
        q = value_dict['q']
        m = m_n_tuple[0]
        n = m_n_tuple[1]
        s = '-'*5
        print(f'{s}  Solution to G(m={m}, n={n}): v={v}, p={p}, q={q}  {s}')


def main():
    """
    Main function that's used to generate the solution to the input game 
    """
    solution: dict = {}
    for i in range(1, 7, 1):
        for j in range(1, 7, 1):
            # get the value of the current game
            game_val_dict = guess_it(m=i, n=j)
            m_n_tuple = (i, j)
            solution[m_n_tuple] = game_val_dict

    pretty_print_solution(solution_dict=solution)


if __name__ == "__main__":

    # Define the parameters for this problem 
    # test_guess_it()
    main()

# TODO Question: are these solutons correct? The lecture shows the indices switched... not sure which to use! 
# TODO supress output from simplex method 