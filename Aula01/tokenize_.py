from base_nltk import *


sentencas = sent_tokenize(texto, language="portuguese")
words = word_tokenize(texto, language="portuguese")

if __name__ == "__main__":

    print("------------------------------------")
    print("Sentenças Tokenize")
    print(sentencas)
    print(type(sentencas))
    print(len(sentencas))

    print("------------------------------------")
    print("Words Tokenize")
    print(words)
    print(type(words))
    print(len(words))
