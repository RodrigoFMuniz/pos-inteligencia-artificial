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
