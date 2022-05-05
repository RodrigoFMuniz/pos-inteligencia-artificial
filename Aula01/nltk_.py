import nltk
from nltk.corpus import stopwords, treebank
from nltk.stem import PorterStemmer, WordNetLemmatizer, SnowballStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag, pos_tag_sents
import string
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('tagsets')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

texto = "Nós somos feitos de poeiras de estrelas. Nós somos uma maneira de os cosmos se auto conhecer. A imaginação nos leva a mundos que sequer existiram, mas sem ela não vamos a lugar algum. Maneiro são as maneiras de maneirismos, imagine se assim não fossem"

sentencas = sent_tokenize(texto, language="portuguese")

print(sentencas)
print(type(sentencas))
print(len(sentencas))

words = word_tokenize(texto, language="portuguese")

print(words)
print(type(words))
print(len(words))

stops = stopwords.words("portuguese")
print(len(stops))
print(stops)

words_wo_stopwords = [w for w in words if w not in stops]

print(words_wo_stopwords)

print(string.punctuation)

texto_wo_stopwords_and_punctuation = [
    w for w in words_wo_stopwords if w not in string.punctuation]

print('---------------------------------')
print('Sem pontuação e sem stopwords')
print(texto_wo_stopwords_and_punctuation)

freq = nltk.FreqDist(texto_wo_stopwords_and_punctuation)
print(freq.most_common(5))
freq_words = freq.pformat


print('---------------------------------')
print('Stem PorterSteamer')
steamer = PorterStemmer()
stem1 = [steamer.stem(words) for words in texto_wo_stopwords_and_punctuation]
print(stem1)

print('---------------------------------')
print('Stem SnowballSteamer')
steamer2 = SnowballStemmer('portuguese')
stem2 = [steamer2.stem(words) for words in texto_wo_stopwords_and_punctuation]
print(stem2)

print('---------------------------------')
print('Stem LancasterSteamer')
steamer3 = LancasterStemmer()
stem3 = [steamer3.stem(words) for words in texto_wo_stopwords_and_punctuation]
print(stem3)
