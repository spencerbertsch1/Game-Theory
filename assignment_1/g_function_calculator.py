"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #1 - Problem #6) G Function Calculator

The goal of this problem is to take any directed acyclig graph (DAG) and identify the g-value of 
each vertex. Additionally, we want to know if each vertex in the graph represents a P position or 
an N position. 

This script can be run at the command line by running the following: $ python3 g_function_calculator.py
"""

# imports 
import numpy as np

# local imports 
from g_function_setup import Graphs


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

def graph_g_func_calc():
    """
    Parent function that uses the recursive g_func_calc function and generates a results table showing the 
    g-function value and the P/N state for each vertex in an input graph. 
    """
    # step 1: generate a dictionary representing the mapping between each vertex and its g-value 
    g_mapper = dict.fromkeys(graph, 0)
    
    # now we need to find g(x) for each x value in the mapper dict 
    for vertex, _ in g_mapper.items():

        # here is where we need to call the recursive g_func_calc function
        g_x = g_func_calc(vertex=vertex)
        # now that we have the g-value for our vertex we need to store it in the g_mapper dict 
        g_mapper[vertex] = g_x

    # convert the g_mapper dict into a numpy array, transpose that array, then add '(x)' and 'g(x)', then print. 
    result = g_mapper.items()
    # Convert object to a list
    results_data = list(result)
    # here we add some strings for extra readability of the output
    results_data.insert(0, ('   x', 'g(x)'))
    # Convert list to an array
    results_array = np.array(results_data)
    results_array = results_array.T

    # at this point we need to add an additional layer to the array to show which of the vertices are P/N states
    p_n_list = []
    for i in range(results_array.shape[1]):
        if i == 0:
            p_n_list.append(' P/N')
        else: 
            if results_array[1][i] == '0':
                p_n_list.append('P')
            else:
                p_n_list.append('N')

    # we now vectorize the list and vertically concatenate it to our matrix of solution information
    n_p_vec = np.asarray(p_n_list)
    results_array_final = np.vstack((results_array, n_p_vec))

    # now we can print the numpy array containg all the solution information. 
    print(results_array_final)


def g_func_calc(vertex: int):
    """
    
    We know that g(x) = mex[g(y)|y in F(x)]. We can use this recursive definition to define all values 
    of g(x) in our graph. 

    :param: int - vertex of the graph 
    :return: int - the g-value for that vertex 
    """

    # base case
    if len(graph[vertex]) == 0:
        # print(f'Vertex: {vertex}, we hit a leaf node so we return 0.')
        return 0

    # recursive case
    else:
        # print(f'Vertex: {vertex}, we hit the recursive case.')
        successors = graph[vertex]
        v_set = []
        for v in successors:
            v_set.append(g_func_calc(vertex=v))
        return mex(v_set)


def main():
    # choose the graph we want to use: 
    global graph
    graph = Graphs.graph3

    print(f'Calculating the g-values and P/N states for each vertex of the following graph: \n {graph} \n Solution:')
    graph_g_func_calc()

if __name__ == "__main__":
    main()
