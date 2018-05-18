Consider a three-class classification problem as follows:

There are three types of coins that we choose from randomly. C1 is a fair coin (1/2 probability of flipping heads), the others are unfair: ( C2 1/3 and C3 1/4 chance of heads).

Our observed data is two features: whether or not heads occurs in each of 2 coin flips. For example our features x1, x2 and true labels might look like:

x1 | x2 | y  

1  | 1  | C1  
1  | 1  | C2  
1  | 0  | C2  
0  | 1  | C3  
0  | 0  | C1  
0  | 0  | C3

Using Bayes' theorem, design a model that predicts which coin was flipped based on the two flip results we observe. You should assume that all coins are equally likely to be chosen.

Are x1 and x2 independent? What about conditionally independent given y?    

Hint: Make it concrete with an example - e.g. start by computing the probability that flipping C3 produced 2 heads.
