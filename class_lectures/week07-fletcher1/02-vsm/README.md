### Plan for Wednesday, May 24

#### Overview

Today we'll talk about **Vector Space Models** for NLP.  Our goal for all of these is just finding the best method to turn words into vectors.  Once we've done that, we can do just about anything :smile:


**Remember:**
* Try to have your Fletcher ideas finalized today, and data by Friday

#### Schedule

**9:15 am**: LET'S GO

**9:30 am**: Pair Programming:  
  * Pair: [Clustering Digits](pair.ipynb)   

Pairings:  

| Student 1 | Student 2 |
|---|---|
| Orlando | Walter |
| Sonal | Previous Group |
| Kenny | Guo |
| Alexander | Andrew |
| Doug | Emily |
| Toni | Kailin |
| Timan | Paul |
| Sathisan | Halle |
| Daniel | Katie |
| Qingling | Florian |
| Thaddeus | Matt |

**10:30 am**: [VSMs](VSMs.ipynb)

**12:30 pm**: Break time!

**2:00 pm**: Investigation Presentation: Sathisan Vannadil on Monte Carlo Simulation

**1:45 pm**: Work
* [Project 4: Fletcher](/projects/04-fletcher)

**6:00 pm:** We're not done with NLP, but you have plenty for your projects :smile:

#### More Resources
##### TFIDF and Naive Bayes Classification
* [tf-idf on Wikipedia](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)
* [tf-idf tutorial with textblob](http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)
* [Stanford slides on text classification with naive Bayes](https://web.stanford.edu/class/cs124/lec/naivebayes.pdf)
* [Naive Bayes on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)
* [Naive Bayes Spam Filtering on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)

Empirically, naive Bayes works really well on text classification. One example is spam filtering. Two classes (spam/not spam). A bag of words model (treating each word as an independent feature), using tf-idf values as weights for the features in `MultinomialNB` works wonders.

However, naive Bayes is not necessarily the ultimate text classifier. It works reasonably well if you don't have ginormous amounts of data. However, if you have enough data, generally successful classifiers like SVMs can surpass it (but they may take longer to train). So don't be shy in trying other classifiers.

##### word2vec
* [Deep Learning, NLP, and Representations](http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/)
