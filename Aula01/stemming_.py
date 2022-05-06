from base_nltk import *
from punctuation_ import texto_wo_stopwords_and_punctuation


if __name__ == "__main__":
    print('---------------------------------')
    print(texto)

    print('---------------------------------')
    print('Stem PorterSteamer')
    steamer = PorterStemmer()
    stem1 = [steamer.stem(words)
             for words in texto_wo_stopwords_and_punctuation]
    print(stem1)

    print('---------------------------------')
    print('Stem SnowballSteamer')
    steamer2 = SnowballStemmer('portuguese')
    stem2 = [steamer2.stem(words)
             for words in texto_wo_stopwords_and_punctuation]
    print(stem2)

    print('---------------------------------')
    print('Stem LancasterSteamer')
    steamer3 = LancasterStemmer()
    stem3 = [steamer3.stem(words)
             for words in texto_wo_stopwords_and_punctuation]
    print(stem3)
