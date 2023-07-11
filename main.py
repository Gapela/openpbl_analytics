import pandas as pd
import streamlit as st
from functions import get_all, get_one_email, media_alunos_geral, dados_quiz
from grafico_radar import grafico

#############
### DADOS ###
#############

dados = get_all() #pega todos os dados do data base e retorna uma lista
df = pd.DataFrame(dados) #transforma os dados em um DataFrame
lista_emails = list(df['user_email']) #faz uma lista com todos os emails do DataFrame

###############
### SIDEBAR ###
###############
st.sidebar.header("Menu") #titulo do menu lateral
email = st.sidebar.selectbox('Selecione um aluno:', lista_emails) # dropbox que dá o valor a variavel email

############
### BODY ###
############
st.title("Dashboard Avaliação") #titulo do main body

#################
### TEMPORADA ###
#################

dados_temporada = media_alunos_geral()

# estrutura do streamlit em colunas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label= "Total", value= dados_temporada['total'])
with col2:
    st.metric(label= "Corretas", value= dados_temporada['corretas']) 
with col3:
    st.metric(label= "Erradas", value= dados_temporada['incorretas'])

#DADOS ALUNO
aluno_dados = get_one_email(email)
aluno = dados_quiz(aluno_dados)

st.subheader(f"Aluno: {email.upper()}") #sub-titulo personalizado a partir da variavel email

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label= "Total", value= aluno['total'])
with col2:
    st.metric(label= "Corretas", value= aluno['corretas'])
with col3:
    st.metric(label= "Erradas", value= aluno['incorretas'])

#####################
### GRAFICO RADAR ###
#####################

grafico(aluno, dados_temporada) #grafico radar