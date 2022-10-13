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

The pattern is pretty clear to see. It repeats over intervals of 4 values - see the diagram below. 

 <p align="center">
    <img src="https://github.com/spencerbertsch1/Game-Theory/blob/main/assignment_2/diagrams/fig_1.png?raw=true" alt="big graph" width="85%"/>
</p>

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

For example: 

```
x=1 --> g(x) = x   = 1
x=2 --> g(x) = x   = 2
x=3 --> g(x) = x+1 = 4
x=4 --> g(x) = x-1 = 3
...
```

And so on. We can see above that the values of x=99 and x=100 are swapped, so these values represent index 3 and index 4 in our 4-length pattern. This makes sense because 100%4=0, so the pattern should begin again at x=101. 