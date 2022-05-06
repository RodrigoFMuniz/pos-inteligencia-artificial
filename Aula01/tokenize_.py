import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('tagsets')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

texto = "Nós somos feitos de poeiras de estrelas. Nós somos uma maneira de os cosmos se auto conhecer. A imaginação nos leva a mundos que sequer existiram, mas sem ela não vamos a lugar algum. Maneiro são as maneiras de maneirismos, imagine se assim não fossem"


print("------------------------------------")
print("Sentenças Tokenize")

sentencas = sent_tokenize(texto, language="portuguese")

print(sentencas)
print(type(sentencas))
print(len(sentencas))

print("------------------------------------")
print("Words Tokenize")

words = word_tokenize(texto, language="portuguese")

print(words)
print(type(words))
print(len(words))
