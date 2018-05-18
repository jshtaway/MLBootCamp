### Plan for Friday, October 27

#### Overview  

Today we'll start **NLP**! :smile:

In the morning I'll talk about some basic concepts of text analysis, which we'll build on next week (but these should get your brain churning on Fletcher ideas over the weekend).  If Lord Savage doesn't wear you out in the afternoon, hopefully we can take some time to talk about **NoSQL Databases** and one of them in particular, **MongoDB**.

#### Schedule

**9:15 am**: Guten Morgen

**9:30 am**: [Pair programming](digits_clustering.ipynb).

| Student 1 | Student 2 |
|---|---|
| Rebekah | Kalgi |
| Pradnya | Trent |
| Chuoran | Jeff |
| Mike | Laura |
| Michael | Kenny |
| Carl | Yanxi |
| Andre | Sufyan |

**10:15 am**: Intro to NLP  
* [NLP Intro](NLP.ipynb)
* [NLP with Python](NLP_nltk.ipynb)

**12:15 pm**: Lunch

**1:45 pm**: Investigation Presentation: Andre Johnson on Python for Finance

**2:00 pm**: More of Lord Savage!

**3:00 pm**: **NoSQL** and **MongoDB**  
- [Slides](NoSQL_and_MongoDB.pdf)
- [Hands-on/Setup](mongodb_ubuntu.md)

### More Resources on MongoDB

 * [Intro to Mongo](https://docs.mongodb.com/getting-started/shell/introduction/)
 * [Mongo query documentation](http://docs.mongodb.org/manual/tutorial/query-documents/)
 * [MongoDB Aggregation Framework Basics Explained](http://www.redotheweb.com/2012/10/12/mongodb-new-aggregation-framework-and-sql-side-by-side.html)
 * [Pymongo tutorial](http://api.mongodb.org/python/current/tutorial.html)


### More Resources

 * [Overencompassing yet still short nltk tutorial](http://www.nltk.org/book/) The official book of the nltk
 * [TextBlob tutorial](http://textblob.readthedocs.org/en/latest/quickstart.html): Awesome, easy to read, very short but to the point. Check this out.
 * [TextBlob full documentation](http://textblob.readthedocs.org/en/dev/): Great documentation
 * [TextBlob Sentiment: Calculating Polarity and Subjectivity](http://planspace.org/20150607-textblob_sentiment/)
 * [List of part-of-speech tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html): What does VBZ mean? etc.
 * [Chunking tutorial](http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf)
 * [MIT slides on chunking](http://web.media.mit.edu/~havasi/MAS.S60/PNLP7.pdf): If you want to learn more on chunking and prepare your own chunking classifiers, these will help.
 * [Demo for different tokenizers](http://text-processing.com/demo/tokenize/) / [Demo for different stemmers](http://text-processing.com/demo/stem/): These let you get a feel for what different classes do.
 * [tf-idf on Wikipedia](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)
 * [tf-idf tutorial with textblob](http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/)
 * [Stanford slides on text classification with naive Bayes](https://web.stanford.edu/class/cs124/lec/naivebayes.pdf)
 * [Naive Bayes on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)
 * [Naive Bayes Spam Filtering on Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)

Empirically, naive Bayes works really well on text classification. One example is spam filtering. Two classes (spam/not spam). A bag of words model (treating each word as an independent feature), using tf-idf values as weights for the features in `MultinomialNB` works wonders.

However, naive Bayes is not necessarily the ultimate text classifier. It works reasonably well if you don't have ginormous amounts of data. However, if you have enough data, generally successful classifiers like SVMs can surpass it (but they may take longer to train). So don't be shy in trying other classifiers.
