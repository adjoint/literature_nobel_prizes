import re
from collections import Counter

with open('lyrics.txt') as f: #with open('book.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)

print word_counts.most_common(100)