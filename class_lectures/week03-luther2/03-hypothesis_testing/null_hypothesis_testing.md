# Null Hypothesis Testing


I claim that I can use mystical abilities to predict the outcome of coin flips.

You don't think I can.

How can we test it?

We do an experiment in which I call 100 coin flips. I get 60 right.

Am I special or not?

---

The hypothesis that I'm not special, the "null hypothesis", is that my true rate of flip prediction is 0.5. But even under this hypothesis, I could get 60 out of 100 right. So did I get lucky (by random chance) or am I mystical?

The interesting claim, or "alternative hypothesis", is that my true rate of flip prediction is greater than 0.5.

The thing we're measuring from the experiment, or "test statistic", is the number of correct flip predictions out of 100.

If the null hypothesis is correct, the test statistic is binomial distributed with parameters `n = 100` and `p = 0.5`. That is, if we repeated the whole experiment many times, we would see such a distribution for all the results.

So if the null hypothesis is correct, how likely is it that I got 60 or more coin flips correct?

Before we check (really, before we do the experiment) we decide what would convince us that I have ESP. The choice of a cutoff at 5% probability is common. That is, if we would only see data as extreme as we've seen less than 5% of the time, we'll say that seems too unlikely and we will conclude that we don't think the null hypothesis is true.

---

In the case of the binomial distribution, which is discrete and not too complicated mathematically, we could just work out the probability. But in general we'll rely on some existing functionality. (In a traditional statistics class, this is the part where we'd turn to a table in the back of the book.)

```python
from scipy.stats import binom
print(1 - binom.cdf(60, 100, 0.5))
# 0.017600100108852379
```

The probability of getting 60 or more correct is about 1.8%. This is less than 5%, so we reject the null hypothesis and (maybe) conclude that I have mystical coin powers.

---

Conversely, we can figure out what the 95% cutoff is beforehand.

```python
from scipy.stats import binom
print(binom.ppf(0.95,100,0.5))
# 58
```

Which means, one should get 58 tosses or more to be considered clairvoyant. And we will say the person has predictive power with a confidence level of 95%.

---

What about confidence intervals?

When using a coin, a hundred tosses sounds good. But let's change the problem. Let's say, someone says, "I can look at a person's address and predict if they are republican or democrat." Say you pull 100 random people from your town and test the claim against a confidence level of 95%. Next you do the same with 100 random people from the entire country. Are these two the same?

As soon as there is variation in population, the size of your sample in relation to your population becomes important. Based on your sample size, you end up getting a confidence interval around your result.

This link provides a nifty calculator: http://www.surveysystem.com/sscalc.htm#one

---

The example(s) above are given for illustrative purposes; it's much more common to test using statistics that have different distributions: chi-squared, t, f, and z (normal) are all common.

---

The machinery of null hypothesis testing comes up in linear regression diagnostics, and we may or may not care. An even more practical application is in A/B testing (more generally "split testing") in which we want to find out if a different rate of clicks (etc.) under two (or more) conditions is due to random chance or due to a real difference in performance between the conditions.
