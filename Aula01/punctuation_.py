from base_nltk import *
from stopwords_ import words_wo_stopwords


texto_wo_stopwords_and_punctuation = [
    w for w in words_wo_stopwords if w not in string.punctuation]

if __name__ == "__main__":
    print(string.punctuation)

    print('---------------------------------')
    print('Sem pontuação e sem stopwords')

    print(texto_wo_stopwords_and_punctuation)
