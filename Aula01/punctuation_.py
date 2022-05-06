import nltk
from stopwords_ import words_wo_stopwords
import string
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('tagsets')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

texto = "Nós somos feitos de poeiras de estrelas. Nós somos uma maneira de os cosmos se auto conhecer. A imaginação nos leva a mundos que sequer existiram, mas sem ela não vamos a lugar algum. Maneiro são as maneiras de maneirismos, imagine se assim não fossem"

print(string.punctuation)

print('---------------------------------')
print('Sem pontuação e sem stopwords')

texto_wo_stopwords_and_punctuation = [
    w for w in words_wo_stopwords if w not in string.punctuation]

print(texto_wo_stopwords_and_punctuation)
