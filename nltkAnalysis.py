import nltk
import re
def getWords(text):
    return re.compile('\w+').findall(text)

filename = "lyrics" #"book"
with open(filename +'.txt') as f:
    passage = f.read()

tokens = getWords(passage)
text = nltk.Text(tokens)

print filename
print "unique words: " + str(len(set(text)))
print "total words: " + str(len(text))
print "ratio: " + str(float(len(set(text)))/len(text))