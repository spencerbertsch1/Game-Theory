# Assignment #2: Two Person Zero Sum Games

ENGG 199.09, Game Theory  
Fall 2022, Dartmouth College  
Spencer Bertsch   

## To run the code: 

1. Clone [this github repository](https://github.com/spencerbertsch1/Game-Theory) locally and `cd` into the `Game-Theory` directory. 
Alternatively, if you acquired this code from a zip file, simply unzip the file locally, `cd` into the `Game-Theory` directory, and continue to Step 2. 
In order to run any of the test scripts in this repository, you will need python 3. 
   1. If you don't have python 3 installed, you can install Anaconda and create a new Conda environment using the following command:
      1. `$ conda create -n game_theory_env python=3.9`
   2. Then activate the new environment by running the following command:
       1. `$ conda activate game_theory_env`
   3. Then proceed to the following step. 
   

2. `cd` to the assignment_2 directory by running the following command:
   1. `$ cd assignment_2`

## How to run Question 1: 2-Person Zero Sum Games
1. Before running the 2-PZSG script, 

EDIT BELOW HERE

## How to run Question 6: G Function Calculator

1. Before running the G Function Calculator script, feel free to add a custom directed acyclic graph to the g_function_setup.py file under the `assignment_2` directory. Or you can use one of the existing graphs if you like.  

2. If you would like, update the graph that will be used in the by modifying line 111 of the `g_function_calculator.py` file. Then run the following command to run the g_function_calculator.py file: 
    1. `$ python3 g_function_calculator.py`

3. You should see the solution printed with the following information: 
 - The graph represented as a python dictionary 
 - The vertex (x)
 - The g-value g(x)
 - The P/N value of that vertex

Here in example run from a directed acyclic graph that we discussed in class: 

<p align="center">
    <img src="https://github.com/spencerbertsch1/Game-Theory/blob/main/assignment_2/diagrams/small_graph.png?raw=true" alt="small graph" width="40%"/>
</p>

```
 Calculating the g-values and P/N states for each vertex of the following graph: 
 {0: [], 1: [0], 2: [1, 0], 3: [2, 1, 0], 4: [3, 2, 1], 5: [4, 3, 2]} 
 Solution:
[['   x' '0' '1' '2' '3' '4' '5']
 ['g(x)' '0' '1' '2' '3' '0' '1']
 [' P/N' 'P' 'N' 'N' 'N' 'P' 'N']]
 ```

 As discussed in class, we can see that x is a P position iff x%4 = 0. 

 Just to ensure this code is working properly, I also tested it on a larger graph that still represents a 
 subtraction game with a subtraction set of s = {1, 2, 3}, but this time there are eleven vertices: 

 <p align="center">
    <img src="https://github.com/spencerbertsch1/Game-Theory/blob/main/assignment_2/diagrams/big_graph.png?raw=true" alt="big graph" width="60%"/>
</p>

The output can be seen below: 

```
Calculating the g-values and P/N states for each vertex of the following graph: 
 {0: [], 1: [0], 2: [1, 0], 3: [2, 1, 0], 4: [3, 2, 1], 5: [4, 3, 2], 6: [5, 4, 3], 7: [6, 5, 4], 8: [7, 6, 5], 9: [8, 7, 6], 10: [9, 8, 7]} 
 Solution:
[['   x' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' '10']
 ['g(x)' '0' '1' '2' '3' '0' '1' '2' '3' '0' '1' '2']
 [' P/N' 'P' 'N' 'N' 'N' 'P' 'N' 'N' 'N' 'P' 'N' 'N']]
```

As expected, again we see that x is a P position iff x%4 = 0. 