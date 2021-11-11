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
from load_css import local_css
from datetime import datetime


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

######################### Banco de Dados ########################
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#sheet = client.open('Banco de Dados - Relatório Simulado Nacional').sheet1          # Enquanto estiver rodando na nuvem
sheet = client.open('Banco de Dados - Relatório Simulado Nacional - Teste').sheet1   # Enquanto estiver rodando no local

#### Colunas (id, Data e Hora, Nome, Rede, Grupo, Gestor, Produto, Faixa de licenças, Namespace, NPS, Feedback)
row0 = ['Data e Hora', 'Turma','Nome','Login']

banco_de_dados = sheet.get_all_records()
banco_de_dados2 = pd.DataFrame(banco_de_dados)

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

html_card_instagram="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 280px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Instagram: @jazz_vestibular</p>
      </div>
    </div>
    """
html_card_whatsapp="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #a5ffa5; padding-top: 12px; width: 280px;
       height: 50px;">
        <p class="card-title" style="background-color:#a5ffa5; color:#008800; font-size:16px; font-family:Georgia; text-align: center; padding: 0px 0;">Whatsapp: (11) 93046-8509</p>
      </div>
    </div>
    """
html_br="""
    <br>
    """

with st.container():
        col1, col2, col3 = st.columns([10, 5, 5])
        with col1:
            st.image('[LOGO] Jazz.png')
        with col2:
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_card_instagram, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.write("##### [Clique aqui para conhecer nossa página](https://www.instagram.com/jazz_vestibular/)")
        with col3:
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.markdown(html_card_whatsapp, unsafe_allow_html=True)
            st.markdown(html_br, unsafe_allow_html=True)
            st.write("##### [Clique aqui para falar conosco](https://api.whatsapp.com/send?phone=55011930468509)")

st.markdown(html_br, unsafe_allow_html=True)
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

if len(login_aluno) > 0:
    nome_aluno3 = resultados_gerais3[resultados_gerais3['Login do aluno(a)'] == login_aluno]['Nome do aluno(a)'].reset_index()
    turma_aluno = resultados_gerais3[resultados_gerais3['Login do aluno(a)'] == login_aluno]['Turma'].reset_index() 
    row = [str(datetime.today()),turma_aluno['Turma'][0],nome_aluno3['Nome do aluno(a)'][0],login_aluno]
    index = 2
    sheet.insert_row(row, index)


    html_br="""
    <br>
    """
    html_download_pdfs="""
    <h2 style="font-size:200%; color: #FF00CE; font-family:Georgia">PDFs DO SIMULADO<br>
     <hr style= "  display: block;
      margin-top: 0.5em;
      margin-bottom: 0.5em;
      margin-left: auto;
      margin-right: auto;
      border-style: inset;
      border-width: 1.5px;"></h2>
    """
    st.markdown(html_download_pdfs, unsafe_allow_html=True)
    st.markdown(get_binary_file_downloader_html('Simulado Nacional Insper 1º fase - Matemática e Linguagens.pdf', 'Simulado de Matemática e Linguagens'), unsafe_allow_html=True)
    if turma_aluno['Turma'][0] == 'Simulado Nacional - Engenharia' or turma_aluno['Turma'][0] == 'Simulado Nacional - Ciências da Computação':
        st.markdown(get_binary_file_downloader_html('Simulado Nacional Insper 1º fase - Ciências da Natureza.pdf', 'Simulado de Ciências da Natureza'), unsafe_allow_html=True)
    else:
        st.markdown(get_binary_file_downloader_html('Simulado Nacional Insper 1º fase - Ciências Humanas.pdf', 'Simulado de Ciências Humanas'), unsafe_allow_html=True)
    html_br="""
    <br>
    """
    st.markdown(html_br, unsafe_allow_html=True)
if login_aluno != '':
    resultados_gerais3.to_csv('Resultado.csv')
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
            fig = px.bar(x=bins, y=counts, labels={'x':'Nota no simulado', 'y':'Número de alunos'})
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
                fig = px.bar(x=bins, y=counts, labels={'x':'Nota no simulado', 'y':'Número de alunos'})
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
                fig = px.bar(x=bins, y=counts, labels={'x':'Nota no simulado', 'y':'Número de alunos'})
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
                fig = px.bar(x=bins, y=counts, labels={'x':'Nota no simulado', 'y':'Número de alunos'})
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

        tabela_final = tabela_questoes(tabela_detalhes_aluno4,'Número da questão','Área do conhecimento','Assunto','Resposta do aluno(a)','Gabarito','Resultado Individual','Resultado Geral','Tempo na questão','Média geral',cor_texto,cor_back)
        with st.container():
            col1, col2, col3 = st.columns([0.5, 20, 0.5])
            with col1:
                st.write("")
            with col2:
                st.markdown(tabela_final, unsafe_allow_html=True)
            with col3:
                st.write("")