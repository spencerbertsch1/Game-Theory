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