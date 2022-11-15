# Assignment #4: N Person Games

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
   
2. `cd` to the assignment_4 directory by running the following command:
   1. `$ cd assignment_4`


## How to run Question 1(b): brouwer_fixed_point.py

#### This section will specifically describe problem `1(b)`.

1. Before running the brouwer_fixed_point.py script, ...

2. Run the following command to run the brouwer_fixed_point.py file: 
    1. `$ python3 brouwer_fixed_point.py`


- Here the continuous mapping function is: `f(x) = 10 * sin(0.2*x) + 0.5*x + 2`

Given this as the input expression, the fixed point can be found quite quickly using the depth-first search based method and it can be found -- albeit more inefficiently -- using the linear search function. See the below code output. 

``` 
Solution Found! 
------------------------------
Depth First Search Method fixed point solution -> x: 13.15, f(x): 13.471.         
Points match to within a tolerance of 0.1. 
------------------------------         
Number of nodes searched before finding a solution 7. 
------------------------------
 
Solution Found! 
------------------------------
Linear Method fixed point solution -> x: 13.3, f(x): 13.282.         
Points match to within a tolerance of 0.1. 
------------------------------         
Number of nodes searched before finding a solution 134. 
------------------------------
``` 




## How to run Question 2(c): bimatrix_tu_game.py

#### This section will specifically describe problem `2(c)`.

1. Run the following command to run the bimatrix_tu_game.py file: 
    1. `$ python3 bimatrix_tu_game.py`

2. You should see the solution printed with the following information: 

``` 
Original Bimatrix:
Payoff matrix for P0: 
 [[1 2 0]
 [4 1 2]
 [5 2 0]]
Payoff matrix for P1: 
 [[5 2 1]
 [2 0 1]
 [0 3 0]]
SOLUTION: 
 ------------------------- 
 Total Payoff Sigma: 6 
 Payoff Split Phi: (3.5, 2.5) 
 -------------------------
```

This solution matches the value that I got when doing this problem by hand, which is a good sign. Additionally, as per the assignment, I have also implemented a function that generated random bimatrix games with the following specifications: 


When you run the `bimatrix_tu_game.py` file with line 129 uncommented you will also see the output of a few solved random games: 

```
Shape of randomly generated Bimatrix: (97, 72)
SOLUTION: 
 ------------------------- 
 Total Payoff Sigma: 1963.0 
 Payoff Split Phi: (991.104, 971.896) 
 -------------------------


Shape of randomly generated Bimatrix: (47, 21)
SOLUTION: 
 ------------------------- 
 Total Payoff Sigma: 1846.0 
 Payoff Split Phi: (1031.4345, 814.5655) 
 -------------------------


Shape of randomly generated Bimatrix: (4, 30)
SOLUTION: 
 ------------------------- 
 Total Payoff Sigma: 1880.0 
 Payoff Split Phi: (597.537, 1282.463) 
 -------------------------
```

Although there's no relistic way to know if these solutions are correct, we can rest assured that the solutions we got for the smaller games match the solutions I got when solving the small TU games by hand. 