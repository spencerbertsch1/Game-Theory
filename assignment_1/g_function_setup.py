"""
-------------------------------
| Dartmouth College           |
| ENGG 199.09 - Game Theory   |
| Fall 2022                   |
| Spencer Bertsch             |
-------------------------------

Assignment #1 - Problem #6) G Function Calculator

This script contains the dictionary representations of the graphs used in the 
g_function_calculator.py script. 
"""

class Graphs: 
    # Here the subtraction set is: {1, 2, 3}
    graph1: dict = {
        0: [],
        1: [0], 
        2: [1, 0], 
        3: [2, 1, 0], 
        4: [3, 2, 1],
        5: [4, 3, 2]
    }

    # Here the subtraction set is: {1, 2, 3}, but the graph goes up to 10. 
    graph2: dict = {
        0: [],
        1: [0], 
        2: [1, 0], 
        3: [2, 1, 0], 
        4: [3, 2, 1],
        5: [4, 3, 2],
        6: [5, 4, 3], 
        7: [6, 5, 4],
        8: [7, 6, 5], 
        9: [8, 7, 6], 
        10: [9, 8, 7]
    }

    # Here we represent the graph from problem 4 to check the answer
    graph3: dict = {
        1: [2, 3, 10],
        2: [3, 4], 
        3: [5, 9], 
        4: [6], 
        5: [4, 6],
        6: [7],
        7: [15], 
        8: [7, 14],
        9: [6, 7, 8], 
        10: [8, 9, 11, 12], 
        11: [8, 13],
        12: [], 
        13: [], 
        14: [], 
        15: []
    }