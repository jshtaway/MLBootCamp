#### Pair Problem

These problems involves first doing some math, either in your head or with pencil and paper, and only afterward verifying with Python.

For each problem, there is a matrix `X` and a vector `y`. You are looking for a vector `w` so that when you take a row of `X` and multiply each element by its corresponding element of `w` and then sum the results (the dot product of the row of `X` with `w`) you get the value at the corresponding position of `y`. For example, if we have:

```
X = [[5, 3, 7],   y = [537,
     [2, 4, 1]]        241]
```

A solution is `w = [100, 10, 1]`.

For each problem, answer two things:

 1. How many solutions are there? Why?
 2. If there are any solutions, what is one?


Problem A:

```
X = [[2]]        y = [8]
```

One solution: w = [4]


Problem B:

```
X = [[0]]        y = [8]
```

No solutions; zero is no good.


Problem C:

```
X = [[2, 4]]     y = [8]
```

Infinitely many solutions.


Problem D:

```
X = [[2, 4],     y = [8,
     [0, 1]]          3]
```

```
import numpy as np
Xd = np.array([[2, 4], [0, 1]])
yd = np.array([8, 3])
wd = np.array([-2, 3])
Xd.dot(wd)               # confirm
np.linalg.solve(Xd, yd)  # find
```


Problem E:

```
X = [[2, 4],     y = [8,
     [0, 1],          3,
     [9, 5]]          1]
```

No solutions; conflicting constraints.


Problem F:

```
X = [[2, 2],     y = [4,
     [3, 3]]          6]
```

Colinearity! Infinitely many solutions.


Problem G:

```
X = [['dog'],    y = [8,
     ['cat']]         6]
```

THIS DOESN'T MAKE ANY SENSE.


Problem H:

```
X = [[1, 0],    y = [8,
     [0, 1]]         6]
```

Oh good.


Problem I:

```
X = [[1, 1, 0],    y = [8,
     [1, 0, 1]]         6]
```

Nope!


Problem J:

```
X = [[1, 0],    y = [8,
     [1, 1]]         6]
```

Yup!


After finishing the problems, use `numpy` to check your solutions. Can you use `numpy` to _find_ solutions?
