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

## How to run Question 3 (a): Take and Break

1. Before running the G Function Calculator script, feel free to add a custom directed acyclic graph to the g_function_setup.py file under the `assignment_2` directory. Or you can use one of the existing graphs if you like.  

2. If you would like, update the graph that will be used in the by modifying line 111 of the `g_function_calculator.py` file. Then run the following command to run the g_function_calculator.py file: 
    1. `$ python3 g_function_calculator.py`

3. You should see the solution printed with the following information: 
 - Each g(x) value printed between x=0 and x=100. 


```
g(0)=0
g(1)=1
g(2)=2
g(3)=4
g(4)=3
g(5)=5
g(6)=6
g(7)=8
g(8)=7
g(9)=9
g(10)=10
... 
g(90)=90
g(91)=92
g(92)=91
g(93)=93
g(94)=94
g(95)=96
g(96)=95
g(97)=97
g(98)=98
g(99)=100
g(100)=99
 ```

 I'm not sure if there's a closed form solution here, but the pattern is clear to see: 

 <p align="center">
    <img src="https://github.com/spencerbertsch1/Game-Theory/blob/main/assignment_2/diagrams/fig_1.png?raw=true" alt="big graph" width="85%"/>
</p>

The pattern repeats over every interval of 4 values.

```
x=1 --> g(x) = x   = 1
x=2 --> g(x) = x   = 2
x=3 --> g(x) = x+1 = 4
x=4 --> g(x) = x-1 = 3
```