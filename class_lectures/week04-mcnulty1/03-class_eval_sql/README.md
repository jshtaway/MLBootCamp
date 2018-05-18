### Plan for Wednesday, October 11

#### Overview

For regression we had a few different metrics for evaluation ($r^2$, MSE, RMSE, etc).  For classification we will have **even more**.  So this morning we'll chat about various **Classification Evaluation Metrics** and why they exist.  For the next few days we'll take a detour from classification algorithms to build up other skills to apply to your Project McNulty.  Lastly, we'll keep skilling up on **SQL** today!

#### Schedule

**9:15 am**: Breakfast coffee!

**9:30 am**: [Pair Problem](pair.md)

| Student 1 | Student 2 |
|---|---|
| Rebekah | Jeff |
| Trent | Laura |
| Kalgi | Kenny |
| Pradnya | Yanxi |
| Chuoran | Sufyan |
| Mike | Andre |
| Michael | Carl |

**10:30 am**: Error metrics for classification
* [Slides](Classification_Errors.pdf)
* [Notebook](Classification_Errors.ipynb)

**11:30 am**: [Intro to SQL](intro_to_sql_notes.md)

**12:00pm**: Lunch

**1:30 pm**: Investigation Presentation: Michael Lin on Analyzing YouTube Comments

**1:45pm**: [SQL Lab](SQL_lab.md)

### More on structuring data, databases, and SQL

 * You could go through Zed Shaw's [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/), which will still take you through lots of SQL with SQLite.
 * For more introductory SQL, check out the [Mode Analytics "SQL School"](http://sqlschool.modeanalytics.com/).


### More on Error Metrics

 * [Precision, recall, sensitivity, specificity](http://uberpython.wordpress.com/2012/01/01/precision-recall-sensitivity-and-specificity/)
 * [Wikipedia page on precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall)
 * [Scikit learn on classification metrics](http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
 * [Receiver Operating Characteristic](http://gim.unmc.edu/dxtests/roc2.htm)
 * [Area under curve (ROC)](http://gim.unmc.edu/dxtests/roc3.htm)


##### What is the relationship between F1 and Fß?

If you have found the [metrics function](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html) in `sklearn` that spits out your precision, recall, and F score, you might have found yourself asking: "What is Fß? Is it the same as F1?"

The answer is ... yes. F1 combines precision and recall. Fß does
the same thing, but uses a weight so that you can weigh one of these
two (precision or recall) more than the other when combining them. It
is a way to tune your score if you care more about precision than
recall, for example. F1 is the Fß for which ß = 1. In
`sklearn`, the default value for ß is 1.

The [wikipedia page](http://en.wikipedia.org/wiki/F1_score) has more on this relationship.
