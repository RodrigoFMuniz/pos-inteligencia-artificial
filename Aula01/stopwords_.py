from base_nltk import *
from tokenize_ import words

print("------------------------------------")
print("Stopwords")

stops = stopwords.words("portuguese")
print(len(stops))
# print(stops)

words_wo_stopwords = [w for w in words if w not in stops]

print(words_wo_stopwords)
