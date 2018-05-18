#### Pair Problem

Write a function that takes three arguments:

 * A list of lists, `X_train`, where each inner list is of length three and represents the position of a Wookiee in space, along the traditional `x`, `y`, and `z` axes.
 * A list of strings, `y`, the same length as the outer list `X_train`, where each string represents the color of a [Wookiee](https://en.wikipedia.org/wiki/Wookiee) at the corresponding position.
 * A list of lists, `X_test`, where each inner list is of length three and represents the position in space of a Wookiee of unknown color.

The function should produce a list of strings, the same length as the outer list, representing for each unknown Wookiee the color of the closest known Wookiee.

For example:

```python
X_train = [[1,   1,  1],
           [0,   0,  0],
           [-1, -1, -1],
           [10, 10, 10]]

y_train = ['red',
           'white',
           'blue',
           'chartreuse']

X_test = [[1.1, 1.1, 1.1]]

for result in your_function(X_train, y_train, X_test):
    print result
## red
```


##### Possible extensions:

 * Does your solution work for any number of features in the training data sets?
 * Does your solution handle ties?
 * Can you add another parameter, `k`, to your solution so that it uses the `k` nearest Wookiees instead of only the nearest Wookiee?
 * Can you add to your solution so that it has reasonable behavior if `y_train` is numeric?

An extension of another kind:

 * Are you confident that your solution is correct? How can you ensure that it is, and check that it stays correct in the future?
