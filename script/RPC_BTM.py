import Constants
import math
import subprocess
import timeit
import numpy as np
import matplotlib.pyplot as plt

SUBSET_COUNT = 5
START_K = 5
END_K = 31
INCREMENT_K = 5

def convertWordIds(wordIds):
    dictionary = dict()
    for id in wordIds:
        if id not in dictionary:
            dictionary[id] = 1
        else:
            dictionary[id] = dictionary[id] + 1
    return list(dictionary.keys()), list(dictionary.values())

def getNParray(li):
    arr = list()
    for each in li:
        dists = each.split()
        subArr = [float(every) for every in dists]
        arr.append(subArr)
    return np.array(arr)



def modifyShellScript(topic_cnt, filename):
    with open(filename) as sh_file:
        lines = sh_file.readlines()

    for line_num in range(len(lines)):
        line = lines[line_num]
        if "# number of topics" in line:
            replace_str = "K=" + str(topic_cnt) + "   # number of topics" + "\n"
            lines[line_num] = replace_str
    sh_file.close()
    sh_file = open(filename, 'w')
    for line in lines:
        print(line, file=sh_file, end='')
    sh_file.close()

def calculatePerplexity(testData, topic_cnt):
    totalWordCount = 0
    file = open(Constants.TEST_DATA_FOLDER_PATH + "dataset.txt", 'w')
    for line in testData:
        words = line.split()
        totalWordCount = totalWordCount + len(words)
        print(line, file=file, end='')
    file.close()
    modifyShellScript(topic_cnt, "InferFromModel.sh")

    print("--------------------   Calculating Perplexity for Test Data  ----------------------")
    subprocess.run(['./InferFromModel.sh'])
    topicDistributionFilename = Constants.MODEL_FOLDER_PATH + "k" + str(topic_cnt) + ".pz_d"
    with open(topicDistributionFilename) as topicDistFile:
        topicDistLines = topicDistFile.readlines()
    topicDistFile.close()

    wordDistributionFilename = Constants.MODEL_FOLDER_PATH + "k" + str(topic_cnt) + ".pw_z"
    with open(wordDistributionFilename) as wordDistFile:
        wordDistLines = wordDistFile.readlines()
    wordDistFile.close()

    # total_pp = 0
    # for line in topicDistLines:
    #     totalLogValue = 0
    #     distValues = line.split()
    #     for value in distValues:
    #         totalLogValue = totalLogValue + math.log10(float(value))
    #         total_pp = total_pp + math.fabs(totalLogValue)/topic_cnt
    #
    # pp = total_pp/len(testData)
    # print("PP=", pp)
    # return pp

    word_id_file = open(Constants.OUTPUT_FOLDER_PATH + "test/doc_wids.txt", "r")
    wordsIds = word_id_file.readlines()
    topic_dist = getNParray(topicDistLines)
    word_dist = getNParray(wordDistLines)
    numerator = 0
    denominator = 0
    for i in range(len(wordsIds)): #for every sentence in test data
        wid = list()
        for eachwid in wordsIds[i].split():
            wid.append(int(eachwid))
        doc_idx, doc_cts = convertWordIds(wid)
        dot_prod = np.dot(topic_dist[i, :], word_dist[:, doc_idx])
        numerator += np.sum(np.log(dot_prod) * doc_cts)
        denominator += np.sum(doc_cts)

    pp = numerator/denominator
    print("PP=", pp)
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
    rpc = list()
    k = START_K

    log_file = open(Constants.FULL_DATA_FOLDER_PATH + "log.txt", 'w')

    for topic_cnt in range(START_K, END_K, INCREMENT_K):
        print("--------------------   TRAINING MODEL  --------------------")
        print("Topic count=", topic_cnt)
        testSet = SUBSET_COUNT - 1
        train_data = list()
        modifyShellScript(topic_cnt, "buildModel.sh")
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
            subprocess.run(['./buildModel.sh'])
            p = calculatePerplexity(subsets[testSet], topic_cnt)
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
            rpc.append((topic_cnt, (pp2 - pp1)/INCREMENT_K))
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
    plt.ylabel('Perplexity')
    plt.xlabel('Topic Count')
    plt.show()

