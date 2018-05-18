### NLP / Clustering Challenges


##### Challenge 1

Cluster sentences with K-means. If you have your own Fletcher text data, get sentences out and cluster them. If not, cluster the tweets you gathered during the last challenge set. For each cluster, print out the sentences, try to see how close the sentences are. Try different K values and try to find a K value that makes the most sense (the sentences look like they do form a meaningful cluster).

How do you deal with retweets (if you're clustering tweets)?


##### Challenge 2

Draw the inertia curve over different k values. (The sklearn KMeans class has an inertia_ attribute.)


##### Challenge 3

__Let's name the clusters 1__

For each cluster, find the sentence closest to the centroid of the cluster.

(You can use [sklearn.metrics.pairwise_distances](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances) or [scipy.spatial.distance](http://docs.scipy.org/doc/scipy/reference/spatial.distance.html) [check `pdist`, `cdist`, and `euclidean distance`] to find distances to the centroid). KMeans has a `cluster_centers_` attribute.

This sentence (closest to centroid) is now the name of the cluster. For each cluster, print the representative sentence, and print 'N people expressed a similar statement', or something like that relevant to your dataset. (This is very close to what amazon used to do in the reviews section.)

Find the biggest 3 clusters, and print their representative sentences. (This is close to what amazon is doing now in the reviews section, except they choose the sentence from the most helpful review instead of closest to center.)


##### Challenge 4

__Let's name the clusters 2__

Calculate the tf-idf of each word in each cluster (think of all sentences of a cluster together as a document). Represent each cluster with the top 1, or top 2 or... to 5 tf-idf words. For each cluster, print the name (keywords) of the cluster, and "N statements" in the cluster (N is the size of the cluster)


##### Challenge 5

__Let's name the clusters 3__

Same as the previous challenge, but this time, calculate tf-idf only for nouns (NN tag) and build keyword(s) with nouns. (This is close to what amazon switched to last year, before settling into the current design). (They would show five nouns, you would click on one and it would show sentences - linked to the reviews- that were related to that noun.)


##### Challenge 6

Cluster the same data with [MiniBatchKMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html). MiniBatchKMeans is a fast way to apply K-means to large data without much loss -- The results are very similar. Instead of using EVERY single point to find the new place of the centroid, MiniBatch just randomly samples a small number (like 100) in the cluster to calculate the new center. Since this is usually very close to the actual center, the algorithm gets there much faster. Try it and compare the results. ([Example on two-feature data](http://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html))


##### Challenge 7

Switch the __init__ parameter to "random" (instead of the default kmeans++) and plot the inertia curve for each of the __n_init__ values for K-Means: 1, 2, 3, 10 (n_init is the number of different runs to try with different random initializations).


##### Challenge 8

Download [this dataset on the purchase stats from clients of a wholesale distributor](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers). Cluster the clients based on their annual spending features (fresh, milk, grocery, frozen, detergents_paper, delicatessen). Remember to scale the features before clustering. After finding a reasonable amount of clusters, for EACH cluster, plot the histogram for every single feature: FRESH, MILK, GROCERY, FROZEN, DETERGENTS_PAPER, DELICATESSEN, CHANNEL, REGION. Is there a natural way to characterize each cluster? How would you describe each cluster to the wholesale distributor if you were working for them?


#### Clustering Extensions (Optional)

Use the same code for your previous clustering challenges.

Repeat each challenge (except the inertia curves, since only the KMeans implementation gives a quick way of calculating that.) However, this time, try (both) Agglomerative Clustering and DBSCAN instead of KMeans.

For text clustering, use cosine distance.
