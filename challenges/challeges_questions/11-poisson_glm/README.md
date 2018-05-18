### Poisson GLM Challenges

#### Data for the Challenges

We are going to fit a model to count data. The first one we will use is about the total count of damage incidents to ships. You can get it here:

[http://data.princeton.edu/wws509/datasets/ships.dta](http://data.princeton.edu/wws509/datasets/ships.dta)

We are stealing this dataset from STATA, so it's in STATA format. Pandas has a reader for that format to make your life easy:

```python
from pandas.io.stata import StataReader
reader = StataReader('ships.dta')
dataframe = reader.data()
```

Here are some details on this dataset:

The file has 34 rows corresponding to the observed combinations of type of ship, year of construction and period of operation. Each row has information on five variables as follows:

 * ship type, coded 1-5 for A, B, C, D and E,
 * year of construction (1=1960-64, 2=1965-70, 3=1970-74, 4=1975-79),
 * period of operation (1=1960-74, 2=1975-79)
 * months of service, ranging from 63 to 20,370, and
 * damage incidents, ranging from 0 to 53.

Note that there no ships of type E built in 1960-64, and that ships built in 1970-74 could not have operated in 1960-74. These combinations are omitted from the data file.


#### Challenge 1

Model the damage incident counts with a Poisson Regression.

> Hint: You can look at the previous ipython notebook with the logistic GLM example to see how you can do GLM with statsmodels

Remember that you will have to create dummy variables for categorical variables, and if you have time bins (like "1960-1964"), you have the option of either a) treating each bin as a category (and create dummies for each bin), or b) treat it as a continuous variable and take the mid-value (1962). Also remember to add a constant (to model the intercept).

Take a look at the statsmodels summary table, the goodness of fit indicators (Deviance, Pearson's chi square statistic) and the coefficients. Is this a good model?


#### Challenge 2

The months of service provides the time interval in which a ship has chances to acquire damages. It can be thought of "exposure", and this column can be used as an offset.

You can check these two resources for a quick idea on exposure and using an offset:

 * [Offset in Wikipedia](http://en.wikipedia.org/wiki/Poisson_regression#.22Exposure.22_and_offset)
 * [When to use an offset in CrossValidated (StackOverflow for statistics)](http://stats.stackexchange.com/questions/11182/when-to-use-an-offset-in-a-poisson-regression)

Try your model with months of service as the offset. Does it perform better?


#### Challenge 3

Now separate your data (even though it's only 14 rows) into a training and test set (your test will only be 4 or 5 rows), and check if you predict well (you can look at mean absolute error or mean squared error using ```sklearn.metrics```).


#### Challenge 4

_Deviance_. Compute the difference in Deviance statistics for your model and the null model. This is called the _null deviance_. You can do this in one of 2 ways:

 1. We need the deviance for the null model (a model where none of the explanatory variables are used; it's just a model with a mean guess). To do that, fit a poisson regression with only a constant. Get the deviance for this null model. Take the difference of deviances between your model and this null model.
 2. Use `statsmodels.genmod.generalized_linear_model.GLMResults`

Check if this difference is extreme enough that we can reject the null hypothesis. If we can't reject the null hypothesis, we cannot say that this model tells us more than that trivial, null model. To calculate the p-value (prob. of getting a deviance difference at least as extreme as this under the null hypothesis), we need to do a hypothesis test.

You can import the chi square test from scipy for this:

```python
from scipy.stats import chisqprob
```

Is your model better than the null model?


#### Challenge 5

Now, instead of a poisson regression, do an ordinary least squares regression with log Y. Compare the models. Are the coefficients close? Do they perform similarly?


#### Challenge 6

Now, let's do this on another dataset: Smoking and Cancer. You can get it here:

[http://data.princeton.edu/wws509/datasets/smoking.dta](http://data.princeton.edu/wws509/datasets/smoking.dta)

This dataset has information on lung cancer deaths by age and smoking status. It has these columns:

 * age: in five-year age groups coded 1 to 9 for 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80+.
 * smoking status: coded 1 = doesn't smoke, 2 = smokes cigars or pipe only, 3 = smokes cigarrettes and cigar or pipe, and 4 = smokes cigarrettes only,
 * population: in hundreds of thousands
 * deaths: number of lung cancer deaths in a year.

That population looks a lot like an offset!

Fit poisson and OLS models and compare them.

_Bonus_: try all these things in R! Your numerical answers should all be the same.
