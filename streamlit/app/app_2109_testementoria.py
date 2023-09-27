import streamlit as st
import pandas as pd
import streamlit as st
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

# Obter valores do usuário
material = st.text_input('Digite o material do produto:', key='material')
cor = st.text_input('Digite a cor do produto:', key = 'cor')
categoria = st.text_input('Digite a categoria do produto:', key= 'categoria')
altura = st.slider(label='Coloque a altura do produto', min_value=0.0, max_value = 199.0, key='altura')
largura = st.slider(label='Coloque a largura do produto', min_value=0.0, max_value = 199.0,  key='largura')
profundidade = st.slider(label='Coloque a profundidade do produto', min_value=0.0,  max_value = 157.0,  key='profundidade') 

# Criar o DataFrame de entrada
df_input = pd.DataFrame({
    'material': [material],
    'cor': [cor],
    'categoria': [categoria],
    'altura': [altura],    
    'largura': [largura],
    'profundidade': [profundidade]
        
    })

st.dataframe(df_input)

## Carregando o modelo #
pkl_file_path = 'c:/Users/carlo/OneDrive/git-repositorios/tag2u/e-commerce/streamlit/data/precificacao_180923_joblib.pkl'
    
# Carregar o arquivo .pkl com joblib
with open(pkl_file_path, 'rb') as model_file:
    modelo =joblib.load(model_file)