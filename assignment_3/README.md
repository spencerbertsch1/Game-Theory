# Assignment #3: Recursive Games

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

## How to run Question 1(a): Guess Target Card
1. Before running ... 

2. Run the following command to run the YYYY.py file: 
    1. `$ python3 YYYY.py`

After running the script, you should see the following output: 

## How to run Question 1(b): Sample Recursive Games

1. Before running the recursive_games.py script, feel free to change the main() function to run either problem `1_b_i` or problem `1_b_ii`. Feel free to leave both calls uncommented to that both parts of the problem will run. This is how I sil submit my assignment. 

### Problem 1_b_i

1. This section will specifically describe problem `1_b_ii`. 

2. Run the following command to run the recursive_games.py file with `main_i()` uncommented at the bottom of the file: 
    1. `$ python3 recursive_games.py`

3. You should see the solution printed with the following information: 

``` 
_____PAYOFF MATRIX_____ 
 [[0 3.0]
 [3.0 -1.0]]
Method 7 Success - Simplex method converged after 2 pivots.
Method 7 - Simplex ----- p: [0.57, 0.43] -----
Method 7 - Simplex ----- q: [0.57, 0.43] -----
Method 7 - Simplex ----- v: 1.29 -----
RECURSIVE SOLUTION - Final Value: 1.286
```

This solution matches the value that we get when solving this game by hand (9/7). 