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

1. Before running the recursive_games.py script, feel free to change the main() function to run either problem `1_b_i` or problem `1_b_ii`. Feel free to leave both calls uncommented to that both parts of the problem will run. This is how I will submit my assignment. 

### Problem 2(c)

1. This section will specifically describe problem `2(c)`.

2. Run the following command to run the bimatrix_tu_game.py file: 
    1. `$ python3 bimatrix_tu_game.py`

Methods: 
-  Find sigma (the total payoff) using the following expression: sigma = MAX(a_ij + b_ij)
-  Find delta using the following expression: delta = val(A - B)
    - Here (A-B) represents the matrix that we get if we subtract all P1 payoffs from P2 payoffs (a_ij - b_ij)
- Find phi (the payoff split) using the following expression: ((sigma + delta)/2, (sigma - delta)/2)
- And we're done! Now we just log the total payoff (sigma) and the payoff split (phi). 

3. You should see the solution printed with the following information: 

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