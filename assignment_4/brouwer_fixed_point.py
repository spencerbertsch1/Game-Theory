"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #4 - Problem #1(b) Brouwer Fixed Point Script

The goal of this script is to find a fixed point over a continuous range using two methods: 
    1. A linear search method
    2. A Depth First Search - based continuous range slicing method 

This attempt actually turned out to be successful over the demo functions I defined in the main() function. 
I was pleased to see, for example, that the DFS-based range splitting algorithm found the fixed point after 
searching only 7 nodes, while the linear search needed to iterate over 132 nodes to find the solution. 

This script can be run at the command line by running the following: $ python3 brower_fixed_point.py
"""

# imports 
import math
import numpy as np
from numpy import array, array_equal

def brouwer_linear_search(domain: range, function: str, tolerance: float):
    """
    Linear search method to find the brouwer fixed point given a range and a continuous mapping function. 
    """
    cutoff = 100_000
    solved = False
    node_search_count = 0
    for x in domain:

        # increment the number of nodes in the graph searched (in this case the graph is just a long line of nodes)
        node_search_count += 1

        # here we add a stopping point so that we don't accidentally run through a billion iterations
        if node_search_count >= cutoff: 
            break

        f_x = function(x)
        if abs(x - f_x) < tolerance: 
            pretty_print_solution(x=x, f_x=f_x, method='Linear', tolerance=tolerance, node_search_count=node_search_count)
            solved = True
            break

    if solved is False:
        print(f'Fixed point could not be found using the linear method...')

    return solved 


def pretty_print_solution(x: float, f_x: float, method: str, tolerance: float, node_search_count: int):
    s = '-'*30
    print(f' \nSolution Found! \n{s}\n{method} Method fixed point solution -> x: {round(x, 3)}, f(x): {round(f_x, 3)}. \
        \nPoints match to within a tolerance of {tolerance}. \n{s} \
        \nNumber of nodes searched before finding a solution {node_search_count}. \n{s}')


def dfs_get_successors(domain: range, range_step: float) -> list:
    """
    This is a bit of an unorthadox was to get successor nodes for DFS, but here we use ranges of continuous values
    as nodes. For example, our root node is the full range, and the children of the root node are the two evenly divided 
    upper and lower halfs of the full range. In this way, DFS along with this function will create a binary tree of sorts 
    in which the leaf nodes will be ranges with length of one tolerance unit value. 

    The resulting tree would look something like this, in which the leaf nodes would be small ranges of length *tolerance*. 

                   [full range]
             /                    \
            v                      v
    [first half range]     [second half range]
         /    \                  /    \
        v      v                v      v
       ...    ...              ...    ...
    """

    min = np.min(domain)
    max = np.max(domain)
    mean = np.mean(domain)

    # left_node = np.arange(min, (mean + (range_step/2)), range_step)
    # right_node = np.arange((mean + (range_step/2)), max, range_step)
    left_node = np.arange(min, mean, range_step)
    right_node = np.arange(mean, max, range_step)

    return [left_node, right_node]


def is_leaf_node(node: range, tolerance: float, VERBOSE: bool):
    """
    Utility function that returns True if the node is a leaf node, False otherwise
    """
    leaf = False

    min = np.min(node)
    max = np.max(node)

    # we define whether we are at a leaf node based on the input tolerance value
    range_span = max - min
    if range_span < 2*tolerance:
        leaf = True
        if VERBOSE: 
            print(f'LEAF NODE REACHED: {node}')

    return leaf 


#test for exact equality
def arreq_in_list(myarr, list_arrays):
    """
    Small utility function that returns True if the array is in the list of arrays
    """
    return next((True for elem in list_arrays if array_equal(elem, myarr)), False)

    
def brouwer_dfs(domain: range, function: str, tolerance: float, range_step: float, 
                node_search_count: int = 0, visited_nodes = None, solved: bool = False, 
                VERBOSE: bool = False):
    """
    Depth First Search method to find the brouwer fixed point given a range and a continuous mapping function. 

    I based the DFS code on an old assignment from an artificial intelligence class at Dartmouth. 
    """

    # initialize solved
    solved = False

    # increment node_search_count
    node_search_count += 1

    # initialize the visited on nodes on the first call of this function
    if visited_nodes is None:
        visited_nodes = []
        # add the domain as a node 
        visited_nodes.append(domain)

    # BASE CASE #1: when we hit the tolerance limit then we know we're at a leaf node
    if is_leaf_node(node=domain, tolerance=tolerance, VERBOSE=VERBOSE):
        return solved

    # BASE CASE #2: When the problem is solved and the fixed point is found
    x = np.mean(domain)
    f_x = function(x)
    if VERBOSE: 
        print(f'x: {x}, f(x): {f_x}')
    if abs(x - f_x) < tolerance*10: 
        pretty_print_solution(x=x, f_x=f_x, method='Depth First Search', \
                              tolerance=tolerance, node_search_count=node_search_count)
        solved = True
        return solved

    # RECURSIVE CASE
    successor_nodes = dfs_get_successors(domain=domain, range_step=range_step)
    # find the nodes to search through 
    nodes_to_search = []
    for n in successor_nodes:
        if not arreq_in_list(n, visited_nodes):
            nodes_to_search.append(n)

    for node in nodes_to_search:
        if ((not arreq_in_list(myarr=node, list_arrays=visited_nodes)) & (solved is False)):
            if VERBOSE: 
                print(f'Node min: {np.min(node)}, Node max: {np.max(node)}')
            # node_search_count += 1

            visited_nodes.append(node)
            brouwer_dfs(domain=node, function=function, tolerance=tolerance, 
                        visited_nodes=visited_nodes, range_step=range_step, 
                        node_search_count=node_search_count, solved=solved)

    return solved 


def fixed_point(domain: range, function: str, tolerance: float, range_step: float, VERBOSE: bool):
    """
    This funciton takes a domain (continuous set of real values) and a function as arguments and returns a fixed point.     
    i.e. this function returns the point that satisfies f(x) = x. 

    :param: domain - python range object that represents a continuous set of real values
    :param: 
    """

    # Use DFS 
    brouwer_dfs(domain=domain, function=function, tolerance=tolerance, range_step=range_step, VERBOSE=VERBOSE)

    # Use Linear Search 
    brouwer_linear_search(domain=domain, function=function, tolerance=tolerance)


def main():
    
    # control excessive logging
    VERBOSE = False

    # define the domain over which we will search 
    range_step = 0.1
    domain = np.arange(0, 100, range_step)

    # define a tolerance so that we can find a solution within the chosen tolerance
    tolerance = 0.1

    # define some smooth, differentiable test functions to use
    function_1 = lambda x : 1 - 1/(math.e**x)
    function_2 = lambda x : 10 * math.sin(0.2*x) + 0.5*x + 2

    fixed_point(domain=domain, tolerance=tolerance, function=function_2, range_step=range_step, VERBOSE=VERBOSE)


if __name__ == "__main__":
    main()

