# Assignment #1

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
   

2. `cd` to the assignment_1 directory by running the following command:
   1. `$ cd assignment_1`

## How to run Question 5: Nim Player
1. Before running the Nim Player script, feel free to add a custom nim_board to the nim_setup.py file under the `assignment_1` directory. You can use existing game boards or add your own. 

2. If you would like, update the board that will be used in the nim_game by modifying line 109 of the `nim_player.py` file. Then run the following command to run the nim_player.py file: `$ python3 nim_player.py`

3. You will see the all the moves that place the user into a P position. Output will look as follows: 
```
Solving the following Nim Game board: [5, 12, 13]
The following move places us in a P position: [-4, 0, 0]
The following move places us in a P position: [0, -4, 0]
The following move places us in a P position: [0, 0, -4]
```

## How to run Question 6: G Function Calculator

1. 