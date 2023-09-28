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
material = st.text_input('Digite o material do produto:', key='material')
cor = st.text_input('Digite a cor do produto:', key = 'cor')
categoria = st.text_input('Digite a categoria do produto:', key= 'categoria')
altura = st.slider(label='Coloque a altura do produto', min_value=0.0, max_value = 199.0, key='altura')
largura = st.slider(label='Coloque a largura do produto', min_value=0.0, max_value = 199.0,  key='largura')
profundidade = st.slider(label='Coloque a profundidade do produto', min_value=0.0,  max_value = 157.0,  key='profundidade') 




## Carregando o modelo #
pkl_file_path = './data/precificacao_230923_joblib_pl_sem_vm.pkl'
    
# Carregar o arquivo .pkl com joblib
with open(pkl_file_path, 'rb') as model_file:
    modelo =joblib.load(model_file)




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

