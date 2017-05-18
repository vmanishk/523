from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities
import gensim
from itertools import chain

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
##en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
##p_stemmer = PorterStemmer()

fin = open('/Users/Brothaman/Home/SBU CS/523/CP/TopicModelling-ShortText/FULL_DATA/dataset.txt', 'r')
all_lines = fin.readlines()

doc_set = []

for line in all_lines:
  doc_set.append(line)


# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    #stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, alpha = 0.01,eta = 0.2, id2word = dictionary, passes=20,minimum_probability=0)

topics  = ldamodel.print_topics(num_topics=20, num_words=10)

for topic in topics:
    print topic


# Assigns the topics to the documents in corpus
lda_corpus = ldamodel[corpus]

# Find the threshold, let's set the threshold to be 1/#clusters,
# To prove that the threshold is sane, we average the sum of all probabilities:
scores = list(chain(*[[score for topic_id,score in topic] \
                      for topic in [doc for doc in lda_corpus]]))
threshold = sum(scores)/len(scores)
print threshold


list_index = range(1, len(doc_set)+1)

cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
cluster6 = []
cluster7 = []
cluster8 = []
cluster9 = []
cluster10 = []
cluster11 = []
cluster12 = []
cluster13 = []
cluster14 = []
cluster15 = []
cluster16 = []
cluster17 = []
cluster18 = []
cluster19 = []


cluster20 = []



doc_index = 0

for text in texts:
    docu = dictionary.doc2bow(text)
    temp =  ldamodel.get_document_topics(docu)
    max_val, argmaxtopic = 0, -1
    
    for pair in temp:
        if max_val < pair[1]:
            max_val = pair[1]
            argmaxtopic = pair[0] + 1
    
    if(argmaxtopic == 1):
        cluster1.append(list_index[doc_index])
    if(argmaxtopic == 2):
        cluster2.append(list_index[doc_index])
    if(argmaxtopic == 3):
        cluster3.append(list_index[doc_index])
    if(argmaxtopic == 4):
        cluster4.append(list_index[doc_index])
    if(argmaxtopic == 5):
        cluster5.append(list_index[doc_index])
    if(argmaxtopic == 6):
        cluster6.append(list_index[doc_index])
    if(argmaxtopic == 7):
        cluster7.append(list_index[doc_index])
    if(argmaxtopic == 8):
        cluster8.append(list_index[doc_index])
    if(argmaxtopic == 9):
        cluster9.append(list_index[doc_index])
    if(argmaxtopic == 10):
        cluster10.append(list_index[doc_index])
    if(argmaxtopic == 11):
        cluster11.append(list_index[doc_index])
    if(argmaxtopic == 12):
        cluster12.append(list_index[doc_index])
    if(argmaxtopic == 13):
        cluster13.append(list_index[doc_index])
    if(argmaxtopic == 14):
        cluster14.append(list_index[doc_index])
    if(argmaxtopic == 15):
        cluster15.append(list_index[doc_index])
    if(argmaxtopic == 16):
        cluster16.append(list_index[doc_index])
    if(argmaxtopic == 17):
        cluster17.append(list_index[doc_index])
    if(argmaxtopic == 18):
        cluster18.append(list_index[doc_index])
    if(argmaxtopic == 19):
        cluster19.append(list_index[doc_index])
    if(argmaxtopic == 20):
        cluster20.append(list_index[doc_index])
    
    doc_index+=1



# # cluster1 = [j for i,j in zip(lda_corpus,doc_set) if i[0][1] > threshold]
# # #cluster1a = [j for i,j in zip(lda_corpus,list_index) if i[0][1] > threshold]
# # cluster2 = [j for i,j in zip(lda_corpus,list_index) if i[1][1] > threshold]
# # cluster3 = [j for i,j in zip(lda_corpus,list_index) if i[2][1] > threshold]
# # cluster4 = [j for i,j in zip(lda_corpus,list_index) if i[3][1] > threshold]
# # cluster5 = [j for i,j in zip(lda_corpus,list_index) if i[4][1] > threshold]
# # cluster6 = [j for i,j in zip(lda_corpus,list_index) if i[5][1] > threshold]
# # cluster7 = [j for i,j in zip(lda_corpus,list_index) if i[6][1] > threshold]
# # cluster8 = [j for i,j in zip(lda_corpus,list_index) if i[7][1] > threshold]
# # cluster9 = [j for i,j in zip(lda_corpus,list_index) if i[8][1] > threshold]
# # cluster10 = [j for i,j in zip(lda_corpus,list_index) if i[9][1] > threshold]
# # cluster11 = [j for i,j in zip(lda_corpus,list_index) if i[10][1] > threshold]
# # cluster12 = [j for i,j in zip(lda_corpus,list_index) if i[11][1] > threshold]
# # cluster13 = [j for i,j in zip(lda_corpus,list_index) if i[12][1] > threshold]
# # cluster14 = [j for i,j in zip(lda_corpus,list_index) if i[13][1] > threshold]
# # cluster15 = [j for i,j in zip(lda_corpus,list_index) if i[14][1] > threshold]
# # cluster16 = [j for i,j in zip(lda_corpus,list_index) if i[15][1] > threshold]
# # cluster17 = [j for i,j in zip(lda_corpus,list_index) if i[16][1] > threshold]

print "list {} & len {}".format(cluster1[0:15], len(cluster1))
print "list {} & len {}".format(cluster2[0:15], len(cluster2))

print "list {} & len {}".format(cluster3[0:15], len(cluster3))

print "list {} & len {}".format(cluster4[0:15], len(cluster4))

print "list {} & len {}".format(cluster5[0:15], len(cluster5))

print "list {} & len {}".format(cluster6[0:15], len(cluster6))

print "list {} & len {}".format(cluster7[0:15], len(cluster7))

print "list {} & len {}".format(cluster8[0:15], len(cluster8))


print "list {} & len {}".format(cluster9[0:15], len(cluster9))

print "list {} & len {}".format(cluster10[0:15], len(cluster10))

print "list {} & len {}".format(cluster11[0:15], len(cluster11))

print "list {} & len {}".format(cluster12[0:15], len(cluster12))

print "list {} & len {}".format(cluster13[0:15], len(cluster13))


print "list {} & len {}".format(cluster14[0:15], len(cluster14))


print "list {} & len {}".format(cluster15[0:15], len(cluster15))


print "list {} & len {}".format(cluster16[0:15], len(cluster16))


print "list {} & len {}".format(cluster17[0:15], len(cluster17))


print "list {} & len {}".format(cluster18[0:15], len(cluster18))


print "list {} & len {}".format(cluster19[0:15], len(cluster19))


print "list {} & len {}".format(cluster20[0:15], len(cluster20))










