###Hints for Poisson GLM (Challenge Set 9) :fish: :fr:

Below are hints to get through first two exercises.  

Linear regression assumes normality of data. Poisson regression with log link function is useful to model count data, which follows the Poisson distribution. You will encounter this type of data in real-life problems, so this statistical model will be valuable for your data science toolkit.

Here are some hints:  

####9.1  
a) Load data.
```
data = pd.read_stata('ships.dta')
```

b) Create dummy variables for the categorical variables. eg.
```
ship_types = pd.get_dummies(data['type'], prefix='type')
```

c) Try running a GLM (without offset) with this data and see why it doesn’t work. (does it fit the assumptions?)
eg.
```
p_glm_no_offset = sm.GLM(Y, X, family=sm.families.Poisson(link=sm.families.links.log)).fit()
```  

This no-offset model will not work well and would yield a deviance of 70.5 and pearson's chi-squared of 65.8. Check with your model answers.


####9.2
Poisson regression is typically used to model count data. Often we need to model rates (counts per unit time) instead of counts. For example, in the ships data, it is not meaningful to treat 3 damages during 1 year and 3 damages during 10 years the same way. Hence we need to include an offset term in the model.

a) Take log of the offset variable (months). If not sure why this is done, do a scatterplot of y by x (y=damage, x=months) and see what the distribution looks like before and after the transformation.
```
logmonths = np.log(X.months)
```

b) When you use months of service as offset, exclude this variable from your X matrix. (If you include months in your X matrix, see what happens….)
```
p_glm_offset = sm.GLM(Y, X_no_months, offset=logmonths, family=sm.families.Poisson()).fit()
```

The with-offset model should work better and yield a deviance of 38.7 and pearson's chi-squared of 42.3. Check your model answers. 

---

####Starter Code

```python
# dummify rank
types = pd.get_dummies(data['type'], prefix='type')
construction = pd.get_dummies(data['construction'], prefix='construction')
operation    = pd.get_dummies(data['operation'], prefix='operation')

print types[:3]
print construction[:3]
print operation[:3]

dummies_only = pd.concat([types, construction,operation],axis=1)
#print '-'*75
#print dummies_only[:5]

# Getting the design matrix (sm_X) ready to input into the GLM. 
# Remove the redundant dummy columns; add a column for the constant
subset_dummy = dummies_only[["type_B","type_C","type_D", "type_E",
                             "construction_1965-70", "construction_1970-74", 
                             "construction_1975-79", "operation_1975-79"
                             ]]

sm_X = pd.concat([data.months, subset_dummy], axis=1)
sm_X = sm.add_constant(sm_X)

print sm_X.shape
sm_X.head()
```

```python
#9.2
## This is the correct model.
## You need to add the offset.

logmonths = np.log(sm_X.months)

glm_offset = sm.GLM(Y, X_no_months, offset=logmonths, family=sm.families.Poisson()).fit()
glm_offset.summary()

## Note: the offset parameter doesn't get its own covariate output. 
## The would-be coefficient for the offset is 
## forced to be 1 (or as close to 1 as possible).

print "Model:  offset = logmonths"
print "deviance:", glm_offset.deviance
print "pearson's chi-squared test statistic:", glm_offset.pearson_chi2
```
