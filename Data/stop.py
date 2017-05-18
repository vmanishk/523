from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import json
import re

fin = open('/Users/Brothaman/Home/SBU CS/523/CP/BTM-master/sample-data/doc_info.txt', 'r')
all_lines = fin.readlines()

fbad = open('/Users/Brothaman/Home/SBU CS/523/CP/BTM-master/sample-data/badwords.txt', 'r')
bad_lines = fbad.readlines()

stops = set(stopwords.words("english"))
stops.add("im")

for bad in bad_lines:
  bad = bad.strip().lower()
  stops.add(bad)

lmtzr = WordNetLemmatizer()
count = 0

def filter_text(text):
    filtered_text = ""
    words = text.split(" ")
    new_words = []
    global count
    for i in range(0,len(words)):
        words[i] = words[i].strip().lower()
        try:
          words[i] = lmtzr.lemmatize(words[i])
        except UnicodeDecodeError:
          count+=1
          #print count
          pass
      
        if words[i].startswith('http') or words[i].startswith('@') or words[i] in stops:
            pass
        else:
            new_words.append(words[i])

    try:
      text = " ".join(new_words)
    except UnicodeDecodeError:
      count+=1
      #print count
      pass
    
    #keep only informative characters
    filtered_text = re.sub('[^a-z|A-Z|\s]', '', text);
    filtered_text = filtered_text.strip()
    return filtered_text

f = open('/Users/Brothaman/Home/SBU CS/523/CP/BTM-master/sample-data/doc_opioid_proc.txt', 'w')

for line in all_lines:
    f.write(filter_text(line)+'\n')

print len(all_lines)

f.close()