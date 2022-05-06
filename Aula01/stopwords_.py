import nltk
from nltk.corpus import stopwords
from tokenize_ import words

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('tagsets')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

texto = "Nós somos feitos de poeiras de estrelas. Nós somos uma maneira de os cosmos se auto conhecer. A imaginação nos leva a mundos que sequer existiram, mas sem ela não vamos a lugar algum. Maneiro são as maneiras de maneirismos, imagine se assim não fossem"

print("------------------------------------")
print("Stopwords")

stops = stopwords.words("portuguese")
print(len(stops))
# print(stops)

words_wo_stopwords = [w for w in words if w not in stops]

print(words_wo_stopwords)
