#### Pair Problem

Practice Lasso regularization technique in five steps:

1) Load Diabetes Dataset from SK Learn (`sklearn.datasets.load_diabetes()`).  Note that data may already be normalized.

2) Use the KFold function from sklearn's cross validation module to divide the data into 5 training/test sets.  Randomize the KFold (via the shuffle parameter with Random State of 0).

3) Tune the lambda (alpha) parameter in the lasso model by looping over a grid of possible lambdas (sklearn: lasso)

```
For each candidate lambda, loop over the 5 training/test sets.  
On each training/test set run the lasso model on the training set and then compute and record the prediction error in the test set.  
Finally total the prediction error for the 5 training/test sets.
```

4) Set lambda to be the value that minimizes prediction error.

5) Run the lasso model again with the optimal lambda determined in step 3. Which variables would you consider excluding on the basis of these results?

6) Try with Ridge and ElasticNet and base LinearRegression Models.  Compare your results.

Report the best score.

**Extra Credit**:  Try some Feature Engineering (Polynomials etc) to fit the data better.  Plot the data to see relationships.
