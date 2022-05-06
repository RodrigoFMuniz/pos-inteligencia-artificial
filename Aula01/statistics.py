from base_nltk import *
from punctuation_ import texto_wo_stopwords_and_punctuation

freq = nltk.FreqDist(texto_wo_stopwords_and_punctuation)
freq_words = freq.pformat

if __name__ == "__main__":
    print(freq.most_common(5))
    print(freq.most_common(35))
    print(freq_words)
