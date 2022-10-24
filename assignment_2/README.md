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

```
_____PAYOFF MATRIX_____ 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
 Reduced (intermediate) matrix: 
 [[1 2 3]
 [7 8 9]]
Reduced matrix: 
 [[1 3]
 [7 9]]
Method 3 successful! The matrix has been reduced to a 2 x 2. Passing the reduced matrix to Method 2.
Method 2 should not be used - this payoff matrix has a saddle point! Using Method 1 instead.
Method 1 - Saddle Points ----- p: [0. 1.] -----
Method 1 - Saddle Points ----- q: [1. 0.] -----
Method 1 - Saddle Points ----- v: 7 -----
Method 7 Success - Simplex method converged after 2 pivots.
Method 7 - Simplex ----- p: [0, 0, 1.0] -----
Method 7 - Simplex ----- q: [1.0, 0, 0] -----
Method 7 - Simplex ----- v: 7.0 -----
```

So here's an interesting example of how our recursive implementaiton of the dominant strategy reduction method worked. First the method removed the middle row because it was completely dominated by the bottom row for P1. Next, the method found that the center column was completely dominated by the right column. At this point the matrix was a 2x2, so it was passed to methods 2 and 1 to be completed. The solution matches the simplex method. 

### Example 4: 2xn or mx2 Matrices 

```
_____PAYOFF MATRIX_____ 
 [[2 3 1 5]
 [4 1 6 0]]
Method 4 - (n x 2) or (2 x m) ----- p: [0.6, 0.4] -----
Method 4 - (n x 2) or (2 x m) ----- q: [] -----
Method 4 - (n x 2) or (2 x m) ----- v: 0 -----
Method 7 Success - Simplex method converged after 2 pivots.
Method 7 - Simplex ----- p: [0.71, 0.29] -----
Method 7 - Simplex ----- q: [0, 0.71, 0.29, 0] -----
Method 7 - Simplex ----- v: 2.43 -----
```

We can see that the p-vector here almost matches, but we do have some differences between the mixed strategy for P2 we got using Method 4 and the mixed strategy for P2 we got using Simplex. I would trust the simplex soluiton! Let's move on. 

### Example 5: Fully Active Matrices - Principal of Indifference

```
_____PAYOFF MATRIX_____ 
 [[ 0  1 -2]
 [ 1 -2  3]
 [-2  3 -4]]
Method 5 - Principal of Indifference ----- p: [0.25 0.5  0.25] -----
Method 5 - Principal of Indifference ----- q: [0.25 0.5  0.25] -----
Method 5 - Principal of Indifference ----- v: 0.0 -----
Method 7 Success - Simplex method converged after 3 pivots.
Method 7 - Simplex ----- p: [0.25, 0.5, 0.25] -----
Method 7 - Simplex ----- q: [0.25, 0.5, 0.25] -----
Method 7 - Simplex ----- v: 0.0 -----
```

Here we can see an example in which we were able to reduce the matrix down to a system of linear equations that was solved using the `numpy.linalg.solve()` method. The solution matches what we get from Simplex. 

### Example 6: Fully Active Matrices - Principal of Indifference

```
_____PAYOFF MATRIX_____ 
 [[ 1 -2  3 -4]
 [ 0  1 -2  3]
 [ 0  0  1 -2]
 [ 0  0  0  1]]
Method 1 complete. No saddle point found. Passing...
Method 6 - Formula for non-degenerate n x n ----- p: [0.08 0.25 0.33 0.33] -----
Method 6 - Formula for non-degenerate n x n ----- q: [0.33 0.33 0.25 0.08] -----
Method 6 - Formula for non-degenerate n x n ----- v: 0.08 -----
Method 7 Success - Simplex method converged after 4 pivots.
Method 7 - Simplex ----- p: [0.08, 0.25, 0.33, 0.33] -----
Method 7 - Simplex ----- q: [0.33, 0.33, 0.25, 0.08] -----
Method 7 - Simplex ----- v: 0.08 -----
```

Here we see Method six functioning successfully for a nonsingular input matrix. The output matches the Simplex method. 

