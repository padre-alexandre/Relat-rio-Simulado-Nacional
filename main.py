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

    resultados_gerais4 = resultados_gerais3[resultados_gerais3['Nota na questão'] > 0]
    resultados_gerais5 = resultados_gerais4.groupby('Nome da avaliação').mean().reset_index()
    
    alunos_fizeram = pd.DataFrame()
    alunos_fizeram['Nome do aluno(a)'] = resultados_gerais4['Nome do aluno(a)']

    ### Resultados gerais do aluno

    numero_candidatos = len(resultados_gerais4['Nome do aluno(a)'])
    aux = resultados_gerais4[resultados_gerais4['Turma'] == 'Engenharias']
    numero_eng = len(aux['Nome do aluno(a)'])

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
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Média Geral: """+str(int(round(truncar(resultados_gerais5['Acerto'][0],-1),0)))+"""</p>
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
                delta={'position': "bottom", 'reference': int(round(truncar(resultados_gerais5['Acerto'][0],-1),0))},
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

    ponto = str(round(100*(numero_candidatos-resultados_gerais_aluno['Classificação'][0])/numero_candidatos,0)).find('.')
    texto = str(round(100*(numero_candidatos-resultados_gerais_aluno['Classificação'][0])/numero_candidatos,0))[0:ponto]
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
        col1, col2, col3, col4, col5 = st.columns([4,25,7,25,4])
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
    
    resultados_disciplina_aluno = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Nome do aluno(a)'] == nome_aluno3].reset_index()
    resultados_disciplina_aluno2 = resultados_disciplina_aluno.sort_values(by = 'Disciplina', ascending = False)
    
    resultados_matematica = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Matemática'].reset_index()
    resultados_linguagens = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Linguagens'].reset_index()
    resultados_ciencias_hum = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Ciências Humanas'].reset_index()
    resultados_ciencias_nat = resultados_disciplina_aluno2[resultados_disciplina_aluno2['Disciplina'] == 'Ciências da Natureza'].reset_index()

    resultados_gerais_disciplina3_mat = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Matemática'].reset_index(drop = True).reset_index()
    resultados_gerais_disciplina3_lin = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Linguagens'].reset_index(drop = True).reset_index()
    resultados_gerais_disciplina3_hum = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Ciências Humanas'].reset_index(drop = True).reset_index()
    resultados_gerais_disciplina3_nat = resultados_gerais_disciplina3[resultados_gerais_disciplina3['Disciplina'] == 'Ciências da Natureza'].reset_index(drop = True).reset_index()
               
    classificacao_aluno_mat = resultados_gerais_disciplina3_mat[resultados_gerais_disciplina3_mat['Nome do aluno(a)'] == nome_aluno3].reset_index()
    classificacao_aluno_lin = resultados_gerais_disciplina3_lin[resultados_gerais_disciplina3_lin['Nome do aluno(a)'] == nome_aluno3].reset_index()
    classificacao_aluno_hum = resultados_gerais_disciplina3_hum[resultados_gerais_disciplina3_hum['Nome do aluno(a)'] == nome_aluno3].reset_index()
    classificacao_aluno_nat = resultados_gerais_disciplina3_nat[resultados_gerais_disciplina3_nat['Nome do aluno(a)'] == nome_aluno3].reset_index()  

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
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(2*round(truncar(resultados_gerais_disciplina_med_mat['Nota na questão'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    html_card_footer1_disc_med_lin="""
    <div class="card">
      <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
       height: 50px;">
        <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(4*round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)))+"""</p>
      </div>
    </div>
    """
    if len(resultados_ciencias_hum['Nota na questão'] == 0):
        html_card_footer1_disc_med_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(4*round(truncar(resultados_gerais_disciplina_med_hum['Nota na questão'][0],-1),0)))+"""</p>
          </div>
        </div>
        """
    else:
        html_card_footer1_disc_med_cie="""
        <div class="card">
          <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #c5ffff; padding-top: 12px; width: 350px;
           height: 50px;">
            <p class="card-title" style="background-color:#c5ffff; color:#008181; font-family:Georgia; text-align: center; padding: 0px 0;">Media Geral: """+str(int(4*round(truncar(resultados_gerais_disciplina_med_nat['Nota na questão'][0],-1),0)))+"""</p>
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
    if resultados_gerais_aluno['Turma'][0] != 'Engenharias':
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
    if resultados_gerais_aluno['Turma'][0] != 'Engenharias':
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
                    value=round(2*resultados_matematica['Nota na questão'][0],1),
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': int(2*round(truncar(resultados_gerais_disciplina_med_mat['Nota na questão'][0],-1),0)), 'relative': False},
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
        ponto = str(round(100*(numero_candidatos-(classificacao_aluno_mat['index'][0]+1))/numero_candidatos,0)).find('.')
        texto = str(round(100*(numero_candidatos-(classificacao_aluno_mat['index'][0]+1))/numero_candidatos,0))[0:ponto]
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
            col1, col2, col3, col4, col5 = st.columns([4,25,7,25,4])
            with col1:
                st.write("")
            with col2:
               # create the bins
                counts, bins = np.histogram(2*resultados_gerais_disciplina3_mat['Nota na questão'], bins=range(0, 1100, 100))
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
                fig.add_vline(x=int(2*resultados_matematica['Nota na questão']), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
                fig.add_vline(x=int(2*round(truncar(resultados_gerais_disciplina_med_mat['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
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
                    value=round(4*resultados_linguagens['Nota na questão'][0],1),
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': int(4*round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)), 'relative': False},
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

        ponto = str(round(100*(numero_candidatos-(classificacao_aluno_lin['index'][0]+1))/numero_candidatos,0)).find('.')
        texto = str(round(100*(numero_candidatos-(classificacao_aluno_lin['index'][0]+1))/numero_candidatos,0))[0:ponto]
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
            col1, col2, col3, col4, col5 = st.columns([4,25,7,25,4])
            with col1:
                st.write("")
            with col2:
               # create the bins
                counts, bins = np.histogram(4*resultados_gerais_disciplina3_lin['Nota na questão'], bins=range(0, 1100, 100))
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
                fig.add_vline(x=int(4*resultados_linguagens['Nota na questão']), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
                fig.add_vline(x=int(4*round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
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
                    value=round(4*resultados_ciencias_fim['Nota na questão'][0],1),
                    number={'suffix': "", "font": {"size": 40, 'color': "#C81F6D", 'family': "Arial"}},
                    delta={'position': "bottom", 'reference': int(4*round(truncar(resultados_gerais_disciplina_med_cie['Nota na questão'][0],-1),0)), 'relative': False},
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
        if resultados_gerais_aluno['Turma'][0] != 'Engenharias':
            ponto = str(round(100*((numero_candidatos-numero_eng)-(classificacao_aluno_fim['index'][0]+1))/(numero_candidatos-numero_eng),0)).find('.')
            texto = str(round(100*((numero_candidatos-numero_eng)-(classificacao_aluno_fim['index'][0]+1))/(numero_candidatos-numero_eng),0))[0:ponto]
        else:
            ponto = str(round(100*((numero_eng)-(classificacao_aluno_fim['index'][0]+1))/(numero_eng),0)).find('.')
            texto = str(round(100*((numero_eng)-(classificacao_aluno_fim['index'][0]+1))/(numero_eng),0))[0:ponto]
      
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
            col1, col2, col3, col4, col5 = st.columns([4,25,7,25,4])
            with col1:
                st.write("")
            with col2:
               # create the bins
                counts, bins = np.histogram(4*resultados_gerais_disciplina3_lin['Nota na questão'], bins=range(0, 1100, 100))
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
                fig.add_vline(x=int(4*resultados_linguagens['Nota na questão']), line_width=7, line_dash="dash", line_color="#FF00CE", annotation_text="Você está aqui!", annotation_position="top right")
                fig.add_vline(x=int(4*round(truncar(resultados_gerais_disciplina_med_lin['Nota na questão'][0],-1),0)), line_width=7, line_dash="dash", line_color="#fedc00", annotation_text="Média", annotation_position="top right")
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