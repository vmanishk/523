from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import json
import csv
import re

fbad = open('/Users/Brothaman/Home/SBU CS/523/CP/BTM-master/sample-data/badwords.txt', 'r')
bad_lines = fbad.readlines()


lmtzr = WordNetLemmatizer()

#all_lines = []
fin = csv.reader(open("full_data.csv", encoding="utf8"))
all_lines = [l for l  in fin]



stops = set(stopwords.words("english"))
stops.add("im")

for bad in bad_lines:
  bad = bad.strip().lower()
  stops.add(bad)


stops.add("fentanyl")
stops.add("opioids")
stops.add("acetaminophen")
stops.add("heroin")
stops.add("hydrocodone")
stops.add("hydros")
stops.add("Ibuprofen")
stops.add("methadone")
stops.add("morphine")
stops.add("narcotic")
stops.add("opiate")
stops.add("opioid")
stops.add("opium")
stops.add("oxycodone")
stops.add("oxycontin")
stops.add("tylenol")
stops.add("vicodin")
stops.add("xanax")
stops.add("lortab")
stops.add("percodan")


def filter_text(text):
    filtered_text = ""
    words = word_tokenize(text)
    # words = text.split(" ")
    new_words = []
    for i in range(0,len(words)):
        words[i] = words[i].strip().lower()
        words[i] = lmtzr.lemmatize(words[i])
        if words[i].startswith('http') or words[i].startswith('@') or words[i] in stops:
            pass
        else:
            new_words.append(words[i])

    text = " ".join(new_words)
    #keep only informative characters
    filtered_text = re.sub('[^a-z|A-Z|\s]', '', text)
    filtered_text = filtered_text.strip()
    return filtered_text


output = []
for line in all_lines:
    # print("Before: ", line[4])
    filtered = filter_text(line[4])
    # print("After: ", filtered)
    output.append(filtered)


file = open("dataset_full.txt", 'w')
for line in output:
    print(line, file=file)

file.close()

