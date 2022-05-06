from base_nltk import *
from tokenize_ import words

stops = stopwords.words("portuguese")
words_wo_stopwords = [w for w in words if w not in stops]

if __name__ == "__main__":
    print("------------------------------------")
    print("Stopwords")

    print(len(stops))
    # print(stops)

    print(words_wo_stopwords)
