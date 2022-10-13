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
import math

def mex(input_set: set): 
    """
    Utility function that returns the smallest non-negative integer that is NOT contained 
    in the input_set 

    :param: set - input_set representing the values we pass to the mex() function
    :return: int - integer representing the result of mex(s)
    """
    mex = 0
    while mex in input_set:
        mex += 1
    return mex 

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
    # this takes care of the previous solutions, now we just need to account for the other values
    curr_nim_sum_list = [v for _, v in g_x_dict.items()]

    # we only need to iterate through half of x since (x NIMSUM y) = (y NIMSUM x)
    iter_x = math.floor(x/2)
    for i in range(1, iter_x+1, 1):
        # create pile 1
        pile_1 = i
        # create pile 2
        pile_2 = x - i
        
        # get g-value for pile 1 and pile 2
        g_pile_1 = g_x_dict[pile_1]
        g_pile_2 = g_x_dict[pile_2]

        # generate the new nim sum that we need to add to the complete list
        nim_sum_to_add = nim_sum((g_pile_1, g_pile_2))

        curr_nim_sum_list.append(nim_sum_to_add)

    final_g_value = mex(tuple(curr_nim_sum_list))

    return final_g_value 


def main():
    g_x_dict = {}
    for x in range(101):
        g_x = take_and_break_logic(x=x, g_x_dict=g_x_dict)
        g_x_dict[x] = g_x
        print(f'g({x})={g_x}')


if __name__ == "__main__":
    main()

