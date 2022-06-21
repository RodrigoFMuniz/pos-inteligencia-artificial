# Pós em inteligência artificial, machine learning e deep learning

## Aula 01

### NLTK.PY

#### importando NLTK

    import nltk
    from nltk.corpus import stopwords, treebank
    from nltk.stem import PorterStemmer, WordNetLemmatizer, SnowballStemmer, LancasterStemmer
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.tag import pos_tag, pos_tag_sents

#### Trabalhando com donwload

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('tagsets')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    nltk.download()

#### Criando um texto base

    texto = "Nós somos feitos de poeiras de estrelas. Nós somos uma maneira de os cosmos se auto conhecer. A imaginação nos leva a mundos que sequer existiram, mas sem ela não vamos a lugar algum."

#### sent_tokenize

    sentencas = sent_tokenize(texto, language="portuguese")

    print(sentencas) # imprime uma lista de frases filtradas do texto
    print(type(sentencas)) # Retorna uma <class list>
    print(len(sentencas))# Retorna o tamanho da lista

#### word_tokenize

    words = word_tokenize(texto,language="portuguese")

    print(words) imprime uma lista de palavras filtradas do texto
    print(type(words)) # Retorna uma <class list>
    print(len(words)) # Retorna o tamanho da lista

#### stopwords

    stops = stopwords.words("portuguese")
    print(len(stops))
    print(stops)

    words_wo_stopwords = [w for w in words if w not in stops]

    print(words_wo_stopwords)

#### string

    print(string.punctuation)

    texto_wo_stopwords_and_punctuation = [w for w in words_wo_stopwords if w not in string.punctuation]

    print (texto_wo_stopwords_and_punctuation)

#### Statistics

    freq = nltk.FreqDist(texto_wo_stopwords_and_punctuation)
    freq_words = freq.pformat

    if __name__ == "__main__":
        print(freq.most_common(5))
        print(freq.most_common(35))
        print(freq_words)

#### Stemming

    from punctuation_ import texto_wo_stopwords_and_punctuation

#### - Texto base

    if __name__ == "__main__":
        print('---------------------------------')
        print(texto)

#### - Porter

        print('---------------------------------')
        print('Stem PorterSteamer')
        steamer = PorterStemmer()
        stem1 = [steamer.stem(words)
                for words in texto_wo_stopwords_and_punctuation]
        print(stem1)

#### - Snowball

        print('---------------------------------')
        print('Stem SnowballSteamer')
        steamer2 = SnowballStemmer('portuguese')
        stem2 = [steamer2.stem(words)
                for words in texto_wo_stopwords_and_punctuation]
        print(stem2)

#### - Lancaster

        print('---------------------------------')
        print('Stem LancasterSteamer')
        steamer3 = LancasterStemmer()
        stem3 = [steamer3.stem(words)
                for words in texto_wo_stopwords_and_punctuation]
        print(stem3)
### Spacy
