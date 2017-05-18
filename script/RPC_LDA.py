## Finding K based on RPC. implemented  by Gaurav Gopalkrishna.
import Constants
import math
from gensim import corpora, models
import timeit
import numpy as np
import matplotlib.pyplot as plt

SUBSET_COUNT = 5
START_K = 2
END_K = 25
INCREMENT_K = 1

def buildModel(topic_cnt):
    tweets = []
    file = open(Constants.TRAIN_DATA_FOLDER_PATH + "dataset.txt", 'r')
    lines = file.readlines()
    for line in lines:
        words = line.split(" ")
        tweets.append(words)
    file.close()

    # create dictionary (index of each element)
    dictionary = corpora.Dictionary(tweets)
    corpus = [dictionary.doc2bow(t) for t in tweets]

    model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, alpha = 0.01,eta = 0.2,num_topics=topic_cnt, update_every=1, chunksize=30000,
                                   passes=1)
    return model, dictionary

def calculatePerplexity(topic_cnt, testData, model, dictionary):
    totalWordCount = 0
    file = open(Constants.TEST_DATA_FOLDER_PATH + "dataset.txt", 'w')
    for line in testData:
        words = line.split()
        totalWordCount = totalWordCount + len(words)
        print(line, file=file, end='')
    file.close()

    test_tweets = []
    file = open(Constants.TEST_DATA_FOLDER_PATH + "dataset.txt", 'r')
    lines = file.readlines()
    for line in lines:
        words = line.split(" ")
        test_tweets.append(words)

    test_corpus = [dictionary.doc2bow(t) for t in test_tweets]
    pp = model.bound(test_corpus)
    #pp = model.log_perplexity(test_corpus)
    print("PP:", pp)
    return pp


if __name__ == '__main__':

    start_time = timeit.default_timer()
    data_file = open(Constants.FULL_DATA_FOLDER_PATH + "dataset.txt", encoding="utf8")
    all_lines = [l for l in data_file]
    print("SUBSET_COUNT =", SUBSET_COUNT)
    print("SUBSET size = ", len(all_lines) / SUBSET_COUNT)
    increment = math.floor(len(all_lines) / SUBSET_COUNT)

    subsets = list()
    counter = 0

    for i in range(SUBSET_COUNT):
        subset = list()
        for j in range(counter, counter + increment):
            subset.append(all_lines[j])
        subsets.append(subset)
        counter = counter + increment

    perplexity = list()
    rpc = list()
    k = START_K

    log_file = open(Constants.FULL_DATA_FOLDER_PATH + "log.txt", 'w')

    for topic_cnt in range(START_K, END_K, INCREMENT_K):
        print("--------------------   TRAINING MODEL  --------------------")
        print("Topic count=", topic_cnt)
        testSet = SUBSET_COUNT - 1
        train_data = list()
        pp = list()
        for j in range(SUBSET_COUNT):
            for k in range(SUBSET_COUNT):
                if k != testSet:
                    train_data.extend(subsets[k])
            print("testSet=", testSet)
            print("train_data size=", len(train_data))
            file = open(Constants.TRAIN_DATA_FOLDER_PATH + "dataset.txt", 'w')
            for line in train_data:
                print(line, file=file, end='')
            lda_model, dictionary = buildModel(topic_cnt)
            p = calculatePerplexity(topic_cnt, subsets[testSet], lda_model, dictionary)
            print(topic_cnt, ":adding p:", p, file=log_file)
            if not math.isnan(p):
                pp.append(p)

            testSet = testSet - 1
            del train_data[:]

        print(topic_cnt, ":avg p:", str(sum(pp) / float(len(pp))), file=log_file)
        perplexity.append((topic_cnt, sum(pp) / float(len(pp))))
        if len(perplexity) > 1:
            tc, pp2 = perplexity[len(perplexity) - 1]
            tc, pp1 = perplexity[len(perplexity) - 2]
            print(topic_cnt, ":rpc:", str((pp2 - pp1)/INCREMENT_K), file=log_file)
            temp = (pp2 - pp1)/INCREMENT_K
            temp = abs(temp)   #changes made to take the absolute value
            rpc.append((topic_cnt, temp))
        del pp[:]

    print(rpc)
    end_time = timeit.default_timer()
    total_time = (end_time-start_time)/60
    print("Total program running time:", total_time, "minutes")
    print("Total program running time:", total_time, "minutes" , file=log_file)
    print("RPC's: ", rpc, file=log_file)
    log_file.close()

    tpcs = list()
    pps = list()
    for each in rpc:
        tpcs.append(each[0])
        pps.append(each[1] * 10000)

    plt.plot(tpcs, pps)
    plt.ylabel('RPC')
    plt.xlabel('Topic Count')
    plt.show()

