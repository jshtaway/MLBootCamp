### MongoDB Challenges

##### Setup

Make sure that mongodb is setup and the database server (`mongod`) is running.

We are going to work with reviews of Heavy Metal movies. Hellz Yeah.
Unzip and unpickle the following file:

[heavy_metal_parsed.pkl.zip](heavy_metal_parsed.pkl.zip)

```
import pickle
with open("heavy_metal_parsed.pkl", 'r') as datafile:
    heavy_metal_reviews = pickle.load(datafile)
```

It's a list of dictionaries. One dictionary per review: perfect for a mongo document.
The key `raw` has the full text as a list of lines. For example, to see the first review, you can do:
```
first_review = heavy_metal_reviews[0]
for line in first_review['raw']:
    print line
```
which will give you:

    200 MOTELS (1971)
    DIRECTORS: Tony Palmer, Frank Zappa
    CAST: Frank Zappa, Ringo Starr, Mark Volman, Howard Kaylan, Keith Moon
    METAL CRED
    Frank Zappa
    Nun Desecration
    THE MEAT
    Beyond his metal sainthood for battling the censor-witches of the PMRC and getting named checked by Deep Purple in “Smoke on the Water”, musical visionary Frank Zappa led many rock fans to heavy metal.
    And, from there, he led many metal fans to the outer expanses of rock’s possibilities.
    Zappa also opened countless banging heads to the far reaches of jazz, classical, doo-wop, and any other art form that could involve (brilliant) noise and (brilliantly dumb) dirty jokes.
    200 Motels is Zappa’s first crack at major motion picture madness, and it
    embodies the much forgotten cultural moment when acid rock tumbled forever into the black pits of rising heavy metal.
    Surrealistic sketches and psychedelic set pieces about the insanity of a being on tour are interspersed among performances in which the Mothers jam with London Philharmonic.
    Ringo Starr plays Zappa during the talking parts. Zappa himself, plays guitar throughout, demonstrating how very much of a six-string maestro he was, every lick on par with his future collaborators Steve Vail and Yngwie Malmsteen.
    SOLID METAL NUGGETS
    - A psychedelic cartoon interlude admiringly tweaks Black Sabbath and Grand Funk Railroad.
    - Keith Moon, madman drummer of the Who, pops up—and off—as “The Hot Nun.”

Let's see what other fields each document has:
```
print first_review.keys()
```
shows
```
['raw',
 'head',
 'metal_cred',
 'title',
 'direct',
 'solid_metal_nuggets',
 'cast',
 'the_meat',
 'year',
 'sections']
```
Basically, each section in the review is parsed into it's own key.

Ok, put these documents into a mongodb collection. For these challenges, do not use the `heavy_metal_reviews` list directly. Use mongo queries (you can use the mongo client directly or use pymongo from within python).


#####Challenge 1
Make a histogram of the years in the data. How many metal movies came
out over the years?

##### Challenge 2
Find the cast member that appeared in most Heavy Metal movies. Is
there one that is shared by more than one of these movies? Or are they
all completely different actors for every movie?

##### Challenge 3
Find the most used words in Heavy Metal film titles. Is there a word
that appears in a lot of them? Is it "The"? If it is something like
"the", How can you get around that? Find one "meaningful" word that
appears the most (this means non-structural word, unlike "the" or "a"
or "in")

##### Challenge 4
METAL CRED section lists themes included in these movies that makes
them more metal.
What were the top 5 metal cred keywords in the 70s? In 80s? In 90s, In
2000s?

##### Challenge 5
Let's use the length of the METAL CRED section as a proxy score for
how metal a movie is. Let's call this the METAL SCORE. To each mongo
document, add the metal_score as a new field.

##### Challenge 6
Find the director that is MOST METAL per movie (director with the
highest average metal score).
Remember that some movies have multiple directors.

##### Challenge 7
The majority of directors and actors will have worked on a single
movie. See if there are any directors that worked with an actor more
than once. If so, find the director-actor duo that have worked
together the most times.

##### Challenge 8
Create an index on the 'director' field to make the queries involving
it faster.
[What is an index?](http://en.wikipedia.org/wiki/Database_index)

[Creating an index in mongo](http://docs.mongodb.org/manual/tutorial/create-an-index/)
[Creating an index in pymongo](http://api.mongodb.org/python/current/api/pymongo/collection.html?highlight=create_index#pymongo.collection.Collection.create_index)
[Single field index on mongo](http://docs.mongodb.org/manual/core/index-single/)
[Mongo documentation on indexes](http://docs.mongodb.org/manual/core/indexes/)

##### Challenge 9 (Optional challenge for early finishers)
For each decade, make a histogram of metal scores.
Also, calculate the average metal score for each decade. Which decade
was the most pure metal decade?

##### Note (rather than a challenge)
In the latest version of mongo, you can do a text query.
To do this, you need to create one (only one) text-based index.
Let's index the_meat field so we can make text search queries on it
(in pymongo):

db.reviews.create_index([("the_meat", pymongo.TEXT,)])

Now you can do text search. For example, let's search for the phrase
"hitting power chords" within "the_meat" fields of all our documents.

    db.reviews.find({"$text": {"$search": "hitting power
    chords"}}).count()

    206

It has found 206 reviews. I can print the titles of the first 10
reviews that were returned in this text search:

    ten_matches = r.find({"$text": {"$search": "hitting power chords"}}).limit(10)
    for match in ten_matches:
        print match["title"]


    DOMINATOR
    REPO: THE GENETIC OPERA
    GREMLINS 2: THE NEW BATCH
    VICE SQUAD
    THE JERKY BOYS: THE MOVIE
    THE SONG REMAINS THE SAME
    THE EXORCIST
    THE CROW
    CANNIBAL HOLOCAUST
    HOSTEL

Enjoy your text searches : ) These can be very useful in some apps.


### Twitter API Extension

Create a mongo collection of tweets about something (anything you
choose).

Each mongo document should contain the text, username, favorite count
and retweet count of the tweet.
