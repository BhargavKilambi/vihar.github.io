from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ['50 million developers come,\n', 'make scraping data tricky,\n', 'third link displays city,\n', 'selenium webdriver helped,\n', 'parse versions intended,\n', 'largest developer community,\n', 'following three links,\n', 'easily grab data,\n', 'testing facebook accounts,\n', 'small facebook app,\n',
             '500 facebook urls,\n', 'uses beautiful soup,\n', 'think scraping data,\n', 'cannot get city,\n', 'try using selenium,\n', 'first using mechanize,\n', 'third type,\n', 'beautiful soup,\n', 'first link,\n', 'facebook displays,\n', 'using facebook,\n', 'try opening,\n', 'similar data,\n', 'required data,\n', 'gets data']


vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)


true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :10]:
        print ' %s' % terms[ind],
    print
