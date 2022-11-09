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
1. Run the following command to run the guess_it.py file:
    1. `$ python3 guess_it.py`

After running the script, you should see the following output:

```-----  Solution to G(m=1, n=1): v=0.5, p=[0.67, 0.33], q=[0.5, 0.5]  -----
-----  Solution to G(m=1, n=2): v=0.63, p=[0.67, 0.33], q=[0.56, 0.44]  -----
-----  Solution to G(m=1, n=3): v=0.67, p=[0.74, 0.26], q=[0.45, 0.55]  -----
-----  Solution to G(m=1, n=4): v=0.72, p=[0.79, 0.21], q=[0.38, 0.62]  -----
-----  Solution to G(m=1, n=5): v=0.75, p=[0.82, 0.18], q=[0.33, 0.67]  -----
-----  Solution to G(m=1, n=6): v=0.78, p=[0.85, 0.15], q=[0.29, 0.71]  -----
-----  Solution to G(m=2, n=1): v=0.5, p=[0.67, 0.33], q=[0.5, 0.5]  -----
-----  Solution to G(m=2, n=2): v=0.5, p=[0.67, 0.33], q=[0.75, 0.25]  -----
-----  Solution to G(m=2, n=3): v=0.46, p=[0.71, 0.29], q=[0.86, 0.14]  -----
-----  Solution to G(m=2, n=4): v=0.43, p=[0, 1.0], q=[1.0, 0]  -----
-----  Solution to G(m=2, n=5): v=0.48, p=[0, 1.0], q=[1.0, 0]  -----
-----  Solution to G(m=2, n=6): v=0.45, p=[0, 1.0], q=[1.0, 0]  -----
-----  Solution to G(m=3, n=1): v=0.5, p=[0.67, 0.33], q=[0.5, 0.5]  -----
-----  Solution to G(m=3, n=2): v=0.56, p=[0.67, 0.33], q=[0.67, 0.33]  -----
-----  Solution to G(m=3, n=3): v=0.57, p=[0.73, 0.27], q=[0.65, 0.35]  -----
-----  Solution to G(m=3, n=4): v=0.58, p=[0.77, 0.23], q=[0.64, 0.36]  -----
-----  Solution to G(m=3, n=5): v=0.55, p=[0.8, 0.2], q=[0.69, 0.31]  -----
-----  Solution to G(m=3, n=6): v=0.57, p=[0.81, 0.19], q=[0.7, 0.3]  -----
-----  Solution to G(m=4, n=1): v=0.5, p=[0.67, 0.33], q=[0.5, 0.5]  -----
-----  Solution to G(m=4, n=2): v=0.53, p=[0.67, 0.33], q=[0.71, 0.29]  -----
-----  Solution to G(m=4, n=3): v=0.51, p=[0.72, 0.28], q=[0.75, 0.25]  -----
-----  Solution to G(m=4, n=4): v=0.5, p=[0.75, 0.25], q=[0.82, 0.18]  -----
-----  Solution to G(m=4, n=5): v=0.51, p=[0.78, 0.22], q=[0.83, 0.17]  -----
-----  Solution to G(m=4, n=6): v=0.49, p=[0.8, 0.2], q=[0.87, 0.13]  -----
-----  Solution to G(m=5, n=1): v=0.5, p=[0.67, 0.33], q=[0.5, 0.5]  -----
-----  Solution to G(m=5, n=2): v=0.54, p=[0.67, 0.33], q=[0.69, 0.31]  -----
-----  Solution to G(m=5, n=3): v=0.54, p=[0.72, 0.28], q=[0.7, 0.3]  -----
-----  Solution to G(m=5, n=4): v=0.54, p=[0.76, 0.24], q=[0.72, 0.28]  -----
-----  Solution to G(m=5, n=5): v=0.53, p=[0.79, 0.21], q=[0.76, 0.24]  -----
-----  Solution to G(m=5, n=6): v=0.55, p=[0.81, 0.19], q=[0.76, 0.24]  -----
-----  Solution to G(m=6, n=1): v=0.5, p=[0.67, 0.33], q=[0.5, 0.5]  -----
-----  Solution to G(m=6, n=2): v=0.54, p=[0.67, 0.33], q=[0.69, 0.31]  -----
-----  Solution to G(m=6, n=3): v=0.53, p=[0.72, 0.28], q=[0.72, 0.28]  -----
-----  Solution to G(m=6, n=4): v=0.52, p=[0.76, 0.24], q=[0.77, 0.23]  -----
-----  Solution to G(m=6, n=5): v=0.52, p=[0.78, 0.22], q=[0.79, 0.21]  -----
-----  Solution to G(m=6, n=6): v=0.51, p=[0.8, 0.2], q=[0.84, 0.16]  -----
```

The solution G(m=1, n=1): 0.5 matches what we found in class.

## How to run Question 1(b): Sample Recursive Games

1. Before running the recursive_games.py script, feel free to change the main() function to run either problem `1_b_i` or problem `1_b_ii`. Feel free to leave both calls uncommented to that both parts of the problem will run. This is how I will submit my assignment.

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
RECURSIVE SOLUTION 
 Value: 1.286 
 p: [0.57, 0.43] 
 q: [0.57, 0.43]
```

This solution matches the value that we get when solving this game by hand 9/7 (1.286 when rounded to 3 decimals). 