### Example 7: Simplex Method
```
_____PAYOFF MATRIX_____ 
 [[ 1  7  3]
 [13  5  6]
 [ 7  8  9]]
Method 7 Success - Simplex method converged after 2 pivots.
Method 7 - Simplex ----- p: [0, 0.11, 0.89] -----
Method 7 - Simplex ----- q: [0.33, 0.67, 0] -----
Method 7 - Simplex ----- v: 7.67 -----
```

I have used the simplex method as a benchmark through out this assignment. As far as I can tell it works on every input matrix I have used. 


### Random Matrix Generation and Solving

In addition to implementing these methods, I also created a script that generates 100 random matrices where the following rules hold: 
- Random values of m rows where 1 <= m <= 100
- Random values of n columns where 1 <= n <= 100
- Random element values where -1000 <= a_ij <= 1000

Feel free to run gambit_test.py to see a few example outputs - I will add one below as well. 

```
_____PAYOFF MATRIX_____ 
 [[ 549. -634. -626. -257.  235. -589.  297. -947.  240.]
 [-111. -384. -475. -615. -144.  945.  876. -205.  858.]
 [ 220. -134. -493.  -84.  574.  993. -280.  912. -600.]
 [-219. -881. -448.  126. -127. -779. -959.  297.  979.]
 [-617.  889. -213.  130.  543. -878.  763.  308.  509.]
 [ -72.  -55.   60.  976.  905.  864.  667. -949.  893.]
 [ 402.  247. -925. -760. -238.  671.  886.  634.   37.]
 [ 944.  172.  551. -560.  875.  933. -603.  714.  815.]
 [-989.  487.  -78. -240.  390. -930.  946.  359.  -48.]
 [ 205.  520.   20. -417. -600.  -31.  929.  567.  606.]
 [-810. -974. -587.  789.  550.  794. -484.  274. -470.]
 [-609.  -52. -609.  351.  139. -593.  922. -641. -857.]
 [ 717. -160. -670.  529.   96.  969. -483. -363.  942.]
 [ 451.  965. -252. -588.  405. -186.  741. -165. -522.]
 [ 771.  -60. -310.  345.  251. -571. -860. -664.  208.]
 [ 736.   20. -832.  248.  894.  827. -777. -131. -702.]
 [ 864.  390. -575.  485.  359.  730. -242.  304. -513.]
 [ -61. -712. -499. -374.  330.  425.  804.  145.  354.]
 [ 313. -355. -794.  661.  700. -367.  283.  417.   33.]
 [-207.  872. -680.  346.  830. -332.  953.  802.  623.]
 [-809.  287.  690.  298.  534. -906. -577. -127.  266.]
 [ 416. -923. -914.  326.  290.  -46. -963.  571. -829.]
 [-711.  634.  562.  807. -631.  883.  713. -591.  432.]
 [-122.  256.  395. -380.  662. -763. -133. -308. -596.]
 [-230.  255.  -63.  615. -570. -699. -745. -995.  139.]
 [ 519.  849.  332.  541. -781. -865. -977. -383.  942.]
 [-816. -234. -198. -132. -123. -138.  643.  836.   31.]
 [  32.  524.  130. -349.  793.  789.  411. -347.  -95.]
 [-231.  556.  873. -985.  813.  641.  970.   72.  442.]
 [ 122. -309.  -68.  120.  217. -835.  347.  836. -687.]
 [-276.   57.  956.  141. -616.  282. -207. -584. -432.]
 [ 815. -794.  519. -599. -678.  -27.  348.  388. -953.]
 [-848.   79.  347. -813.  465. -511. -988.  718. -790.]]
Method 7 Success - Simplex method converged after 19 pivots.
Method 7 - Simplex ----- p: [0, 0, 0, 0, 0, 0.08, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0.11, 0, 0, 0.07, 0, 0, 0.26, 0, 0, 0, 0, 0, 0, 0.17, 0, 0.06, 0] -----
Method 7 - Simplex ----- q: [0.21, 0.03, 0.2, 0.25, 0, 0, 0.15, 0.15, 0.01] -----
Method 7 - Simplex ----- v: 203.01 -----
```

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