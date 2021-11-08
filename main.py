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

base_resultados_adm_eco_dir = pd.read_csv('./Jazz Vestibular - 2022.1 - Operação - [RELATÓRIO] Matriz de Questões.csv')
base_matriz_adm_eco_dir = pd.read_csv('./Jazz Vestibular - 2022.1 - Operação - [RELATÓRIO] Base de Dados.csv')

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

resultados_gerais = base_adm_eco_dir.groupby(['Nome da avaliação','Turma','Nome do aluno(a)','Login do aluno(a)']).sum().reset_index()

for i in range(len(resultados_gerais['Nome do aluno(a)'])):
    if resultados_gerais['Turma'][i] == 'Simulado Nacional - Engenharia' and resultados_gerais['Nome da avaliação'][i] == 'Simulado Nacional Insper 1º fase - Matemática e Linguagens':
        resultados_gerais['Nota na questão'][i] = (1/3)*resultados_gerais['Nota na questão'][i]
    elif resultados_gerais['Turma'][i] == 'Simulado Nacional - Ciências da Computação' and resultados_gerais['Nome da avaliação'][i] == 'Simulado Nacional Insper 1º fase - Matemática e Linguagens':
        resultados_gerais['Nota na questão'][i] = (1/3)*resultados_gerais['Nota na questão'][i]
    elif  resultados_gerais['Nome da avaliação'][i] == 'Simulado Nacional Insper 1º fase - Matemática e Linguagens':
        resultados_gerais['Nota na questão'][i] = (750/2000)*resultados_gerais['Nota na questão'][i]
    
    if resultados_gerais['Nome da avaliação'][i] == 'Simulado Nacional Insper 1º fase - Ciências Humanas':
        resultados_gerais['Nota na questão'][i] = (250/1000)*resultados_gerais['Nota na questão'][i]

    if resultados_gerais['Nome da avaliação'][i] == 'Simulado Nacional Insper 1º fase - Ciências da Natureza':
        resultados_gerais['Nota na questão'][i] = (1/3)*resultados_gerais['Nota na questão'][i]
    
resultados_gerais2 = resultados_gerais.groupby(['Turma','Nome do aluno(a)','Login do aluno(a)']).sum().reset_index()

#resultados_gerais2 = resultados_gerais.drop(columns = ['Número da questão'])
resultados_gerais3 = resultados_gerais2.sort_values(by = 'Nota na questão', ascending = False).reset_index(drop = True)                


### Selecionar o aluno
login_aluno = st.text_input('Digite o seu login', '')

#nome_aluno = resultados_gerais3.sort_values(by = 'Nome do aluno(a)')
#nome_aluno2 = inserir_linha(pd.DataFrame(data = nome_aluno['Nome do aluno(a)'].unique()),pd.DataFrame({0: 'Nome'}, index=[-1]))
#nome_aluno3 = str(st.selectbox('Selecione o aluno(a)',nome_aluno2[0]))
nome_aluno3 = resultados_gerais3[resultados_gerais3['Login do aluno(a)'] == login_aluno]['Nome do aluno(a)'].reset_index()

