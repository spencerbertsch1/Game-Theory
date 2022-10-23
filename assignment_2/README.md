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
1. Before running the `zero_sum.py` script, feel free to change the payoff matrix that's being tested by changing the `PayoffMatrices.mat11` 
line in in the `main()` function of `zero_sum.py`. 

2. Run the following command to run the zero_sum.py file: 
    1. `$ python3 zero_sum.py`

After running the script, you should see many different results based on which of the seven methods are being used and which of the 
payoff matrices was loaded. Let's go through a few examples: 

### Example 1: Saddle Point Matrix
```
_____PAYOFF MATRIX_____ 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Method 1 - Saddle Points ----- p: [0. 0. 1.] -----
Method 1 - Saddle Points ----- q: [1. 0. 0.] -----
Method 1 - Saddle Points ----- v: 7 -----
Method 7 Success - Simplex method converged after 2 pivots.
Method 7 - Simplex ----- p: [0, 0, 1.0] -----
Method 7 - Simplex ----- q: [1.0, 0, 0] -----
Method 7 - Simplex ----- v: 7.0 -----
```

We see that Method 1 was able to find the saddle point and the output matches the simplex method (which correctly handles all cases). Let's look at another case. 

### Example 2: Non-Saddle Point 2x2 Matrix
```
_____PAYOFF MATRIX_____ 
 [[9 2]
 [3 5]]
Method 1 complete. No saddle point found. Passing...
Method 1 complete. No saddle point found. Passing...
Method 2 - 2x2 Formulas ----- p: [0.22, 0.78] -----
Method 2 - 2x2 Formulas ----- q: [0.33, 0.67] -----
Method 2 - 2x2 Formulas ----- v: 4.33 -----
Method 7 Success - Simplex method converged after 2 pivots.
Method 7 - Simplex ----- p: [0.22, 0.78] -----
Method 7 - Simplex ----- q: [0.33, 0.67] -----
Method 7 - Simplex ----- v: 4.33 -----
```

We see that Method 2 was able to generate the correct answer given a 2x2 matrix. The solution matches our simplex method. Let's look at another example: 

### Example 3: Dominant Strategy Reduction 




## How to run Question 3 (a): Take and Break

1. Before running the take_and_break.py script, feel free to change the number of (x) values that are tested and printed to the console by altering line 114 of take_and_break.py. 

2. Run the following command to run the take_and_break.py file: 
    1. `$ python3 take_and_break.py`

3. You should see the solution printed with the following information: 
 - Each g(x) value printed between x=0 and x=100. 

```
g(0)=0                  g(90)=89
g(1)=1                  g(91)=92
g(2)=2                  g(92)=91
g(3)=4                  g(93)=94
g(4)=3                  g(94)=93
g(5)=6         ...      g(95)=96
g(6)=5                  g(96)=95
g(7)=8                  g(97)=98
g(8)=7                  g(98)=97
g(9)=10                 g(99)=100
g(10)=9                 g(100)=99
```

Here is some pseudocode that shows the logic needed to generate g(x) for any input x: 

```
if (x==0 or x==1 or x==2):
    g(x)=x
else:
    if x%2=0: g(x) = x-1
    if x%2=1: g(x) = x+1
```

**The pattern is as follows:**  

If x is 0, 1, or 2, then g(x) = x. If x is greater than 2, then g(x) = x+1 if x is odd, and g(x) = g-1 if x is even. 

### Sub-problem: If we assume that we should take the nim sum of the g-values of each pile
- I wasn't exactly sure whether the assignment instructions were telling us to take the nim sum of the number of chips in each pile. or the nim sum of the g-values of the number of chips in each pile. I programmed both cases, however, and I'm also listing the solution for the latter case. If the previous case turns out to be correct, this section can safely be ignored, or pondered upon as an interesting experiment. 

```
g(0)=0                  g(90)=90
g(1)=1                  g(91)=92
g(2)=2                  g(92)=91
g(3)=4                  g(93)=93
g(4)=3                  g(94)=94
g(5)=5       ...        g(95)=96
g(6)=6                  g(96)=95
g(7)=8                  g(97)=97
g(8)=7                  g(98)=98
g(9)=9                  g(99)=100
g(10)=10                g(100)=99
```

Here is some pseudocode that shows the logic needed to generate g(x) for any input x: 

```
if x==0:
    g(x)=0
else:
    if x%4=0: g(x) = x-1
    if x%4=1: g(x) = x
    if x%4=2: g(x) = x
    if x%4=3: g(x) = x+1
```

We can see this is slightly different than the expression for g(x) if we assume the assignment instructions tell us to use the nin sum of the number of chips in each pile. 