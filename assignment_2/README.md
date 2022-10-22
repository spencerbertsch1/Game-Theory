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
1. Before running the zero_sum.py script, 

EDIT BELOW HERE

## How to run Question 3 (a): Take and Break

1. Before running the take_and_break.py script, feel free to change the number of (x) values that are tested and printed to the console by altering line 112 of take_and_break.py. 

1. Run the following command to run the take_and_break.py file: 
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