html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)
if len(nome_aluno3['Nome do aluno(a)']) > 0:

    resultados_gerais_aluno = resultados_gerais3[resultados_gerais3['Nome do aluno(a)'] == nome_aluno3['Nome do aluno(a)'][0]].reset_index()
    resultados_gerais_aluno.rename(columns = {'index':'Classificação'}, inplace = True)
    resultados_gerais_aluno['Classificação'][0] = resultados_gerais_aluno['Classificação'][0] + 1

    resultados_gerais4 = resultados_gerais3[resultados_gerais3['Nota na questão'] > 0]

    resultados_gerais5 = resultados_gerais4.groupby('Login do aluno(a)').mean().reset_index()
    
    alunos_fizeram = pd.DataFrame()
    alunos_fizeram['Nome do aluno(a)'] = resultados_gerais4['Nome do aluno(a)']

    ### Resultados gerais do aluno

    numero_candidatos = len(resultados_gerais4['Nome do aluno(a)'])
    aux = resultados_gerais4[resultados_gerais4['Turma'] == 'Simulado Nacional - Engenharia']
    aux2 = resultados_gerais4[resultados_gerais4['Turma'] == 'Simulado Nacional - Ciências da Computação']
    numero_eng = len(aux['Nome do aluno(a)']) + len(aux2['Nome do aluno(a)'])

    html_header_geral="""
    <h2 style="font-size:200%; color: #FF00CE; font-family:Georgia"> GERAL<br>
     <hr style= "  display: block;
      margin-top: 0.5em;
      margin-bottom: 0.5em;
      margin-left: auto;
      margin-right: auto;
      border-style: inset;
      border-width: 1.5px;"></h2>
    """
    st.markdown(html_header_geral, unsafe_allow_html=True)
    
    html_card_header1="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <h4 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Nota</h4>
      </div>
    </div>
    """
    html_card_footer1="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Nota máxima: 1000</p>
      </div>
    </div>
    """

    html_card_footer_med1="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Média Geral: """+str(int(round(resultados_gerais5['Nota na questão'][0],0)))+"""</p>
      </div>
    </div>
    """

    html_card_header2="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <h4 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Número de acertos</h4>
      </div>
    </div>
    """
    html_card_footer2="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Total de questões: 90</p>
      </div>
    </div>
    """
    html_card_footer_med2="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Média Geral: """+str(int(round(resultados_gerais5['Acerto'][0],0)))+"""</p>
      </div>
    </div>
    """
    html_card_header3="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <h4 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Classificação</h4>
      </div>
    </div>
    """
    html_card_footer3="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
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
                mode="number+delta",
                value=round(resultados_gerais_aluno['Nota na questão'][0],1),
                number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais5['Nota na questão'][0],-1),0)), 'relative': False},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c1.update_layout(autosize=False,
                                 width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                 paper_bgcolor="#FFF0FC", font={'size': 20})
            fig_c1.update_traces(delta_decreasing_color="#FF4136",
                                delta_increasing_color="#3D9970",
                                delta_valueformat='.0f',
                                selector=dict(type='indicator'))
            st.plotly_chart(fig_c1)
            st.markdown(html_card_footer1, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_card_footer_med1, unsafe_allow_html=True)
        with col3:
            st.write("")
        with col4:
            st.markdown(html_card_header2, unsafe_allow_html=True)
            fig_c2 = go.Figure(go.Indicator(
                mode="number+delta",
                value=resultados_gerais_aluno['Acerto'][0],
                number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}, 'valueformat': ',f'},
                delta={'position': "bottom", 'reference': int(round(resultados_gerais5['Acerto'][0],0))},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c2.update_layout(autosize=False,
                                 width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                 paper_bgcolor="#FFF0FC", font={'size': 20})
            fig_c2.update_traces(delta_decreasing_color="#FF4136",
                                 delta_increasing_color="#3D9970",
                                 delta_valueformat='f',
                                 selector=dict(type='indicator'))
            st.plotly_chart(fig_c2)
            st.markdown(html_card_footer2, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_card_footer_med2, unsafe_allow_html=True)
        with col5:
            st.write("")
        with col6:
            st.markdown(html_card_header3, unsafe_allow_html=True)
            fig_c3 = go.Figure(go.Indicator(
                mode="number",
                value=resultados_gerais_aluno['Classificação'][0],
                number={'suffix': "º", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                delta={'position': "bottom", 'reference': 1, 'relative': False},
                domain={'x': [0, 1], 'y': [0, 1]}))
            fig_c3.update_layout(autosize=False,
                                 width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                 paper_bgcolor="#FFF0FC", font={'size': 20})
            fig_c3.update_traces(delta_decreasing_color="#3D9970",
                                 delta_increasing_color="#FF4136",
                                 delta_valueformat='.3f',
                                 selector=dict(type='indicator'))
            st.plotly_chart(fig_c3)
            st.markdown(html_card_footer3, unsafe_allow_html=True)
        with col7:
            st.write("")
    
    st.markdown(html_br, unsafe_allow_html=True)
    st.markdown(html_br, unsafe_allow_html=True)

    ponto = str(round(100*(numero_candidatos-(resultados_gerais_aluno['Classificação'][0]-1))/numero_candidatos,0)).find('.')
    texto = str(round(100*(numero_candidatos-(resultados_gerais_aluno['Classificação'][0]-1))/numero_candidatos,0))[0:ponto]
    html_card_header_destaques_gerais="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 60px; width: 495px;
       height: 150px;">
        <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Você foi melhor que """+texto+"""% dos alunos!</h5>
      </div>
    </div>
    """    
    ### Block 1#########################################################################################
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([9,25,2,25,4])
        with col1:
            st.write("")
        with col2:
            # create the bins
            counts, bins = np.histogram(resultados_gerais4['Nota na questão'], bins=range(0, 1100, 100))
            bins = 0.5 * (bins[:-1] + bins[1:])
            fig = px.bar(x=bins, y=counts, labels={'x':'Nota na questão', 'y':'Número de alunos'})
            fig.update_layout(title={'text': "Distribuição de notas", 'x': 0.5}, paper_bgcolor="#FFF0FC", 
                           plot_bgcolor="#FFF0FC", font={'color': "#C81F6D", 'size': 14, 'family': "Georgia"}, height=400,
                           width=540,
                           legend=dict(orientation="h",
                                       yanchor="top",
                                       y=0.99,
                                       xanchor="left",
                                       x=0.01),
                           margin=dict(l=1, r=1, b=1, t=30))
            fig.add_vline(x=int(round(resultados_gerais_aluno['Nota na questão'][0],1)), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
            fig.add_vline(x=int(round(truncar(resultados_gerais5['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
            fig.update_xaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=6, rangemode="tozero",
                          showgrid=False, gridwidth=0.5, gridcolor='#f6f6f6')
            fig.update_yaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=10, rangemode="tozero",
                          showgrid=True, gridwidth=0.5, gridcolor='#f6f6f6')
            fig.update_traces(marker_color='#01e1e1')
            st.plotly_chart(fig)
        with col3:
            st.write("")
        with col4:
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_card_header_destaques_gerais, unsafe_allow_html=True)
        with col5:
            st.write("")
        
    #### Resultados gerais por disciplina
    
    base_alunos_fizeram = base_adm_eco_dir[base_adm_eco_dir['Nome do aluno(a)'].isin(alunos_fizeram['Nome do aluno(a)'])].reset_index(drop = True)
    
    resultados_gerais_disciplina = base_alunos_fizeram.groupby(['Turma','Login do aluno(a)','Nome do aluno(a)','Disciplina']).sum().reset_index()
    resultados_gerais_disciplina2 = resultados_gerais_disciplina.drop(columns = ['Número da questão'])
    resultados_gerais_disciplina3 = resultados_gerais_disciplina2.sort_values(by = 'Nota na questão', ascending = False).reset_index(drop = True)
    resultados_gerais_disciplina4 = resultados_gerais_disciplina3.groupby('Disciplina').mean().reset_index()
    resultados_gerais_disciplina5 = resultados_gerais_disciplina4.sort_values(by = 'Disciplina', ascending = False)
    
    ### Resultados do aluno por disciplina
    
    resultados_disciplina_aluno = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Login do aluno(a)'] == login_aluno].reset_index()
    resultados_disciplina_aluno2 = resultados_disciplina_aluno.sort_values(by = 'Disciplina', ascending = False)
    
    resultados_matematica = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Matemática'].reset_index()
    resultados_linguagens = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Linguagens'].reset_index()
    resultados_ciencias_hum = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Ciências Humanas'].reset_index()
    resultados_ciencias_nat = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Ciências da Natureza'].reset_index()

    resultados_gerais_disciplina3_mat = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Matemática'].reset_index(drop = True).reset_index()
    resultados_gerais_disciplina3_lin = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Linguagens'].reset_index(drop = True).reset_index()
    resultados_gerais_disciplina3_hum = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Ciências Humanas'].reset_index(drop = True).reset_index()
    resultados_gerais_disciplina3_nat = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Ciências da Natureza'].reset_index(drop = True).reset_index()
            
    classificacao_aluno_mat = resultados_gerais_disciplina3_mat[resultados_gerais_disciplina3_mat['Login do aluno(a)'] == login_aluno].reset_index()
    classificacao_aluno_lin = resultados_gerais_disciplina3_lin[resultados_gerais_disciplina3_lin['Login do aluno(a)'] == login_aluno].reset_index()
    classificacao_aluno_hum = resultados_gerais_disciplina3_hum[resultados_gerais_disciplina3_hum['Login do aluno(a)'] == login_aluno].reset_index()
    classificacao_aluno_nat = resultados_gerais_disciplina3_nat[resultados_gerais_disciplina3_nat['Login do aluno(a)'] == login_aluno].reset_index()  

    resultados_gerais_disciplina_med_mat = resultados_gerais_disciplina5[resultados_gerais_disciplina5['Disciplina'] == 'Matemática'].reset_index(drop = True)
    resultados_gerais_disciplina_med_lin = resultados_gerais_disciplina5[resultados_gerais_disciplina5['Disciplina'] == 'Linguagens'].reset_index(drop = True)
    resultados_gerais_disciplina_med_hum = resultados_gerais_disciplina5[resultados_gerais_disciplina5['Disciplina'] == 'Ciências Humanas'].reset_index(drop = True)
    resultados_gerais_disciplina_med_nat = resultados_gerais_disciplina5[resultados_gerais_disciplina5['Disciplina'] == 'Ciências da Natureza'].reset_index(drop = True)

    if len(resultados_ciencias_hum['Disciplina']) == 0:
        resultados_ciencias_fim = resultados_ciencias_nat.copy()
        resultados_gerais_disciplina3_fim = resultados_gerais_disciplina3_nat.copy()
        classificacao_aluno_fim = classificacao_aluno_nat.copy()
        resultados_gerais_disciplina_med_cie = resultados_gerais_disciplina_med_nat.copy()
    else:
        resultados_ciencias_fim = resultados_ciencias_hum.copy()
        resultados_gerais_disciplina3_fim = resultados_gerais_disciplina3_hum.copy()
        classificacao_aluno_fim = classificacao_aluno_hum.copy()
        resultados_gerais_disciplina_med_cie = resultados_gerais_disciplina_med_hum.copy()

    html_card_header1_disc="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <h4 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Nota</h4>
      </div>
    </div>
    """
    html_card_footer1_disc="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Nota máxima: 1000</p>
      </div>
    </div>
    """
    html_card_footer1_disc_med_mat="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_mat['Nota na questão'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    html_card_footer1_disc_med_lin="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    if len(resultados_ciencias_hum['Nota na questão'] == 0):
        html_card_footer1_disc_med_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_hum['Nota na questão'][0],-1),0)))+"""</p>
          </div>
        </div>
        """
    else:
        html_card_footer1_disc_med_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_nat['Nota na questão'][0],-1),0)))+"""</p>
          </div>
        </div>
        """
    html_card_header2_disc="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <h4 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Número de acertos</h4>
      </div>
    </div>
    """
    html_card_footer2_disc="""
    <div class="card">
      <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Total de questões: 30</p>
      </div>
    </div>
    """
    html_card_footer2_disc_med_mat="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_mat['Acerto'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    html_card_footer2_disc_med_lin="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_lin['Acerto'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    if resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Engenharia' and resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Ciências da Computação':
        html_card_footer2_disc_med_cie="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_hum['Acerto'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    else:
        html_card_footer2_disc_med_cie="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(round(truncar(resultados_gerais_disciplina_med_nat['Acerto'][0],-1),0)))+"""</p>
      </div>
    </div>
    """  
    html_card_header3_disc="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 12px; width: 350px;
       height: 50px;">
        <h4 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Classificação</h4>
      </div>
    </div>
    """
    html_card_footer3_disc_matlin="""
        <div class="card">
          <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Quantidade de alunos: """+str(numero_candidatos)+"""</p>
          </div>
        </div>
        """
    if resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Engenharia' and resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Ciências da Computação':
        html_card_footer3_disc="""
        <div class="card">
          <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Quantidade de alunos: """+str(numero_candidatos-numero_eng)+"""</p>
          </div>
        </div>
        """
    else:
        html_card_footer3_disc="""
        <div class="card">
          <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffd8f8; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 0px 0;">Quantidade de alunos: """+str(numero_eng)+"""</p>
          </div>
        </div>
        """

    matematica_detalhes = base_alunos_fizeram[base_alunos_fizeram['Disciplina'] == 'Matemática']
    
    matematica_detalhes_media = matematica_detalhes.groupby('Assunto').mean().reset_index()
    
    matematica_aluno = matematica_detalhes[matematica_detalhes['Login do aluno(a)'] == login_aluno]
    
    matematica_aluno_media = matematica_aluno.groupby('Assunto').mean().reset_index()
    matematica_aluno_media2 = matematica_aluno.groupby('Assunto').count().reset_index()
    matematica_aluno_media3 = pd.DataFrame()
    matematica_aluno_media3['Assunto'] = matematica_aluno_media2['Assunto']
    matematica_aluno_media3['Número da questão'] = matematica_aluno_media2['Número da questão']

    matematica_tabela = pd.merge(matematica_aluno_media,matematica_detalhes_media, on = 'Assunto', how = 'inner')
    matematica_tabela2 = matematica_tabela.drop(columns = ['Número da questão_x','Número da questão_y','Valor da questão_x','Valor da questão_y','Nota na questão_x','Nota na questão_y','Tempo na questão_x','Tempo na questão_y'])
    matematica_tabela2.rename(columns = {'Acerto_x':'Resultado Individual decimal','Acerto_y':'Resultado Geral decimal'}, inplace = True)
    matematica_tabela2['Resultado Geral'] = ''
    matematica_tabela2['Resultado Individual'] = ''
    for i in range(len(matematica_tabela2['Assunto'])):
        matematica_tabela2['Resultado Geral'][i] = "{0:.0%}".format(matematica_tabela2['Resultado Geral decimal'][i])
        matematica_tabela2['Resultado Individual'][i] = "{0:.0%}".format(matematica_tabela2['Resultado Individual decimal'][i])
    matematica_tabela3 = pd.merge(matematica_tabela2,matematica_aluno_media3, on = 'Assunto', how = 'inner')
    matematica_tabela3.rename(columns = {'Número da questão':'Quantidade de questões'}, inplace = True)
    matematica_tabela3 = matematica_tabela3[['Assunto','Quantidade de questões','Resultado Individual', 'Resultado Geral','Resultado Individual decimal', 'Resultado Geral decimal']]
    matematica_tabela3['Status'] = ''
    for i in range(len(matematica_tabela3['Assunto'])):
        if matematica_tabela3['Resultado Individual decimal'][i] == 0:
            matematica_tabela3['Status'][i] = "🔴" 
        elif matematica_tabela3['Resultado Individual decimal'][i] >= matematica_tabela3['Resultado Geral decimal'][i]:
            matematica_tabela3['Status'][i] = "🟢"
        elif matematica_tabela3['Resultado Individual decimal'][i] - matematica_tabela3['Resultado Geral decimal'][i] > - 0.25:
            matematica_tabela3['Status'][i] = "🟡"
        else:
            matematica_tabela3['Status'][i] = "🔴"
    matematica_tabela3['Diferença'] = ''
    for i in range(len(matematica_tabela3['Assunto'])):
        matematica_tabela3['Diferença'][i] = matematica_tabela3['Resultado Individual decimal'][i] - matematica_tabela3['Resultado Geral decimal'][i]
    
    matematica_tabela_ordenado = matematica_tabela3.sort_values(by = 'Diferença')

    matematica_tabela_verde = matematica_tabela_ordenado[matematica_tabela_ordenado['Status'] == '🟢']
    matematica_tabela_verde_ordenado = matematica_tabela_verde.sort_values(by = 'Diferença', ascending = False).reset_index(drop = True)
    
    matematica_tabela_vermelho = matematica_tabela_ordenado[matematica_tabela_ordenado['Status'] == '🔴']
    matematica_tabela_vermelho_ordenado = matematica_tabela_vermelho.sort_values(by = 'Diferença', ascending = True).reset_index(drop = True)

    html_header_mat="""
    <h2 style="font-size:200%; color: #FF00CE; font-family:Georgia"> MATEMÁTICA<br>
     <hr style= "  display: block;
      margin-top: 0.5em;
      margin-bottom: 0.5em;
      margin-left: auto;
      margin-right: auto;
      border-style: inset;
      border-width: 1.5px;"></h2>
    """
    if len(resultados_matematica['Nome do aluno(a)']) != 0:

        ### MATEMÁTICA

        st.markdown(html_header_mat, unsafe_allow_html=True)

        ### Block 1#########################################################################################
        with st.container():
            col1, col2, col3, col4, col5, col6, col7 = st.columns([1,20,1,20,1,20,1])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_card_header1_disc, unsafe_allow_html=True)
                fig_c1 = go.Figure(go.Indicator(
                    mode="number+delta",
                    value=round(resultados_matematica['Nota na questão'][0],1),
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais_disciplina_med_mat['Nota na questão'][0],-1),0)), 'relative': False},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c1.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                st.plotly_chart(fig_c1)
                st.markdown(html_card_footer1_disc, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_footer1_disc_med_mat, unsafe_allow_html=True)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_card_header2_disc, unsafe_allow_html=True)
                fig_c2 = go.Figure(go.Indicator(
                    mode="number+delta",
                    value=resultados_matematica['Acerto'][0],
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}, 'valueformat': ',f'},
                    delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais_disciplina_med_mat['Acerto'][0],-1),0))},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c2.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                fig_c2.update_traces(delta_decreasing_color="#FF4136",
                                 delta_increasing_color="#3D9970",
                                 delta_valueformat='f',
                                 selector=dict(type='indicator'))
                st.plotly_chart(fig_c2)
                st.markdown(html_card_footer2_disc, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_footer2_disc_med_mat, unsafe_allow_html=True)
            with col5:
                st.write("")
            with col6:
                st.markdown(html_card_header3_disc, unsafe_allow_html=True)
                fig_c3 = go.Figure(go.Indicator(
                    mode="number",
                    value=classificacao_aluno_mat['index'][0]+1,
                    number={'suffix': "º", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': 1, 'relative': False},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c3.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                fig_c3.update_traces(delta_decreasing_color="#3D9970",
                                     delta_increasing_color="#FF4136",
                                     delta_valueformat='.3f',
                                     selector=dict(type='indicator'))
                st.plotly_chart(fig_c3)
                st.markdown(html_card_footer3_disc_matlin, unsafe_allow_html=True)
            with col7:
                st.write("")
        html_br="""
        <br>
        """
        ponto = str(round(100*(numero_candidatos-(classificacao_aluno_mat['index'][0]))/numero_candidatos,0)).find('.')
        texto = str(round(100*(numero_candidatos-(classificacao_aluno_mat['index'][0]))/numero_candidatos,0))[0:ponto]
        html_card_header_destaques_mat="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 60px; width: 495px;
           height: 150px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Você foi melhor que """+texto+"""% dos alunos!</h5>
          </div>
        </div>
        """  

        st.markdown(html_br, unsafe_allow_html=True)
        st.markdown(html_br, unsafe_allow_html=True)

        with st.container():
            col1, col2, col3, col4, col5 = st.columns([9,25,2,25,4])
            with col1:
                st.write("")
            with col2:
               # create the bins
                counts, bins = np.histogram(resultados_gerais_disciplina3_mat['Nota na questão'], bins=range(0, 1100, 100))
                bins = 0.5 * (bins[:-1] + bins[1:])
                fig = px.bar(x=bins, y=counts, labels={'x':'Nota na questão', 'y':'Número de alunos'})
                fig.update_layout(title={'text': "Distribuição de notas", 'x': 0.5}, paper_bgcolor="#FFF0FC", 
                               plot_bgcolor="#FFF0FC", font={'color': "#C81F6D", 'size': 14, 'family': "Georgia"}, height=400,
                               width=540,
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.01),
                               margin=dict(l=1, r=1, b=1, t=30))
                fig.add_vline(x=int(resultados_matematica['Nota na questão']), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
                fig.add_vline(x=int(round(truncar(resultados_gerais_disciplina_med_mat['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
                fig.update_xaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=6, rangemode="tozero",
                              showgrid=False, gridwidth=0.5, gridcolor='#f6f6f6')
                fig.update_yaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=10, rangemode="tozero",
                              showgrid=True, gridwidth=0.5, gridcolor='#f6f6f6')
                fig.update_traces(marker_color='#01e1e1')
                st.plotly_chart(fig)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_header_destaques_mat, unsafe_allow_html=True)
            with col5:
                st.write("")

        st.markdown(html_br, unsafe_allow_html=True)
        
        html_table=""" 
        <table bordercolor=#FFF0FC>
          <tr style="background-color:#ffd8f8; height: 90px; color:#C81F6D; font-family:Georgia; font-size: 17px; text-align: center">
            <th style="width:350px; bordercolor=#FFF0FC">Assunto</th>
            <th style="width:150px; bordercolor=#FFF0FC">Quantidade de questões</th>
            <th style="width:150px; bordercolor=#FFF0FC">Resultado Individual</th>
            <th style="width:150px; bordercolor=#FFF0FC">Resultado Geral</th>
            <th style="width:150px; bordercolor=#FFF0FC">Status</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][0])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][0])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][0])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][0])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][0])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][1])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][1])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][1])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][1])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][1])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][2])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][2])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][2])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][2])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][2])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][3])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][3])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][3])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][3])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][3])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][4])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][4])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][4])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][4])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][4])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][5])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][5])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][5])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][5])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][5])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][6])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][6])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][6])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][6])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][6])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][7])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][7])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][7])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][7])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][7])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][8])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][8])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][8])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][8])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][8])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][9])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][9])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][9])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][9])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][9])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][10])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][10])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][10])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][10])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][10])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][11])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][11])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][11])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][11])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][11])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][12])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][12])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][12])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][12])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][12])+"""</th>
          </tr>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][13])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][13])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][13])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][13])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][13])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(matematica_tabela3['Assunto'][14])+"""</th>
            <th>"""+str(matematica_tabela3['Quantidade de questões'][14])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Individual'][14])+"""</th>
            <th>"""+str(matematica_tabela3['Resultado Geral'][14])+"""</th>
            <th>"""+str(matematica_tabela3['Status'][14])+"""</th>
          </tr>

        </table>
        """

        html_card_header_melhores_resultados="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 30px; width: 495px;
           height: 100px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Seus melhores resultados</h5>
          </div>
        </div>
        """
        if len(matematica_tabela_verde_ordenado) > 0:
            html_card_header_melhores_resultados1="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(matematica_tabela_verde_ordenado['Assunto'][0])+"""</p>
              </div>
            </div>
            """
        if len(matematica_tabela_verde_ordenado) > 1:
            html_card_header_melhores_resultados2="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(matematica_tabela_verde_ordenado['Assunto'][1])+"""</p>
              </div>
            </div>
            """
        if len(matematica_tabela_verde_ordenado) > 2:
            html_card_header_melhores_resultados3="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(matematica_tabela_verde_ordenado['Assunto'][2])+"""</p>
              </div>
            </div>
            """
        html_card_header_pontos_melhorar="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 30px; width: 495px;
           height: 100px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Pontos que você pode melhorar</h5>
          </div>
        </div>
        """
        if len(matematica_tabela_vermelho_ordenado) > 0:
            html_card_header_pontos_melhorar1="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(matematica_tabela_vermelho_ordenado['Assunto'][0])+"""</p>
              </div>
            </div>
            """
        if len(matematica_tabela_vermelho_ordenado) > 1:
            html_card_header_pontos_melhorar2="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(matematica_tabela_vermelho_ordenado['Assunto'][1])+"""</p>
              </div>
            </div>
            """
        if len(matematica_tabela_vermelho_ordenado) > 2:
            html_card_header_pontos_melhorar3="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(matematica_tabela_vermelho_ordenado['Assunto'][2])+"""</p>
              </div>
            </div>
            """
        
        with st.container():
            col1, col2, col3, col4 = st.columns([0.5,12,0.5,10.5])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_table, unsafe_allow_html=True)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_card_header_melhores_resultados, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                if len(matematica_tabela_verde_ordenado) > 0:
                    st.markdown(html_card_header_melhores_resultados1, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(matematica_tabela_verde_ordenado) > 1:
                    st.markdown(html_card_header_melhores_resultados2, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(matematica_tabela_verde_ordenado) > 2:
                    st.markdown(html_card_header_melhores_resultados3, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)

                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_header_pontos_melhorar, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                if len(matematica_tabela_vermelho_ordenado) > 0:
                    st.markdown(html_card_header_pontos_melhorar1, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(matematica_tabela_vermelho_ordenado) > 1:
                    st.markdown(html_card_header_pontos_melhorar2, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(matematica_tabela_vermelho_ordenado) > 2:
                    st.markdown(html_card_header_pontos_melhorar3, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)

        st.markdown(html_br, unsafe_allow_html=True)

        ### LINGUAGENS

        linguagens_detalhes = base_alunos_fizeram[base_alunos_fizeram['Disciplina'] == 'Linguagens']
    
        linguagens_detalhes_media = linguagens_detalhes.groupby('Assunto').mean().reset_index()

        linguagens_aluno = linguagens_detalhes[linguagens_detalhes['Login do aluno(a)'] == login_aluno]

        linguagens_aluno_media = linguagens_aluno.groupby('Assunto').mean().reset_index()
        linguagens_aluno_media2 = linguagens_aluno.groupby('Assunto').count().reset_index()
        linguagens_aluno_media3 = pd.DataFrame()
        linguagens_aluno_media3['Assunto'] = linguagens_aluno_media2['Assunto']
        linguagens_aluno_media3['Número da questão'] = linguagens_aluno_media2['Número da questão']

        linguagens_tabela = pd.merge(linguagens_aluno_media,linguagens_detalhes_media, on = 'Assunto', how = 'inner')
        linguagens_tabela2 = linguagens_tabela.drop(columns = ['Número da questão_x','Número da questão_y','Valor da questão_x','Valor da questão_y','Nota na questão_x','Nota na questão_y','Tempo na questão_x','Tempo na questão_y'])
        linguagens_tabela2.rename(columns = {'Acerto_x':'Resultado Individual decimal','Acerto_y':'Resultado Geral decimal'}, inplace = True)
        linguagens_tabela2['Resultado Geral'] = ''
        linguagens_tabela2['Resultado Individual'] = ''
        for i in range(len(linguagens_tabela2['Assunto'])):
            linguagens_tabela2['Resultado Geral'][i] = "{0:.0%}".format(linguagens_tabela2['Resultado Geral decimal'][i])
            linguagens_tabela2['Resultado Individual'][i] = "{0:.0%}".format(linguagens_tabela2['Resultado Individual decimal'][i])
        linguagens_tabela3 = pd.merge(linguagens_tabela2,linguagens_aluno_media3, on = 'Assunto', how = 'inner')
        linguagens_tabela3.rename(columns = {'Número da questão':'Quantidade de questões'}, inplace = True)
        linguagens_tabela3 = linguagens_tabela3[['Assunto','Quantidade de questões','Resultado Individual', 'Resultado Geral','Resultado Individual decimal', 'Resultado Geral decimal']]
        linguagens_tabela3['Status'] = ''
        for i in range(len(linguagens_tabela3['Assunto'])):
            if linguagens_tabela3['Resultado Individual decimal'][i] == 0:
                linguagens_tabela3['Status'][i] = "🔴" 
            elif linguagens_tabela3['Resultado Individual decimal'][i] >= linguagens_tabela3['Resultado Geral decimal'][i]:
                linguagens_tabela3['Status'][i] = "🟢"
            elif linguagens_tabela3['Resultado Individual decimal'][i] - linguagens_tabela3['Resultado Geral decimal'][i] > - 0.25:
                linguagens_tabela3['Status'][i] = "🟡"
            else:
                linguagens_tabela3['Status'][i] = "🔴"
        linguagens_tabela3['Diferença'] = ''
        for i in range(len(linguagens_tabela3['Assunto'])):
            linguagens_tabela3['Diferença'][i] = linguagens_tabela3['Resultado Individual decimal'][i] - linguagens_tabela3['Resultado Geral decimal'][i]

        linguagens_tabela_ordenado = linguagens_tabela3.sort_values(by = 'Diferença')

        linguagens_tabela_verde = linguagens_tabela_ordenado[linguagens_tabela_ordenado['Status'] == '🟢']
        linguagens_tabela_verde_ordenado = linguagens_tabela_verde.sort_values(by = 'Diferença', ascending = False).reset_index(drop = True)

        linguagens_tabela_vermelho = linguagens_tabela_ordenado[linguagens_tabela_ordenado['Status'] == '🔴']
        linguagens_tabela_vermelho_ordenado = linguagens_tabela_vermelho.sort_values(by = 'Diferença', ascending = True).reset_index(drop = True)

        #st.dataframe(linguagens_tabela_ordenado)
        html_header_lin="""
        <h2 style="font-size:200%; color: #FF00CE; font-family:Georgia"> LINGUAGENS<br>
         <hr style= "  display: block;
          margin-top: 0.5em;
          margin-bottom: 0.5em;
          margin-left: auto;
          margin-right: auto;
          border-style: inset;
          border-width: 1.5px;"></h2>
        """
        st.markdown(html_header_lin, unsafe_allow_html=True)

        ### Block 1#########################################################################################
        with st.container():
            col1, col2, col3, col4, col5, col6, col7 = st.columns([1,20,1,20,1,20,1])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_card_header1_disc, unsafe_allow_html=True)
                fig_c1 = go.Figure(go.Indicator(
                    mode="number+delta",
                    value=round(resultados_linguagens['Nota na questão'][0],1),
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)), 'relative': False},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c1.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                st.plotly_chart(fig_c1)
                st.markdown(html_card_footer1_disc, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_footer1_disc_med_lin, unsafe_allow_html=True)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_card_header2_disc, unsafe_allow_html=True)
                fig_c2 = go.Figure(go.Indicator(
                    mode="number+delta",
                    value=resultados_linguagens['Acerto'][0],
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}, 'valueformat': ',f'},
                    delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais_disciplina_med_lin['Acerto'][0],-1),0))},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c2.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                fig_c2.update_traces(delta_decreasing_color="#FF4136",
                                 delta_increasing_color="#3D9970",
                                 delta_valueformat='f',
                                 selector=dict(type='indicator'))
                st.plotly_chart(fig_c2)
                st.markdown(html_card_footer2_disc, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_footer2_disc_med_lin, unsafe_allow_html=True)
            with col5:
                st.write("")
            with col6:
                st.markdown(html_card_header3_disc, unsafe_allow_html=True)
                fig_c3 = go.Figure(go.Indicator(
                    mode="number",
                    value=classificacao_aluno_lin['index'][0]+1,
                    number={'suffix': "º", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': 1, 'relative': False},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c3.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                fig_c3.update_traces(delta_decreasing_color="#3D9970",
                                     delta_increasing_color="#FF4136",
                                     delta_valueformat='.3f',
                                     selector=dict(type='indicator'))
                st.plotly_chart(fig_c3)
                st.markdown(html_card_footer3_disc_matlin, unsafe_allow_html=True)
            with col7:
                st.write("")
        html_br="""
        <br>
        """
        st.markdown(html_br, unsafe_allow_html=True)

        ponto = str(round(100*(numero_candidatos-(classificacao_aluno_lin['index'][0]))/numero_candidatos,0)).find('.')
        texto = str(round(100*(numero_candidatos-(classificacao_aluno_lin['index'][0]))/numero_candidatos,0))[0:ponto]
        html_card_header_destaques_lin="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 60px; width: 495px;
           height: 150px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Você foi melhor que """+texto+"""% dos alunos!</h5>
          </div>
        </div>
        """  

        st.markdown(html_br, unsafe_allow_html=True)

        with st.container():
            col1, col2, col3, col4, col5 = st.columns([9,25,2,25,4])
            with col1:
                st.write("")
            with col2:
               # create the bins
                counts, bins = np.histogram(resultados_gerais_disciplina3_lin['Nota na questão'], bins=range(0, 1100, 100))
                bins = 0.5 * (bins[:-1] + bins[1:])
                fig = px.bar(x=bins, y=counts, labels={'x':'Nota na questão', 'y':'Número de alunos'})
                fig.update_layout(title={'text': "Distribuição de notas", 'x': 0.5}, paper_bgcolor="#FFF0FC", 
                               plot_bgcolor="#FFF0FC", font={'color': "#C81F6D", 'size': 14, 'family': "Georgia"}, height=400,
                               width=540,
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.01),
                               margin=dict(l=1, r=1, b=1, t=30))
                fig.add_vline(x=int(resultados_linguagens['Nota na questão']), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
                fig.add_vline(x=int(round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
                fig.update_xaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=6, rangemode="tozero",
                              showgrid=False, gridwidth=0.5, gridcolor='#f6f6f6')
                fig.update_yaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=10, rangemode="tozero",
                              showgrid=True, gridwidth=0.5, gridcolor='#f6f6f6')
                fig.update_traces(marker_color='#01e1e1')
                st.plotly_chart(fig)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_header_destaques_lin, unsafe_allow_html=True)
            with col5:
                st.write("")

        html_table_lin=""" 
        <table bordercolor=#FFF0FC>
          <tr style="background-color:#ffd8f8; height: 90px; color:#C81F6D; font-family:Georgia; font-size: 17px; text-align: center">
            <th style="width:350px; bordercolor=#FFF0FC">Assunto</th>
            <th style="width:150px; bordercolor=#FFF0FC">Quantidade de questões</th>
            <th style="width:150px; bordercolor=#FFF0FC">Resultado Individual</th>
            <th style="width:150px; bordercolor=#FFF0FC">Resultado Geral</th>
            <th style="width:150px; bordercolor=#FFF0FC">Status</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][0])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][0])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][0])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][0])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][0])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][1])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][1])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][1])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][1])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][1])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][2])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][2])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][2])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][2])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][2])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][3])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][3])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][3])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][3])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][3])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][4])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][4])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][4])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][4])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][4])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][5])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][5])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][5])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][5])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][5])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][6])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][6])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][6])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][6])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][6])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][7])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][7])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][7])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][7])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][7])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][8])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][8])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][8])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][8])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][8])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][9])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][9])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][9])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][9])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][9])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(linguagens_tabela3['Assunto'][10])+"""</th>
            <th>"""+str(linguagens_tabela3['Quantidade de questões'][10])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Individual'][10])+"""</th>
            <th>"""+str(linguagens_tabela3['Resultado Geral'][10])+"""</th>
            <th>"""+str(linguagens_tabela3['Status'][10])+"""</th>
          </tr>

        </table>
        """

        html_card_header_melhores_resultados_lin="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 30px; width: 495px;
           height: 100px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Seus melhores resultados</h5>
          </div>
        </div>
        """
        if len(linguagens_tabela_verde_ordenado) > 0:
            html_card_header_melhores_resultados1_lin="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(linguagens_tabela_verde_ordenado['Assunto'][0])+"""</p>
              </div>
            </div>
            """
        if len(linguagens_tabela_verde_ordenado) > 1:
            html_card_header_melhores_resultados2_lin="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(linguagens_tabela_verde_ordenado['Assunto'][1])+"""</p>
              </div>
            </div>
            """
        if len(linguagens_tabela_verde_ordenado) > 2:
            html_card_header_melhores_resultados3_lin="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(linguagens_tabela_verde_ordenado['Assunto'][2])+"""</p>
              </div>
            </div>
            """
        html_card_header_pontos_melhorar_lin="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 30px; width: 495px;
           height: 100px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Pontos que você pode melhorar</h5>
          </div>
        </div>
        """
        if len(linguagens_tabela_vermelho_ordenado) > 0:
            html_card_header_pontos_melhorar1_lin="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(linguagens_tabela_vermelho_ordenado['Assunto'][0])+"""</p>
              </div>
            </div>
            """
        if len(linguagens_tabela_vermelho_ordenado) > 1:
            html_card_header_pontos_melhorar2_lin="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(linguagens_tabela_vermelho_ordenado['Assunto'][1])+"""</p>
              </div>
            </div>
            """
        if len(linguagens_tabela_vermelho_ordenado) > 2:
            html_card_header_pontos_melhorar3_lin="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(linguagens_tabela_vermelho_ordenado['Assunto'][2])+"""</p>
              </div>
            </div>
            """
        
        with st.container():
            col1, col2, col3, col4 = st.columns([0.5,12,0.5,10.5])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_table_lin, unsafe_allow_html=True)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_card_header_melhores_resultados_lin, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                if len(linguagens_tabela_verde_ordenado) > 0:
                    st.markdown(html_card_header_melhores_resultados1_lin, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(linguagens_tabela_verde_ordenado) > 1:
                    st.markdown(html_card_header_melhores_resultados2_lin, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(linguagens_tabela_verde_ordenado) > 2:
                    st.markdown(html_card_header_melhores_resultados3_lin, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)

                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_header_pontos_melhorar_lin, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                if len(linguagens_tabela_vermelho_ordenado) > 0:
                    st.markdown(html_card_header_pontos_melhorar1_lin, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(linguagens_tabela_vermelho_ordenado) > 1:
                    st.markdown(html_card_header_pontos_melhorar2_lin, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(linguagens_tabela_vermelho_ordenado) > 2:
                    st.markdown(html_card_header_pontos_melhorar3_lin, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)

        st.markdown(html_br, unsafe_allow_html=True)

        if resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Engenharia' and resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Ciências da Computação':
            ciencias_detalhes = base_alunos_fizeram[base_alunos_fizeram['Disciplina'] == 'Ciências Humanas']
        else:
            ciencias_detalhes = base_alunos_fizeram[base_alunos_fizeram['Disciplina'] == 'Ciências da Natureza']
    
        ciencias_detalhes_media = ciencias_detalhes.groupby('Assunto').mean().reset_index()

        ciencias_aluno = ciencias_detalhes[ciencias_detalhes['Login do aluno(a)'] == login_aluno]

        ciencias_aluno_media = ciencias_aluno.groupby('Assunto').mean().reset_index()
        ciencias_aluno_media2 = ciencias_aluno.groupby('Assunto').count().reset_index()
        ciencias_aluno_media3 = pd.DataFrame()
        ciencias_aluno_media3['Assunto'] = ciencias_aluno_media2['Assunto']
        ciencias_aluno_media3['Número da questão'] = ciencias_aluno_media2['Número da questão']

        ciencias_tabela = pd.merge(ciencias_aluno_media,ciencias_detalhes_media, on = 'Assunto', how = 'inner')
        ciencias_tabela2 = ciencias_tabela.drop(columns = ['Número da questão_x','Número da questão_y','Valor da questão_x','Valor da questão_y','Nota na questão_x','Nota na questão_y','Tempo na questão_x','Tempo na questão_y'])
        ciencias_tabela2.rename(columns = {'Acerto_x':'Resultado Individual decimal','Acerto_y':'Resultado Geral decimal'}, inplace = True)
        ciencias_tabela2['Resultado Geral'] = ''
        ciencias_tabela2['Resultado Individual'] = ''
        for i in range(len(ciencias_tabela2['Assunto'])):
            ciencias_tabela2['Resultado Geral'][i] = "{0:.0%}".format(ciencias_tabela2['Resultado Geral decimal'][i])
            ciencias_tabela2['Resultado Individual'][i] = "{0:.0%}".format(ciencias_tabela2['Resultado Individual decimal'][i])
        ciencias_tabela3 = pd.merge(ciencias_tabela2,ciencias_aluno_media3, on = 'Assunto', how = 'inner')
        ciencias_tabela3.rename(columns = {'Número da questão':'Quantidade de questões'}, inplace = True)
        ciencias_tabela3 = ciencias_tabela3[['Assunto','Quantidade de questões','Resultado Individual', 'Resultado Geral','Resultado Individual decimal', 'Resultado Geral decimal']]
        ciencias_tabela3['Status'] = ''
        for i in range(len(ciencias_tabela3['Assunto'])):
            if ciencias_tabela3['Resultado Individual decimal'][i] == 0:
                ciencias_tabela3['Status'][i] = "🔴" 
            elif ciencias_tabela3['Resultado Individual decimal'][i] >= ciencias_tabela3['Resultado Geral decimal'][i]:
                ciencias_tabela3['Status'][i] = "🟢"
            elif ciencias_tabela3['Resultado Individual decimal'][i] - ciencias_tabela3['Resultado Geral decimal'][i] > - 0.25:
                ciencias_tabela3['Status'][i] = "🟡"
            else:
                ciencias_tabela3['Status'][i] = "🔴"
        ciencias_tabela3['Diferença'] = ''
        for i in range(len(ciencias_tabela3['Assunto'])):
            ciencias_tabela3['Diferença'][i] = ciencias_tabela3['Resultado Individual decimal'][i] - ciencias_tabela3['Resultado Geral decimal'][i]

        ciencias_tabela_ordenado = ciencias_tabela3.sort_values(by = 'Diferença')

        ciencias_tabela_verde = ciencias_tabela_ordenado[ciencias_tabela_ordenado['Status'] == '🟢']
        ciencias_tabela_verde_ordenado = ciencias_tabela_verde.sort_values(by = 'Diferença', ascending = False).reset_index(drop = True)

        ciencias_tabela_vermelho = ciencias_tabela_ordenado[ciencias_tabela_ordenado['Status'] == '🔴']
        ciencias_tabela_vermelho_ordenado = ciencias_tabela_vermelho.sort_values(by = 'Diferença', ascending = True).reset_index(drop = True)

        html_header_hum="""
        <h2 style="font-size:200%; color: #FF00CE; font-family:Georgia"> CIÊNCIAS HUMANAS<br>
         <hr style= "  display: block;
          margin-top: 0.5em;
          margin-bottom: 0.5em;
          margin-left: auto;
          margin-right: auto;
          border-style: inset;
          border-width: 1.5px;"></h2>
        """

        html_header_nat="""
        <h2 style="font-size:200%; color: #FF00CE; font-family:Georgia"> CIÊNCIAS DA NATUREZA<br>
         <hr style= "  display: block;
          margin-top: 0.5em;
          margin-bottom: 0.5em;
          margin-left: auto;
          margin-right: auto;
          border-style: inset;
          border-width: 1.5px;"></h2>
        """
        if len(resultados_ciencias_hum['Disciplina']) == 0:
            st.markdown(html_header_nat, unsafe_allow_html=True)
        else:
            st.markdown(html_header_hum, unsafe_allow_html=True)

        ### Block 1#########################################################################################
        with st.container():
            col1, col2, col3, col4, col5, col6, col7 = st.columns([1,20,1,20,1,20,1])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_card_header1_disc, unsafe_allow_html=True)
                fig_c1 = go.Figure(go.Indicator(
                    mode="number+delta",
                    value=round(resultados_ciencias_fim['Nota na questão'][0],1),
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais_disciplina_med_cie['Nota na questão'][0],-1),0)), 'relative': False},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c1.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                st.plotly_chart(fig_c1)
                st.markdown(html_card_footer1_disc, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_footer1_disc_med_cie, unsafe_allow_html=True)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_card_header2_disc, unsafe_allow_html=True)
                fig_c2 = go.Figure(go.Indicator(
                    mode="number+delta",
                    value=resultados_ciencias_fim['Acerto'][0],
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}, 'valueformat': ',f'},
                    delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais_disciplina_med_cie['Acerto'][0],-1),0))},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c2.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                fig_c2.update_traces(delta_decreasing_color="#FF4136",
                                 delta_increasing_color="#3D9970",
                                 delta_valueformat='f',
                                 selector=dict(type='indicator'))
                st.plotly_chart(fig_c2)
                st.markdown(html_card_footer2_disc, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_footer2_disc_med_cie, unsafe_allow_html=True)
            with col5:
                st.write("")
            with col6:
                st.markdown(html_card_header3_disc, unsafe_allow_html=True)
                fig_c3 = go.Figure(go.Indicator(
                    mode="number",
                    value=classificacao_aluno_fim['index'][0]+1,
                    number={'suffix': "º", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': 1, 'relative': False},
                    domain={'x': [0, 1], 'y': [0, 1]}))
                fig_c3.update_layout(autosize=False,
                                     width=350, height=90, margin=dict(l=20, r=20, b=20, t=50),
                                     paper_bgcolor="#FFF0FC", font={'size': 20})
                fig_c3.update_traces(delta_decreasing_color="#3D9970",
                                     delta_increasing_color="#FF4136",
                                     delta_valueformat='.3f',
                                     selector=dict(type='indicator'))
                st.plotly_chart(fig_c3)
                st.markdown(html_card_footer3_disc, unsafe_allow_html=True)
            with col7:
                st.write("")
        html_br="""
        <br>
        """
        st.markdown(html_br, unsafe_allow_html=True)
        if resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Engenharia' and resultados_gerais_aluno['Turma'][0] != 'Simulado Nacional - Ciências da Computação':
            ponto = str(round(100*((numero_candidatos-numero_eng)-(classificacao_aluno_fim['index'][0]))/(numero_candidatos-numero_eng),0)).find('.')
            texto = str(round(100*((numero_candidatos-numero_eng)-(classificacao_aluno_fim['index'][0]))/(numero_candidatos-numero_eng),0))[0:ponto]
        else:
            ponto = str(round(100*((numero_eng)-(classificacao_aluno_fim['index'][0]))/(numero_eng),0)).find('.')
            texto = str(round(100*((numero_eng)-(classificacao_aluno_fim['index'][0]))/(numero_eng),0))[0:ponto]
       
        html_card_header_destaques_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 60px; width: 495px;
           height: 150px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Você foi melhor que """+texto+"""% dos alunos!</h5>
          </div>
        </div>
        """  

        st.markdown(html_br, unsafe_allow_html=True)

        with st.container():
            col1, col2, col3, col4, col5 = st.columns([9,25,2,25,4])
            with col1:
                st.write("")
            with col2:
               # create the bins
                counts, bins = np.histogram(resultados_gerais_disciplina3_fim['Nota na questão'], bins=range(0, 1100, 100))
                bins = 0.5 * (bins[:-1] + bins[1:])
                fig = px.bar(x=bins, y=counts, labels={'x':'Nota na questão', 'y':'Número de alunos'})
                fig.update_layout(title={'text': "Distribuição de notas", 'x': 0.5}, paper_bgcolor="#FFF0FC", 
                               plot_bgcolor="#FFF0FC", font={'color': "#C81F6D", 'size': 14, 'family': "Georgia"}, height=400,
                               width=540,
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.01),
                               margin=dict(l=1, r=1, b=1, t=30))
                fig.add_vline(x=int(resultados_ciencias_fim['Nota na questão']), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
                fig.add_vline(x=int(round(truncar(resultados_gerais_disciplina_med_cie['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
                fig.update_xaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=6, rangemode="tozero",
                              showgrid=False, gridwidth=0.5, gridcolor='#f6f6f6')
                fig.update_yaxes(showline=True, linewidth=1, linecolor='#f6f6f6', mirror=False, nticks=10, rangemode="tozero",
                              showgrid=True, gridwidth=0.5, gridcolor='#f6f6f6')
                fig.update_traces(marker_color='#01e1e1')
                st.plotly_chart(fig)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_header_destaques_cie, unsafe_allow_html=True)
            with col5:
                st.write("")

        html_table_cie=""" 
        <table bordercolor=#FFF0FC>
          <tr style="background-color:#ffd8f8; height: 90px; color:#C81F6D; font-family:Georgia; font-size: 17px; text-align: center">
            <th style="width:350px; bordercolor=#FFF0FC">Assunto</th>
            <th style="width:150px; bordercolor=#FFF0FC">Quantidade de questões</th>
            <th style="width:150px; bordercolor=#FFF0FC">Resultado Individual</th>
            <th style="width:150px; bordercolor=#FFF0FC">Resultado Geral</th>
            <th style="width:150px; bordercolor=#FFF0FC">Status</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][0])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][0])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][0])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][0])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][0])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][1])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][1])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][1])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][1])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][1])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][2])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][2])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][2])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][2])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][2])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][3])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][3])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][3])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][3])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][3])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][4])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][4])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][4])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][4])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][4])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][5])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][5])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][5])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][5])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][5])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][6])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][6])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][6])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][6])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][6])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][7])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][7])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][7])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][7])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][7])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][8])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][8])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][8])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][8])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][8])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][9])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][9])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][9])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][9])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][9])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][10])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][10])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][10])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][10])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][10])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][11])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][11])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][11])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][11])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][11])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][12])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][12])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][12])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][12])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][12])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][13])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][13])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][13])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][13])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][13])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][14])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][14])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][14])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][14])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][14])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][15])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][15])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][15])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][15])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][15])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][16])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][16])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][16])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][16])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][16])+"""</th>
          </tr>
          <tr style="background-color:#f7d4f0; height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][17])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][17])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][17])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][17])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][17])+"""</th>
          </tr>
          <tr style="height: 42px; color:#C81F6D; font-size: 16px;text-align: center">
            <th>"""+str(ciencias_tabela3['Assunto'][18])+"""</th>
            <th>"""+str(ciencias_tabela3['Quantidade de questões'][18])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Individual'][18])+"""</th>
            <th>"""+str(ciencias_tabela3['Resultado Geral'][18])+"""</th>
            <th>"""+str(ciencias_tabela3['Status'][18])+"""</th>
          </tr>

        </table>
        """

        html_card_header_melhores_resultados_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 30px; width: 495px;
           height: 100px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Seus melhores resultados</h5>
          </div>
        </div>
        """
        if len(ciencias_tabela_verde_ordenado) > 0:
            html_card_header_melhores_resultados1_cie="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(ciencias_tabela_verde_ordenado['Assunto'][0])+"""</p>
              </div>
            </div>
            """
        if len(ciencias_tabela_verde_ordenado) > 1:
            html_card_header_melhores_resultados2_cie="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(ciencias_tabela_verde_ordenado['Assunto'][1])+"""</p>
              </div>
            </div>
            """
        if len(ciencias_tabela_verde_ordenado) > 2:
            html_card_header_melhores_resultados3_cie="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🟢 """+str(ciencias_tabela_verde_ordenado['Assunto'][2])+"""</p>
              </div>
            </div>
            """
        html_card_header_pontos_melhorar_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #ffd8f8; padding-top: 30px; width: 495px;
           height: 100px;">
            <h5 class="card-title" style="background-color:#ffd8f8; color:#C81F6D; font-family:Georgia; text-align: center; padding: 10px 0;">Pontos que você pode melhorar</h5>
          </div>
        </div>
        """
        if len(ciencias_tabela_vermelho_ordenado) > 0:
            html_card_header_pontos_melhorar1_cie="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(ciencias_tabela_vermelho_ordenado['Assunto'][0])+"""</p>
              </div>
            </div>
            """
        if len(ciencias_tabela_vermelho_ordenado) > 1:
            html_card_header_pontos_melhorar2_cie="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(ciencias_tabela_vermelho_ordenado['Assunto'][1])+"""</p>
              </div>
            </div>
            """
        if len(ciencias_tabela_vermelho_ordenado) > 2:
            html_card_header_pontos_melhorar3_cie="""
            <div class="card">
              <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #ffb1b1; padding-top: 12px; width: 495px;
               height: 50px;">
                <p class="card-title" style="background-color:#ffb1b1; color:#a80000; font-size: 20px;  font-family:Georgia; text-align: center; padding: 0px 0;">🔴 """+str(ciencias_tabela_vermelho_ordenado['Assunto'][2])+"""</p>
              </div>
            </div>
            """
        
        with st.container():
            col1, col2, col3, col4 = st.columns([0.5,12,0.5,10.5])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_table_cie, unsafe_allow_html=True)
            with col3:
                st.write("")
            with col4:
                st.markdown(html_card_header_melhores_resultados_cie, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                if len(ciencias_tabela_verde_ordenado) > 0:
                    st.markdown(html_card_header_melhores_resultados1_cie, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(ciencias_tabela_verde_ordenado) > 1:
                    st.markdown(html_card_header_melhores_resultados2_cie, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(ciencias_tabela_verde_ordenado) > 2:
                    st.markdown(html_card_header_melhores_resultados3_cie, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)

                st.markdown(html_br, unsafe_allow_html=True)
                st.markdown(html_card_header_pontos_melhorar_cie, unsafe_allow_html=True)
                st.markdown(html_br, unsafe_allow_html=True)
                if len(ciencias_tabela_vermelho_ordenado) > 0:
                    st.markdown(html_card_header_pontos_melhorar1_cie, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(ciencias_tabela_vermelho_ordenado) > 1:
                    st.markdown(html_card_header_pontos_melhorar2_cie, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)
                if len(ciencias_tabela_vermelho_ordenado) > 2:
                    st.markdown(html_card_header_pontos_melhorar3_cie, unsafe_allow_html=True)
                    st.markdown(html_br, unsafe_allow_html=True)

        st.markdown(html_br, unsafe_allow_html=True)
        st.markdown(html_br, unsafe_allow_html=True)

        html_subtitle="""
        <h2 style="color:#FF00CE; font-family:Georgia;"> DETALHAMENTO POR QUESTÃO
        <hr style= "  display: block;
          margin-top: 0.5em;
          margin-bottom: 0.5em;
          margin-left: auto;
          margin-right: auto;
          border-style: inset;
          border-width: 1.5px;"></h2>
        """
        st.markdown(html_subtitle, unsafe_allow_html=True)
        
        
        tabela_detalhes = base_alunos_fizeram.copy()
        
        for i in range(len(tabela_detalhes['Nome do aluno(a)'])):
            if tabela_detalhes['Resposta do aluno(a)'][i] == 'a':
                tabela_detalhes['Resposta do aluno(a)'][i] = 'A'
            elif tabela_detalhes['Resposta do aluno(a)'][i] == 'b':
                tabela_detalhes['Resposta do aluno(a)'][i] = 'B'
            elif tabela_detalhes['Resposta do aluno(a)'][i] == 'c':
                tabela_detalhes['Resposta do aluno(a)'][i] = 'C'
            elif tabela_detalhes['Resposta do aluno(a)'][i] == 'd':
                tabela_detalhes['Resposta do aluno(a)'][i] = 'D'
            elif tabela_detalhes['Resposta do aluno(a)'][i] == 'e':
                tabela_detalhes['Resposta do aluno(a)'][i] = 'E'
            else:
                tabela_detalhes['Resposta do aluno(a)'][i] = ''

            if tabela_detalhes['Gabarito'][i] == 'a':
                tabela_detalhes['Gabarito'][i] = 'A'
            elif tabela_detalhes['Gabarito'][i] == 'b':
                tabela_detalhes['Gabarito'][i] = 'B'
            elif tabela_detalhes['Gabarito'][i] == 'c':
                tabela_detalhes['Gabarito'][i] = 'C'
            elif tabela_detalhes['Gabarito'][i] == 'd':
                tabela_detalhes['Gabarito'][i] = 'D'
            elif tabela_detalhes['Gabarito'][i] == 'e':
                tabela_detalhes['Gabarito'][i] = 'E'
            else:
                tabela_detalhes['Gabarito'][i] = ''
        
        tabela_detalhes_aluno = tabela_detalhes[tabela_detalhes['Login do aluno(a)'] == login_aluno]
        tabela_detalhes_aluno2 = tabela_detalhes_aluno.drop(columns = ['Nota na questão','Valor da questão','Nome do aluno(a)','Login do aluno(a)','Certo ou errado'])
        tabela_detalhes_media = tabela_detalhes.groupby('Número da questão').mean().reset_index()
        tabela_detalhes_media2 = tabela_detalhes_media.drop(columns = ['Nota na questão','Valor da questão'])

        tabela_detalhes_aluno3 = pd.merge(tabela_detalhes_aluno2, tabela_detalhes_media2, on = 'Número da questão', how = 'inner')
        
        for i in range(len(tabela_detalhes_aluno3['Número da questão'])):
            if tabela_detalhes_aluno3['Número da questão'][i] > 90:
                tabela_detalhes_aluno3['Número da questão'][i] = tabela_detalhes_aluno3['Número da questão'][i] - 30
        
        tabela_detalhes_aluno4 = tabela_detalhes_aluno3.drop(columns = ['Nome da avaliação','Turma'])
        
        cor_back = []
        cor_texto = []
        for i in range(len(tabela_detalhes_aluno4['Número da questão'])):
            minutes, seconds= divmod(tabela_detalhes_aluno4['Tempo na questão_x'][i], 60)
            aux1 = str(round(minutes,0)).find('.')
            texto1 = str(round(minutes,0))[0:aux1]
            aux2 = str(round(seconds,0)).find('.')  
            texto2 = str(round(seconds,0))[0:aux2]  
            tabela_detalhes_aluno4['Tempo na questão_x'][i] = texto1+' min '+texto2+' s' 
            minutes, seconds= divmod(tabela_detalhes_aluno4['Tempo na questão_y'][i], 60)
            aux1 = str(round(minutes,0)).find('.')
            texto1 = str(round(minutes,0))[0:aux1]
            aux2 = str(round(seconds,0)).find('.')  
            texto2 = str(round(seconds,0))[0:aux2]  
            tabela_detalhes_aluno4['Tempo na questão_y'][i] = texto1+' min '+texto2+' s' 
            tabela_detalhes_aluno4['Acerto_x'][i] = "{0:.0%}".format(tabela_detalhes_aluno4['Acerto_x'][i])
            tabela_detalhes_aluno4['Acerto_y'][i] = "{0:.0%}".format(tabela_detalhes_aluno4['Acerto_y'][i])
            if tabela_detalhes_aluno4['Acerto_x'][i] == '100%':
                cor_back.append('#a5ffa5')
                cor_texto.append('#008800')
            else:
                cor_back.append('#ffb1b1')
                cor_texto.append('#a80000')

        tabela_detalhes_aluno4 = tabela_detalhes_aluno4[['Número da questão','Disciplina','Assunto','Resposta do aluno(a)','Gabarito','Acerto_x','Acerto_y','Tempo na questão_x','Tempo na questão_y']]
        tabela_detalhes_aluno4.rename(columns = {'Disciplina':'Área do conhecimento','Acerto_x':'Resultado Individual','Acerto_y':'Resultado Geral','Tempo na questão_x':'Tempo na questão','Tempo na questão_y':'Média geral'}, inplace = True)

        html_table_questoes=""" 
        <table bordercolor=#FFF0FC>
          <tr style="background-color:#ffd8f8; height: 90px; color:#C81F6D; font-family:Georgia; font-size: 17px; text-align: center">
            <th style="width:150px; bordercolor=#FFF0FC">Número da questão</th>
            <th style="width:200px; bordercolor=#FFF0FC">Área do conhecimento</th>
            <th style="width:350px; bordercolor=#FFF0FC">Assunto</th>
            <th style="width:150px; bordercolor=#FFF0FC">Sua resposta</th>
            <th style="width:150px; bordercolor=#FFF0FC">Gabarito</th>
            <th style="width:150px; bordercolor=#FFF0FC">Seu resultado</th>
            <th style="width:200px; bordercolor=#FFF0FC">Porcentagem de acerto geral</th>
            <th style="width:200px; bordercolor=#FFF0FC">Tempo na questão</th>
            <th style="width:200px; bordercolor=#FFF0FC">Tempo médio na questão</th>
          </tr>
          <tr style="background-color:"""+cor_back[0]+"""; height: 42px; color:"""+cor_texto[0]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][0])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][0])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[1]+"""; height: 42px; color:"""+cor_texto[1]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][1])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][1])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[2]+"""; height: 42px; color:"""+cor_texto[2]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][2])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][2])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[3]+"""; height: 42px; color:"""+cor_texto[3]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][3])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][3])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[4]+"""; height: 42px; color:"""+cor_texto[4]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][4])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][4])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[5]+"""; height: 42px; color:"""+cor_texto[5]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][5])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][5])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[6]+"""; height: 42px; color:"""+cor_texto[6]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][6])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][6])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[7]+"""; height: 42px; color:"""+cor_texto[7]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][7])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[8]+"""; height: 42px; color:"""+cor_texto[8]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][8])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[9]+"""; height: 42px; color:"""+cor_texto[9]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][9])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][9])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[10]+"""; height: 42px; color:"""+cor_texto[10]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][10])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][10])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[11]+"""; height: 42px; color:"""+cor_texto[11]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][11])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][11])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[12]+"""; height: 42px; color:"""+cor_texto[12]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][12])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][12])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[13]+"""; height: 42px; color:"""+cor_texto[13]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][13])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][13])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[14]+"""; height: 42px; color:"""+cor_texto[14]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][14])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][14])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[15]+"""; height: 42px; color:"""+cor_texto[15]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][15])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][15])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[16]+"""; height: 42px; color:"""+cor_texto[16]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][16])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][16])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[17]+"""; height: 42px; color:"""+cor_texto[17]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][17])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][17])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[18]+"""; height: 42px; color:"""+cor_texto[18]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][18])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][18])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[19]+"""; height: 42px; color:"""+cor_texto[19]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][19])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][19])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[20]+"""; height: 42px; color:"""+cor_texto[20]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][20])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][20])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[21]+"""; height: 42px; color:"""+cor_texto[21]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][21])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][21])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[22]+"""; height: 42px; color:"""+cor_texto[22]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][22])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][22])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[23]+"""; height: 42px; color:"""+cor_texto[23]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][23])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][23])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[24]+"""; height: 42px; color:"""+cor_texto[24]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][24])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][24])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[25]+"""; height: 42px; color:"""+cor_texto[25]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][25])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][25])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[26]+"""; height: 42px; color:"""+cor_texto[26]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][26])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][26])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[27]+"""; height: 42px; color:"""+cor_texto[27]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][27])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][27])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[28]+"""; height: 42px; color:"""+cor_texto[28]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][28])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][28])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[29]+"""; height: 42px; color:"""+cor_texto[29]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][29])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][29])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[30]+"""; height: 42px; color:"""+cor_texto[30]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][30])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][30])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[31]+"""; height: 42px; color:"""+cor_texto[31]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][31])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][31])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[32]+"""; height: 42px; color:"""+cor_texto[32]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][32])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][32])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[33]+"""; height: 42px; color:"""+cor_texto[33]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][33])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][33])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[34]+"""; height: 42px; color:"""+cor_texto[34]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][34])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][34])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[35]+"""; height: 42px; color:"""+cor_texto[35]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][35])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][35])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[36]+"""; height: 42px; color:"""+cor_texto[36]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][36])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][36])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[37]+"""; height: 42px; color:"""+cor_texto[37]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][37])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][37])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[38]+"""; height: 42px; color:"""+cor_texto[38]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][38])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][38])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[39]+"""; height: 42px; color:"""+cor_texto[39]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][39])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][39])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[40]+"""; height: 42px; color:"""+cor_texto[40]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][40])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][40])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[41]+"""; height: 42px; color:"""+cor_texto[41]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][41])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][41])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[42]+"""; height: 42px; color:"""+cor_texto[42]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][42])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][42])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[43]+"""; height: 42px; color:"""+cor_texto[43]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][43])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][43])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[44]+"""; height: 42px; color:"""+cor_texto[44]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][44])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][44])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[45]+"""; height: 42px; color:"""+cor_texto[45]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][45])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][45])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[46]+"""; height: 42px; color:"""+cor_texto[46]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][46])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][46])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[47]+"""; height: 42px; color:"""+cor_texto[47]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][47])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][47])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[48]+"""; height: 42px; color:"""+cor_texto[48]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][48])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][48])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[49]+"""; height: 42px; color:"""+cor_texto[49]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][49])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][49])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[50]+"""; height: 42px; color:"""+cor_texto[50]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][50])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][50])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[51]+"""; height: 42px; color:"""+cor_texto[51]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][51])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][51])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[52]+"""; height: 42px; color:"""+cor_texto[52]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][52])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][52])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[53]+"""; height: 42px; color:"""+cor_texto[53]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][53])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][53])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[54]+"""; height: 42px; color:"""+cor_texto[54]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][54])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][54])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[55]+"""; height: 42px; color:"""+cor_texto[55]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][55])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][55])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[56]+"""; height: 42px; color:"""+cor_texto[56]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][56])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][56])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[57]+"""; height: 42px; color:"""+cor_texto[57]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][57])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][57])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[58]+"""; height: 42px; color:"""+cor_texto[58]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][58])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][58])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[59]+"""; height: 42px; color:"""+cor_texto[59]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][59])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][59])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[60]+"""; height: 42px; color:"""+cor_texto[60]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][60])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][60])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[61]+"""; height: 42px; color:"""+cor_texto[61]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][61])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][61])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[62]+"""; height: 42px; color:"""+cor_texto[62]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][62])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][62])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[63]+"""; height: 42px; color:"""+cor_texto[63]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][63])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][63])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[64]+"""; height: 42px; color:"""+cor_texto[64]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][64])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][64])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[65]+"""; height: 42px; color:"""+cor_texto[65]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][65])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][65])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[66]+"""; height: 42px; color:"""+cor_texto[66]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][66])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][66])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[67]+"""; height: 42px; color:"""+cor_texto[67]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][67])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][67])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[68]+"""; height: 42px; color:"""+cor_texto[68]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][8])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][68])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][68])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[69]+"""; height: 42px; color:"""+cor_texto[69]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][69])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][69])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[70]+"""; height: 42px; color:"""+cor_texto[70]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][70])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][70])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[71]+"""; height: 42px; color:"""+cor_texto[71]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][71])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][71])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[72]+"""; height: 42px; color:"""+cor_texto[72]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][72])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][72])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[73]+"""; height: 42px; color:"""+cor_texto[73]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][73])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][73])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[74]+"""; height: 42px; color:"""+cor_texto[74]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][74])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][74])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[75]+"""; height: 42px; color:"""+cor_texto[75]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][75])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][75])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[76]+"""; height: 42px; color:"""+cor_texto[76]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][76])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][76])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[77]+"""; height: 42px; color:"""+cor_texto[77]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][7])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][77])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][77])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[78]+"""; height: 42px; color:"""+cor_texto[78]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][78])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][78])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[79]+"""; height: 42px; color:"""+cor_texto[79]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][79])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][79])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[80]+"""; height: 42px; color:"""+cor_texto[80]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][80])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][80])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[81]+"""; height: 42px; color:"""+cor_texto[81]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][81])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][81])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[82]+"""; height: 42px; color:"""+cor_texto[82]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][82])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][82])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[83]+"""; height: 42px; color:"""+cor_texto[83]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][83])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][83])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[84]+"""; height: 42px; color:"""+cor_texto[84]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][84])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][84])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[85]+"""; height: 42px; color:"""+cor_texto[85]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][85])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][85])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[86]+"""; height: 42px; color:"""+cor_texto[86]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][86])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][86])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[87]+"""; height: 42px; color:"""+cor_texto[87]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][87])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][87])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[88]+"""; height: 42px; color:"""+cor_texto[88]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][88])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][88])+"""</th>
          </tr>
          <tr style="background-color:"""+cor_back[89]+"""; height: 42px; color:"""+cor_texto[89]+"""; font-size: 16px;text-align: center">
            <th>"""+str(tabela_detalhes_aluno4['Número da questão'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Área do conhecimento'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Assunto'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resposta do aluno(a)'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Gabarito'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Individual'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Resultado Geral'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Tempo na questão'][89])+"""</th>
            <th>"""+str(tabela_detalhes_aluno4['Média geral'][89])+"""</th>
          </tr>
          
          

        </table>
        """

        with st.container():
            col1, col2, col3 = st.columns([1, 20, 1])
            with col1:
                st.write("")
            with col2:
                st.markdown(html_table_questoes, unsafe_allow_html=True)
            with col3:
                st.write("")
        