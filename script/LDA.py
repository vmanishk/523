from gensim import corpora, models, similarities

# tweets=[['human', 'interface', 'computer'],
#  ['survey', 'user', 'computer', 'system', 'response', 'time'],
#  ['eps', 'user', 'interface', 'system'],
#  ['system', 'human', 'system', 'eps'],
#  ['user', 'response', 'time'],
#  ['trees'],
#  ['graph', 'trees'],
#  ['graph', 'minors', 'trees'],
#  ['graph', 'minors', 'survey']]

tweets = []
file = open('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/dataset.txt', 'r')
lines = file.readlines()
for line in lines:
    words = line.split(" ")
    tweets.append(words)

# create dictionary (index of each element)
dictionary = corpora.Dictionary(tweets)
dictionary.save('/tmp/tweets.dict') # store the dictionary, for future reference

# compile corpus (vectors number of times each elements appears)
raw_corpus = [dictionary.doc2bow(t) for t in tweets]
corpora.MmCorpus.serialize('/tmp/tweets.mm', raw_corpus) # store to disk

# STEP 2 : similarity between corpuses
dictionary = corpora.Dictionary.load('/tmp/tweets.dict')
corpus = corpora.MmCorpus('/tmp/tweets.mm')
print(corpus)
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=8, update_every=1, chunksize=10000, passes=2)
topics = lda.print_topics(8)
for topic in topics:
    print(topic)


# -----------------------------------------------------------------------
# # Transform Text with TF-IDF
# tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
# # corpus tf-idf
# corpus_tfidf = tfidf[corpus]
#
# # STEP 3 : Create similarity matrix of all files
# index = similarities.MatrixSimilarity(tfidf[corpus])
# index.save('/tmp/deerwester.index')
# index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
#
# sims = index[corpus_tfidf]


# ---------------------------------------------------------------
# import gensim
# import os

# file = open('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/dataset.txt', 'r')
# path = '/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/Docs/'
# lines = file.readlines()
# for i in range(len(lines)):
#     line = lines[i]
#     print(os.path.join(path, str(i)))
#     temp_file = open(os.path.join(path, str(i)), 'w')
#     print(line, file=temp_file)
#     temp_file.close()

# tfidf = gensim.models.tfidfmodel.TfidfModel('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/Docs')
# print(tfidf)
# tfidf.save('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/tfidf_model')

# id2word = gensim.corpora.Dictionary.load_from_text('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/dataset.txt')
# mm = gensim.corpora.MmCorpus()
