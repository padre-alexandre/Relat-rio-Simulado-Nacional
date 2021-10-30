##### Relatório Simulado Nacional Insper - Jazz Vestibular

##### Base de Dados

### Nome da Avaliação
### Turma
### Nome do aluno (a)
### Login do aluno (a)
### Disciplina
### Frente
### Assunto
### Número da questão
### Alternativa assinalada pelo aluno (a)
### Gabarito
### Certo ou Errado
### Tempo gasto
### Valor da questão

### Importação de bibliotecas

import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from funcoes import *
from matplotlib import pyplot as plt
from st_card import st_card
from st_radial import st_radial
from load_css import local_css


### Configurando a página

st.set_page_config(page_title="Relatório", page_icon="", layout="wide")
st.markdown('<style>body{background-color: #FF00CE}</style>',unsafe_allow_html=True)

local_css("style.css")

### Lista de cores e fontes

# Cor de fundo dos retângulos: #ffd8f8
# Cor de fundo da página: #FFF0FC
# Cor da fonte dos títulos: #FF00CE
# Cor da fonte dos texto: #C81F6D
# Fonte: Arial

### Cabeçalho principal

html_header="""
<head>
<title>Relatório</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<meta charset="utf-8">
<meta name="keywords" content="relatorio diagnostico, simulado nacional, insper">
<meta name="description" content="relatorio diagnostico simulado">
<meta name="author" content="Alexandre Fernandes">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color: #FF00CE; font-family:Georgia"> SIMULADO NACIONAL INSPER<br>
 <h2 style="color: #FF00CE; font-family:Georgia">RELATÓRIO</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""

st.markdown(html_header, unsafe_allow_html=True)

### Leitura das bases de dados

base_resultados_adm_eco_dir = pd.read_csv('./base_resultados_adm_eco_dir.csv')
base_matriz_adm_eco_dir = pd.read_csv('./base_matriz_adm_eco_dir.csv')

### Renomeando colunas e ajustando células vazias

base_adm_eco_dir = pd.merge(base_resultados_adm_eco_dir, base_matriz_adm_eco_dir, on = 'num_exercicio', how = 'inner')
base_adm_eco_dir.rename(columns = {'atividade_nome':'Nome da avaliação','turma':'Turma','aluno_nome':'Nome do aluno(a)','aluno_login':'Login do aluno(a)','num_exercicio':'Número da questão','resp_aluno':'Resposta do aluno(a)','gabarito':'Gabarito','certo_ou_errado':'Certo ou errado','tempo_no_exercicio(s)':'Tempo na questão','valor_do_exercicio':'Valor da questão','disciplina':'Disciplina','frente':'Frente','assunto':'Assunto'}, inplace = True)
base_adm_eco_dir['Resposta do aluno(a)'] = base_adm_eco_dir['Resposta do aluno(a)'].fillna('x')
base_adm_eco_dir['Tempo na questão'] = base_adm_eco_dir['Tempo na questão'].fillna(0)
base_adm_eco_dir['Valor da questão'] = base_adm_eco_dir['Valor da questão'].apply(lambda x: float(x.replace(".","").replace(",",".")))

### Resultados Gerais

base_adm_eco_dir['Acerto'] = 0
base_adm_eco_dir['Nota na questão'] = 0.00

for i in range(len(base_adm_eco_dir['Nome da avaliação'])):
    if base_adm_eco_dir['Certo ou errado'][i] == 'certo':
        base_adm_eco_dir['Acerto'][i] = 1
        base_adm_eco_dir['Nota na questão'][i] = base_adm_eco_dir['Acerto'][i]*base_adm_eco_dir['Valor da questão'][i]

resultados_gerais = base_adm_eco_dir.groupby(['Nome da avaliação','Turma','Nome do aluno(a)']).sum().reset_index()
resultados_gerais2 = resultados_gerais.drop(columns = ['Número da questão'])
resultados_gerais3 = resultados_gerais2.sort_values(by = 'Nota na questão', ascending = False).reset_index(drop = True)                

### Selecionar o aluno

nome_aluno = resultados_gerais3.sort_values(by = 'Nome do aluno(a)')
nome_aluno2 = inserir_linha(pd.DataFrame(data = nome_aluno['Nome do aluno(a)'].unique()),pd.DataFrame({0: 'Nome'}, index=[-1]))
nome_aluno3 = str(st.selectbox('Selecione o aluno(a)',nome_aluno2[0]))

html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)
if nome_aluno3 != 'Nome':

    resultados_gerais_aluno = resultados_gerais3[resultados_gerais3['Nome do aluno(a)'] == nome_aluno3].reset_index()
    resultados_gerais_aluno.rename(columns = {'index':'Classificação'}, inplace = True)
    resultados_gerais_aluno['Classificação'][0] = resultados_gerais_aluno['Classificação'][0] + 1

    ### Resultados gerais do aluno

    numero_candidatos = len(resultados_gerais3['Nome do aluno(a)'])

    #### Resultados gerais por disciplina
    #
    #resultados_gerais_disciplina = base_adm_eco_dir.groupby(['Nome da avaliação','Turma','Nome do aluno(a)','Disciplina']).sum().reset_index()
    #resultados_gerais_disciplina2 = resultados_gerais_disciplina.drop(columns = ['Número da questão'])
    #resultados_gerais_disciplina3 = resultados_gerais_disciplina2.sort_values(by = 'Nota na questão', ascending = False).reset_index(drop = True)
    #resultados_gerais_disciplina4 = resultados_gerais_disciplina3.groupby('Disciplina').mean().reset_index()
    #resultados_gerais_disciplina5 = resultados_gerais_disciplina4.sort_values(by = 'Disciplina', ascending = False)
    #
    #### Resultados do aluno por disciplina
    #
    #resultados_disciplina_aluno = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Nome do aluno(a)'] == nome_aluno3].reset_index()
    #resultados_disciplina_aluno2 = resultados_disciplina_aluno.sort_values(by = 'Disciplina', ascending = False)
    #st.dataframe(resultados_gerais_disciplina5)
    #
    #fig = px.bar(resultados_disciplina_aluno2, x = resultados_disciplina_aluno2['Disciplina'], y = resultados_disciplina_aluno2['Acerto'], range_y=[0,30], color_discrete_sequence = [cor_barra]*len(resultados_disciplina_aluno2))
    #fig.add_scatter(x = resultados_gerais_disciplina5['Disciplina'], y = resultados_gerais_disciplina5['Acerto'],mode='lines+markers', name = 'Média dos alunos', line=dict(color='black'))     
    #st.plotly_chart(fig)               
    #
    #
    #


    #st.markdown(""" <style>
    ##MainMenu {visibility: hidden;}
    #footer {visibility: hidden;}
    #</style> """, unsafe_allow_html=True)

    html_card_header1="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 5px; width: 350px;
       height: 50px;">
        <h3 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; font-size:50%; text-align: center; padding: 0px 0;">Resultado Geral</h3>
      </div>
    </div>
    """
    html_card_footer1="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 1rem;; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Nota máxima: 1000</p>
      </div>
    </div>
    """
    html_card_header2="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 5px; width: 350px;
       height: 50px;">
        <h3 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Número de acertos</h3>
      </div>
    </div>
    """
    html_card_footer2="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 1rem;; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Total de questões: 90</p>
      </div>
    </div>
    """
    html_card_header3="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 5px; width: 350px;
       height: 50px;">
        <h3 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Classificação</h3>
      </div>
    </div>
    """
    html_card_footer3="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 1rem;; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Quantidade de alunos: """+str(numero_candidatos)+"""</p>
      </div>
    </div>
    """

    ### Block 1#########################################################################################
    with st.container():
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,20,1,20,1,20,1])
        with col1:
            st.write("")
        with col2:
            st.markdown(html_card_header1, unsafe_allow_html=True)
            fig_c1 = go.Figure(go.Indicator(
                mode="number",
                value=round(resultados_gerais_aluno['Nota na questão'][0],1),
                number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': 46, 'relative': False},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c1.update_layout(autosize=False,
                                 width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                                 paper_bgcolor="#FFF0FC", font={'size': 20})
            st.plotly_chart(fig_c1)
            st.markdown(html_card_footer1, unsafe_allow_html=True)
        with col3:
            st.write("")
        with col4:
            st.markdown(html_card_header2, unsafe_allow_html=True)
            fig_c2 = go.Figure(go.Indicator(
                mode="number",
                value=resultados_gerais_aluno['Acerto'][0],
                number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}, 'valueformat': ',f'},
                delta={'position': "bottom", 'reference': 92700},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c2.update_layout(autosize=False,
                                 width=350, height=90, margin=dict(l=20, r=20, b=20, t=20),
                                 paper_bgcolor="#FFF0FC", font={'size': 20})
            fig_c2.update_traces(delta_decreasing_color="#3D9970",
                                 delta_increasing_color="#FF4136",
                                 delta_valueformat='f',
                                 selector=dict(type='indicator'))
            st.plotly_chart(fig_c2)
            st.markdown(html_card_footer2, unsafe_allow_html=True)
        with col5:
            st.write("")
        with col6:
            st.markdown(html_card_header3, unsafe_allow_html=True)
            fig_c3 = go.Figure(go.Indicator(
                mode="number",
                value=resultados_gerais_aluno['Classificação'][0],
                number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': 1, 'relative': False},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c3.update_layout(autosize=False,
                                 width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                                 paper_bgcolor="#FFF0FC", font={'size': 20})
            fig_c3.update_traces(delta_decreasing_color="#3D9970",
                                 delta_increasing_color="#FF4136",
                                 delta_valueformat='.3f',
                                 selector=dict(type='indicator'))
            st.plotly_chart(fig_c3)
            st.markdown(html_card_footer3, unsafe_allow_html=True)
        with col7:
            st.write("")
    html_br="""
    <br>
    """
    st.markdown(html_br, unsafe_allow_html=True)