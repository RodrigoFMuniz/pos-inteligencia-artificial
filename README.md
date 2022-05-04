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
