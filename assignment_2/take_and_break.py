"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #2 - Problem #3) a) Take and Break

The goal of this problem is to ...

This script can be run at the command line by running the following: $ python3 take_and_break.py
"""

# imports
import numpy as np
import re


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


def take_and_break_logic(x: int, g_x_dict: dict) -> int:
    # TODO add the game logic here! 
    return x*2


def main():
    g_x_dict = {}
    for x in range(101):
        g_x = take_and_break_logic(x=x, g_x_dict=g_x_dict)
        g_x_dict[x] = g_x
        print(f'x={x}, g(x)={g_x}')


if __name__ == "__main__":
    main()
