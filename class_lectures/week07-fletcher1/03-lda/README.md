### Plan for Tuesday, May 30

#### Overview

Today we'll give you one last taste of topic modeling that you might be able to try on your projects, with Latent Dirichlet Allocation (LDA).  The full math to get to the LDA solution uses some deep stuff that I wouldn't expect you to be able to solve, but at its core it's just Bayesian inference so don't stress.  Ultimately, it's just one more technique to reduce from the original document-term space to a latent topic space (in fact LDA explicitly constructs the idea of a topic as humans might think of them).

#### Schedule

**9:15 am**: :penguin: :trophy:

**9:30 am**: [Pair Problem](pair.md).

| Student 1 | Student 2 |
|---|---|
| Orlando | Andrew |
| Guo | Emily |
| Previous Group | Kailin |
| Walter | Paul |
| Sonal | Halle |
| Kenny | Katie |
| Alexander | Florian |
| Doug | Matt |
| Toni | Thaddeus |
| Timan | Qingling |
| Sathisan | Daniel |

**10:30 am**: [Topic Modeling](Topic_Modeling.pdf)

**11:15 am**: [LDA a la gensim](LDA.ipynb)

**11:45 am**: Quiz Review

**12:30 pm**: Eating time

**2:00 pm**: Investigation Presentation: Matt Murray on Newcastle Brown Ale

**2:15 pm**: Let's Project!

### Further Resources

 * Christine Doig's [Introduction to Topic Modeling in Python](http://chdoig.github.io/pygotham-topic-modeling/) from PyGotham 2015
 * [Topic Models (Wikipedia)](http://en.wikipedia.org/wiki/Topic_model): This also has links to other main topic modeling algorithms:
     * Explicit semantic analysis (Using documents of another corpus as topics)
     * Latent semantic analysis  (PCA with Multinomial distribution, predecessor of LDA)
     * Latent Dirichlet allocation (LDA, the most popular one, what we went over today)
     * Hierarchical Dirichlet process (Hierarchical LDA)
     * Non-negative matrix factorization (A linear algebra based method)
 * [How does LDA work?](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/): This is a pretty good explanation, I really recommend reading it.
 * [LDA Math](http://obphio.us/pdfs/lda_tutorial.pdf)
 * [Introduction to Probabilistic Topic Models](https://www.cs.princeton.edu/~blei/papers/Blei2011.pdf) from LDA originator David Blei
 * [gensim tutorial for working with corpora](http://radimrehurek.com/gensim/tut1.html)
 * [gensim tutorial for tfidf and topic modeling](http://radimrehurek.com/gensim/tut2.html)
 * [gensim LDAModel](http://radimrehurek.com/gensim/models/ldamodel.html)
 * Brandon Rose has a nice [notebook](http://brandonrose.org/clustering) demonstrating a whole process including using Gensim.
 * There's another Python package called [lda](https://pypi.python.org/pypi/lda).
 * [LDAvis: A method for visualizing and interpreting topics](http://nlp.stanford.edu/events/illvi2014/papers/sievert-illvi2014.pdf), a paper about the corresponding tool, which now has a Python version
