import streamlit as st
import pandas as pd
import streamlit as st
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

#Configuração do título da página
st.set_page_config(page_title='Tag2u')

# st.write('Hello!')

#Elementos de texto
st.header('TAG2U')

## -- Parametros -- #
#Widgets

# Obter valores do usuário
valor_mercado = st.slider(label='Coloque valor de mercado do produto', min_value=0.0, max_value = 4500.0,  key='valor_mercado')
material = st.text_input('Digite o material do produto:', key='material')
cor = st.text_input('Digite a cor do produto:', key = 'cor')
categoria = st.text_input('Digite a categoria do produto:', key= 'categoria')
altura = st.slider(label='Coloque a altura do produto', min_value=0.0, max_value = 230.0, key='altura')
largura = st.slider(label='Coloque a largura do produto', min_value=0.0, max_value = 300.0,  key='largura')
profundidade = st.slider(label='Coloque a profundidade do produto', min_value=0.0,  max_value = 205.0,  key='profundidade') 
tempo_estoque = st.slider(label='Coloque o tempo de estoque do produto', min_value=0.0,  max_value = 321.0,  key='tempo_estoque') 




## Carregando o modelo #
pkl_file_path = './streamlit/data/precificacao_08102023_2_joblib_pl_vm.pkl'
    
# Carregar o arquivo .pkl com joblib
with open(pkl_file_path, 'rb') as model_file:
    modelo =joblib.load(model_file)




# Criar o DataFrame de entrada
df_input = pd.DataFrame({
    'valor_mercado':[valor_mercado],
    'material': [material],
    'cor': [cor],
    'categoria': [categoria],
    'altura': [altura],    
    'largura': [largura],
    'profundidade': [profundidade],
    'tempo_estoque':[tempo_estoque]    
    })

st.dataframe(df_input)

 
def prediction():
    # Verificar os valores de df_input
    st.write("Valores em df_input:")
    st.dataframe(df_input)

    # Realizar a previsão
    prediction = modelo.predict(df_input)[0]
    return prediction


if st.button('Atualizar'):
    valor_produto = prediction()
    st.write(valor_produto)

