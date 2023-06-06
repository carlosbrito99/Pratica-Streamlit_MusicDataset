import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import streamlit as st
import matplotlib.pyplot as plt
#
# pip install streamlit pandas numpy matplotlib seaborn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Fonte de Dados
# https://www.kaggle.com/datasets/suraj520/music-dataset-song-information-and-lyrics?resource=download

import seaborn as sns

data = pd.read_csv("songs.csv")
graph1_type = st.sidebar.selectbox("Gráfico 1: Selecione o tipo de gráfico", ("Barra", "Pizza", "Dispersão", "Histograma", "Boxplot"))
st.dataframe(data)

sns.histplot(data, x='Popularity', kde=True, color='g')

# sidebar
st.sidebar.title("Apresentação dos Dados")

# Adicionando um título
st.title("Análise de Dados do Dataset de Músicas")

# Adicionando uma tabela para mostrar a média de popularidade
st.subheader("Média de popularidade")
music_mean_pop = data.groupby('Artist')['Popularity'].mean()
st.table(music_mean_pop)

# Gráfico de Pizza para mostrar a distribuição de nome por popularidade

st.subheader("Distribuição de Gênero dos Nomes")
music_count = data['Popularity'].value_counts()
fig, ax = plt.subplots()
if graph1_type == "Pizza":
    ax.pie(music_count.values, labels=music_count.index, autopct='%1.1f%%')
    ax.set_title('Distribuição de Popularidade Por Musica')
else:
    sns.barplot(x=music_count.index, y=music_count.values)
    ax.set_xlabel('Artistas')
    ax.set_ylabel('Popularidade')
st.pyplot(fig)