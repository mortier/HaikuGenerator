from pattern.web import *

import re
#re.findall("a",full_text)
#re.findall("a+",full_text)
#matches = re.findall("\w+","hello test hi HEYO")
#re.findall("[a-zA-Z'_0-9]+","hello test hi...'1-")
#all_words = re.findall("[\w'\-]+",full_text)

f = open("Websters.txt","r")
full_text = f.read()
start_of_dict = full_text.index("Produced by Graham Lawrence")
end_of_dict = full_text.index("End of Project Gutenberg's Webster's")
full_text = full_text[start_of_dict + len("Produced by Graham Lawrence"):end_of_dict]

# PICKLE MY DICT!
import pickle

word_to_syllables = {}

all_words = re.findall("[\w'\-\*\"\']+",full_text[:10000])
for i in all_words:
    if i.isupper():
        word_to_syllables[i] = all_words[all_words.index(i)+1]

pickle.dump(word_to_syllables,open("save.p","wb"))
word_to_syllables = pickle.load(open("save.p","rb"))