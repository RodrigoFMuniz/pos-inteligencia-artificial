import nltk
import dtale
import dtale.app as dtale_app
import wordcloud
import pandas as pd

dtale_app.USE_COLAB = False

data = pd.read_excel('../assets/Vagas_para_Cientista_e_Analista_de_Dados.xlsx')
dtale.show(data)

