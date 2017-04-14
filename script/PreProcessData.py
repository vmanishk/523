from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import csv
import re

lemmatizer = WordNetLemmatizer()
fin = csv.reader(open('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/sample-data/merged_marijuana_1_13.csv', encoding="utf8"))
all_lines = [l for l in fin]

stops = set(stopwords.words("english"))
stops.add("im")

def filter_text(text):
    filtered_text = ""
    words = text.split(" ")
    new_words = []
    for i in range(0,len(words)):
        words[i] = words[i].strip().lower()
        lemmatized_word = lemmatizer.lemmatize(words[i])
        words[i] = lemmatized_word
        if words[i].startswith('http') or words[i].startswith('@') or words[i] in stops:
            pass
        else:
            new_words.append(words[i])

    text = " ".join(new_words)
    #keep only informative characters
    filtered_text = re.sub('[^a-z|A-Z|\s]', '', text);
    filtered_text = filtered_text.strip()
    return filtered_text


output = []
for line in all_lines:
    # print("Before: ", line[4])
    filtered = filter_text(line[4])
    # print("After: ", filtered)
    output.append(filtered)


file = open('/home/gauravbg/Documents/Advanced Project (CSE-523)/TopicModelling-Twitter-text-master/Data/dataset.txt', 'w')
for line in output:
    print(line, file=file)

file.close()

