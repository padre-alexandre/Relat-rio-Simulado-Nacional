import pandas as pd

def inserir_linha(df, linha):
    df = df.append(linha, ignore_index=False)
    df = df.sort_index().reset_index(drop=True)
    return df

def classificacao_cor(value):
    if value >= 15:
        color = '#199a22'
    elif value >= 10:
        color = '#be9815'
    elif value >= 5:
        color = '#c17611'
    else:
        color = '#910a08'
    return 'color: %s' % color

def truncar(num, digits):
    sp = str(num).split('.')
    return float(str(sp[0])+'.'+str(sp[1][0:digits]))

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

import os
import base64
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Clique aqui para baixar o {file_label}</a>'
    return href

def tabela_questoes(dataframe,coluna1,coluna2,coluna3,coluna4,coluna5,coluna6,coluna7,coluna8,coluna9,cor_texto,cor_back):
    html_table_questoes=""" 
    <table bordercolor=#FFF0FC>
      <tr style="background-color:#ffd8f8; height: 90px; color:#C81F6D; font-family:Georgia; font-size: 17px; text-align: center">
        <th style="width:100px; bordercolor=#FFF0FC">Número da questão</th>
        <th style="width:200px; bordercolor=#FFF0FC">Área do conhecimento</th>
        <th style="width:350px; bordercolor=#FFF0FC">Assunto</th>
        <th style="width:100px; bordercolor=#FFF0FC">Sua resposta</th>
        <th style="width:100px; bordercolor=#FFF0FC">Gabarito</th>
        <th style="width:100px; bordercolor=#FFF0FC">Seu resultado</th>
        <th style="width:100px; bordercolor=#FFF0FC">Porcentagem de acerto geral</th>
        <th style="width:100px; bordercolor=#FFF0FC">Tempo na questão</th>
        <th style="width:100px; bordercolor=#FFF0FC">Tempo médio na questão</th>
      </tr>
      <tr style="background-color:"""+cor_back[0]+"""; height: 42px; color:"""+cor_texto[0]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][0])+"""</th>
        <th>"""+str(dataframe[coluna2][0])+"""</th>
        <th>"""+str(dataframe[coluna3][0])+"""</th>
        <th>"""+str(dataframe[coluna4][0])+"""</th>
        <th>"""+str(dataframe[coluna5][0])+"""</th>
        <th>"""+str(dataframe[coluna6][0])+"""</th>
        <th>"""+str(dataframe[coluna7][0])+"""</th>
        <th>"""+str(dataframe[coluna8][0])+"""</th>
        <th>"""+str(dataframe[coluna9][0])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[1]+"""; height: 42px; color:"""+cor_texto[1]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][1])+"""</th>
        <th>"""+str(dataframe[coluna2][1])+"""</th>
        <th>"""+str(dataframe[coluna3][1])+"""</th>
        <th>"""+str(dataframe[coluna4][1])+"""</th>
        <th>"""+str(dataframe[coluna5][1])+"""</th>
        <th>"""+str(dataframe[coluna6][1])+"""</th>
        <th>"""+str(dataframe[coluna7][1])+"""</th>
        <th>"""+str(dataframe[coluna8][1])+"""</th>
        <th>"""+str(dataframe[coluna9][1])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[2]+"""; height: 42px; color:"""+cor_texto[2]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][2])+"""</th>
        <th>"""+str(dataframe[coluna2][2])+"""</th>
        <th>"""+str(dataframe[coluna3][2])+"""</th>
        <th>"""+str(dataframe[coluna4][2])+"""</th>
        <th>"""+str(dataframe[coluna5][2])+"""</th>
        <th>"""+str(dataframe[coluna6][2])+"""</th>
        <th>"""+str(dataframe[coluna7][2])+"""</th>
        <th>"""+str(dataframe[coluna8][2])+"""</th>
        <th>"""+str(dataframe[coluna9][2])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[3]+"""; height: 42px; color:"""+cor_texto[3]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][3])+"""</th>
        <th>"""+str(dataframe[coluna2][3])+"""</th>
        <th>"""+str(dataframe[coluna3][3])+"""</th>
        <th>"""+str(dataframe[coluna4][3])+"""</th>
        <th>"""+str(dataframe[coluna5][3])+"""</th>
        <th>"""+str(dataframe[coluna6][3])+"""</th>
        <th>"""+str(dataframe[coluna7][3])+"""</th>
        <th>"""+str(dataframe[coluna8][3])+"""</th>
        <th>"""+str(dataframe[coluna9][3])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[4]+"""; height: 42px; color:"""+cor_texto[4]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][4])+"""</th>
        <th>"""+str(dataframe[coluna2][4])+"""</th>
        <th>"""+str(dataframe[coluna3][4])+"""</th>
        <th>"""+str(dataframe[coluna4][4])+"""</th>
        <th>"""+str(dataframe[coluna5][4])+"""</th>
        <th>"""+str(dataframe[coluna6][4])+"""</th>
        <th>"""+str(dataframe[coluna7][4])+"""</th>
        <th>"""+str(dataframe[coluna8][4])+"""</th>
        <th>"""+str(dataframe[coluna9][4])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[5]+"""; height: 42px; color:"""+cor_texto[5]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][5])+"""</th>
        <th>"""+str(dataframe[coluna2][5])+"""</th>
        <th>"""+str(dataframe[coluna3][5])+"""</th>
        <th>"""+str(dataframe[coluna4][5])+"""</th>
        <th>"""+str(dataframe[coluna5][5])+"""</th>
        <th>"""+str(dataframe[coluna6][5])+"""</th>
        <th>"""+str(dataframe[coluna7][5])+"""</th>
        <th>"""+str(dataframe[coluna8][5])+"""</th>
        <th>"""+str(dataframe[coluna9][5])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[6]+"""; height: 42px; color:"""+cor_texto[6]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][6])+"""</th>
        <th>"""+str(dataframe[coluna2][6])+"""</th>
        <th>"""+str(dataframe[coluna3][6])+"""</th>
        <th>"""+str(dataframe[coluna4][6])+"""</th>
        <th>"""+str(dataframe[coluna5][6])+"""</th>
        <th>"""+str(dataframe[coluna6][6])+"""</th>
        <th>"""+str(dataframe[coluna7][6])+"""</th>
        <th>"""+str(dataframe[coluna8][6])+"""</th>
        <th>"""+str(dataframe[coluna9][6])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[7]+"""; height: 42px; color:"""+cor_texto[7]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][7])+"""</th>
        <th>"""+str(dataframe[coluna2][7])+"""</th>
        <th>"""+str(dataframe[coluna3][7])+"""</th>
        <th>"""+str(dataframe[coluna4][7])+"""</th>
        <th>"""+str(dataframe[coluna5][7])+"""</th>
        <th>"""+str(dataframe[coluna6][7])+"""</th>
        <th>"""+str(dataframe[coluna7][7])+"""</th>
        <th>"""+str(dataframe[coluna8][7])+"""</th>
        <th>"""+str(dataframe[coluna9][7])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[8]+"""; height: 42px; color:"""+cor_texto[8]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][8])+"""</th>
        <th>"""+str(dataframe[coluna2][8])+"""</th>
        <th>"""+str(dataframe[coluna3][8])+"""</th>
        <th>"""+str(dataframe[coluna4][8])+"""</th>
        <th>"""+str(dataframe[coluna5][8])+"""</th>
        <th>"""+str(dataframe[coluna6][8])+"""</th>
        <th>"""+str(dataframe[coluna7][8])+"""</th>
        <th>"""+str(dataframe[coluna8][8])+"""</th>
        <th>"""+str(dataframe[coluna9][8])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[9]+"""; height: 42px; color:"""+cor_texto[9]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][9])+"""</th>
        <th>"""+str(dataframe[coluna2][9])+"""</th>
        <th>"""+str(dataframe[coluna3][9])+"""</th>
        <th>"""+str(dataframe[coluna4][9])+"""</th>
        <th>"""+str(dataframe[coluna5][9])+"""</th>
        <th>"""+str(dataframe[coluna6][9])+"""</th>
        <th>"""+str(dataframe[coluna7][9])+"""</th>
        <th>"""+str(dataframe[coluna8][9])+"""</th>
        <th>"""+str(dataframe[coluna9][9])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[10]+"""; height: 42px; color:"""+cor_texto[10]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][10])+"""</th>
        <th>"""+str(dataframe[coluna2][10])+"""</th>
        <th>"""+str(dataframe[coluna3][10])+"""</th>
        <th>"""+str(dataframe[coluna4][10])+"""</th>
        <th>"""+str(dataframe[coluna5][10])+"""</th>
        <th>"""+str(dataframe[coluna6][10])+"""</th>
        <th>"""+str(dataframe[coluna7][10])+"""</th>
        <th>"""+str(dataframe[coluna8][10])+"""</th>
        <th>"""+str(dataframe[coluna9][10])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[11]+"""; height: 42px; color:"""+cor_texto[11]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][11])+"""</th>
        <th>"""+str(dataframe[coluna2][11])+"""</th>
        <th>"""+str(dataframe[coluna3][11])+"""</th>
        <th>"""+str(dataframe[coluna4][11])+"""</th>
        <th>"""+str(dataframe[coluna5][11])+"""</th>
        <th>"""+str(dataframe[coluna6][11])+"""</th>
        <th>"""+str(dataframe[coluna7][11])+"""</th>
        <th>"""+str(dataframe[coluna8][11])+"""</th>
        <th>"""+str(dataframe[coluna9][11])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[12]+"""; height: 42px; color:"""+cor_texto[12]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][12])+"""</th>
        <th>"""+str(dataframe[coluna2][12])+"""</th>
        <th>"""+str(dataframe[coluna3][12])+"""</th>
        <th>"""+str(dataframe[coluna4][12])+"""</th>
        <th>"""+str(dataframe[coluna5][12])+"""</th>
        <th>"""+str(dataframe[coluna6][12])+"""</th>
        <th>"""+str(dataframe[coluna7][12])+"""</th>
        <th>"""+str(dataframe[coluna8][12])+"""</th>
        <th>"""+str(dataframe[coluna9][12])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[13]+"""; height: 42px; color:"""+cor_texto[13]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][13])+"""</th>
        <th>"""+str(dataframe[coluna2][13])+"""</th>
        <th>"""+str(dataframe[coluna3][13])+"""</th>
        <th>"""+str(dataframe[coluna4][13])+"""</th>
        <th>"""+str(dataframe[coluna5][13])+"""</th>
        <th>"""+str(dataframe[coluna6][13])+"""</th>
        <th>"""+str(dataframe[coluna7][13])+"""</th>
        <th>"""+str(dataframe[coluna8][13])+"""</th>
        <th>"""+str(dataframe[coluna9][13])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[14]+"""; height: 42px; color:"""+cor_texto[14]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][14])+"""</th>
        <th>"""+str(dataframe[coluna2][14])+"""</th>
        <th>"""+str(dataframe[coluna3][14])+"""</th>
        <th>"""+str(dataframe[coluna4][14])+"""</th>
        <th>"""+str(dataframe[coluna5][14])+"""</th>
        <th>"""+str(dataframe[coluna6][14])+"""</th>
        <th>"""+str(dataframe[coluna7][14])+"""</th>
        <th>"""+str(dataframe[coluna8][14])+"""</th>
        <th>"""+str(dataframe[coluna9][14])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[15]+"""; height: 42px; color:"""+cor_texto[15]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][15])+"""</th>
        <th>"""+str(dataframe[coluna2][15])+"""</th>
        <th>"""+str(dataframe[coluna3][15])+"""</th>
        <th>"""+str(dataframe[coluna4][15])+"""</th>
        <th>"""+str(dataframe[coluna5][15])+"""</th>
        <th>"""+str(dataframe[coluna6][15])+"""</th>
        <th>"""+str(dataframe[coluna7][15])+"""</th>
        <th>"""+str(dataframe[coluna8][15])+"""</th>
        <th>"""+str(dataframe[coluna9][15])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[16]+"""; height: 42px; color:"""+cor_texto[16]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][16])+"""</th>
        <th>"""+str(dataframe[coluna2][16])+"""</th>
        <th>"""+str(dataframe[coluna3][16])+"""</th>
        <th>"""+str(dataframe[coluna4][16])+"""</th>
        <th>"""+str(dataframe[coluna5][16])+"""</th>
        <th>"""+str(dataframe[coluna6][16])+"""</th>
        <th>"""+str(dataframe[coluna7][16])+"""</th>
        <th>"""+str(dataframe[coluna8][16])+"""</th>
        <th>"""+str(dataframe[coluna9][16])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[17]+"""; height: 42px; color:"""+cor_texto[17]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][17])+"""</th>
        <th>"""+str(dataframe[coluna2][17])+"""</th>
        <th>"""+str(dataframe[coluna3][17])+"""</th>
        <th>"""+str(dataframe[coluna4][17])+"""</th>
        <th>"""+str(dataframe[coluna5][17])+"""</th>
        <th>"""+str(dataframe[coluna6][17])+"""</th>
        <th>"""+str(dataframe[coluna7][17])+"""</th>
        <th>"""+str(dataframe[coluna8][17])+"""</th>
        <th>"""+str(dataframe[coluna9][17])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[18]+"""; height: 42px; color:"""+cor_texto[18]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][18])+"""</th>
        <th>"""+str(dataframe[coluna2][18])+"""</th>
        <th>"""+str(dataframe[coluna3][18])+"""</th>
        <th>"""+str(dataframe[coluna4][18])+"""</th>
        <th>"""+str(dataframe[coluna5][18])+"""</th>
        <th>"""+str(dataframe[coluna6][18])+"""</th>
        <th>"""+str(dataframe[coluna7][18])+"""</th>
        <th>"""+str(dataframe[coluna8][18])+"""</th>
        <th>"""+str(dataframe[coluna9][18])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[19]+"""; height: 42px; color:"""+cor_texto[19]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][19])+"""</th>
        <th>"""+str(dataframe[coluna2][19])+"""</th>
        <th>"""+str(dataframe[coluna3][19])+"""</th>
        <th>"""+str(dataframe[coluna4][19])+"""</th>
        <th>"""+str(dataframe[coluna5][19])+"""</th>
        <th>"""+str(dataframe[coluna6][19])+"""</th>
        <th>"""+str(dataframe[coluna7][19])+"""</th>
        <th>"""+str(dataframe[coluna8][19])+"""</th>
        <th>"""+str(dataframe[coluna9][19])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[20]+"""; height: 42px; color:"""+cor_texto[20]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][20])+"""</th>
        <th>"""+str(dataframe[coluna2][20])+"""</th>
        <th>"""+str(dataframe[coluna3][20])+"""</th>
        <th>"""+str(dataframe[coluna4][20])+"""</th>
        <th>"""+str(dataframe[coluna5][20])+"""</th>
        <th>"""+str(dataframe[coluna6][20])+"""</th>
        <th>"""+str(dataframe[coluna7][20])+"""</th>
        <th>"""+str(dataframe[coluna8][20])+"""</th>
        <th>"""+str(dataframe[coluna9][20])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[21]+"""; height: 42px; color:"""+cor_texto[21]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][21])+"""</th>
        <th>"""+str(dataframe[coluna2][21])+"""</th>
        <th>"""+str(dataframe[coluna3][21])+"""</th>
        <th>"""+str(dataframe[coluna4][21])+"""</th>
        <th>"""+str(dataframe[coluna5][21])+"""</th>
        <th>"""+str(dataframe[coluna6][21])+"""</th>
        <th>"""+str(dataframe[coluna7][21])+"""</th>
        <th>"""+str(dataframe[coluna8][21])+"""</th>
        <th>"""+str(dataframe[coluna9][21])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[22]+"""; height: 42px; color:"""+cor_texto[22]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][22])+"""</th>
        <th>"""+str(dataframe[coluna2][22])+"""</th>
        <th>"""+str(dataframe[coluna3][22])+"""</th>
        <th>"""+str(dataframe[coluna4][22])+"""</th>
        <th>"""+str(dataframe[coluna5][22])+"""</th>
        <th>"""+str(dataframe[coluna6][22])+"""</th>
        <th>"""+str(dataframe[coluna7][22])+"""</th>
        <th>"""+str(dataframe[coluna8][22])+"""</th>
        <th>"""+str(dataframe[coluna9][22])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[23]+"""; height: 42px; color:"""+cor_texto[23]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][23])+"""</th>
        <th>"""+str(dataframe[coluna2][23])+"""</th>
        <th>"""+str(dataframe[coluna3][23])+"""</th>
        <th>"""+str(dataframe[coluna4][23])+"""</th>
        <th>"""+str(dataframe[coluna5][23])+"""</th>
        <th>"""+str(dataframe[coluna6][23])+"""</th>
        <th>"""+str(dataframe[coluna7][23])+"""</th>
        <th>"""+str(dataframe[coluna8][23])+"""</th>
        <th>"""+str(dataframe[coluna9][23])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[24]+"""; height: 42px; color:"""+cor_texto[24]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][24])+"""</th>
        <th>"""+str(dataframe[coluna2][24])+"""</th>
        <th>"""+str(dataframe[coluna3][24])+"""</th>
        <th>"""+str(dataframe[coluna4][24])+"""</th>
        <th>"""+str(dataframe[coluna5][24])+"""</th>
        <th>"""+str(dataframe[coluna6][24])+"""</th>
        <th>"""+str(dataframe[coluna7][24])+"""</th>
        <th>"""+str(dataframe[coluna8][24])+"""</th>
        <th>"""+str(dataframe[coluna9][24])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[25]+"""; height: 42px; color:"""+cor_texto[25]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][25])+"""</th>
        <th>"""+str(dataframe[coluna2][25])+"""</th>
        <th>"""+str(dataframe[coluna3][25])+"""</th>
        <th>"""+str(dataframe[coluna4][25])+"""</th>
        <th>"""+str(dataframe[coluna5][25])+"""</th>
        <th>"""+str(dataframe[coluna6][25])+"""</th>
        <th>"""+str(dataframe[coluna7][25])+"""</th>
        <th>"""+str(dataframe[coluna8][25])+"""</th>
        <th>"""+str(dataframe[coluna9][25])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[26]+"""; height: 42px; color:"""+cor_texto[26]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][26])+"""</th>
        <th>"""+str(dataframe[coluna2][26])+"""</th>
        <th>"""+str(dataframe[coluna3][26])+"""</th>
        <th>"""+str(dataframe[coluna4][26])+"""</th>
        <th>"""+str(dataframe[coluna5][26])+"""</th>
        <th>"""+str(dataframe[coluna6][26])+"""</th>
        <th>"""+str(dataframe[coluna7][26])+"""</th>
        <th>"""+str(dataframe[coluna8][26])+"""</th>
        <th>"""+str(dataframe[coluna9][26])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[27]+"""; height: 42px; color:"""+cor_texto[27]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][27])+"""</th>
        <th>"""+str(dataframe[coluna2][27])+"""</th>
        <th>"""+str(dataframe[coluna3][27])+"""</th>
        <th>"""+str(dataframe[coluna4][27])+"""</th>
        <th>"""+str(dataframe[coluna5][27])+"""</th>
        <th>"""+str(dataframe[coluna6][27])+"""</th>
        <th>"""+str(dataframe[coluna7][27])+"""</th>
        <th>"""+str(dataframe[coluna8][27])+"""</th>
        <th>"""+str(dataframe[coluna9][27])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[28]+"""; height: 42px; color:"""+cor_texto[28]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][28])+"""</th>
        <th>"""+str(dataframe[coluna2][28])+"""</th>
        <th>"""+str(dataframe[coluna3][28])+"""</th>
        <th>"""+str(dataframe[coluna4][28])+"""</th>
        <th>"""+str(dataframe[coluna5][28])+"""</th>
        <th>"""+str(dataframe[coluna6][28])+"""</th>
        <th>"""+str(dataframe[coluna7][28])+"""</th>
        <th>"""+str(dataframe[coluna8][28])+"""</th>
        <th>"""+str(dataframe[coluna9][28])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[29]+"""; height: 42px; color:"""+cor_texto[29]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][29])+"""</th>
        <th>"""+str(dataframe[coluna2][29])+"""</th>
        <th>"""+str(dataframe[coluna3][29])+"""</th>
        <th>"""+str(dataframe[coluna4][29])+"""</th>
        <th>"""+str(dataframe[coluna5][29])+"""</th>
        <th>"""+str(dataframe[coluna6][29])+"""</th>
        <th>"""+str(dataframe[coluna7][29])+"""</th>
        <th>"""+str(dataframe[coluna8][29])+"""</th>
        <th>"""+str(dataframe[coluna9][29])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[30]+"""; height: 42px; color:"""+cor_texto[30]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][30])+"""</th>
        <th>"""+str(dataframe[coluna2][30])+"""</th>
        <th>"""+str(dataframe[coluna3][30])+"""</th>
        <th>"""+str(dataframe[coluna4][30])+"""</th>
        <th>"""+str(dataframe[coluna5][30])+"""</th>
        <th>"""+str(dataframe[coluna6][30])+"""</th>
        <th>"""+str(dataframe[coluna7][30])+"""</th>
        <th>"""+str(dataframe[coluna8][30])+"""</th>
        <th>"""+str(dataframe[coluna9][30])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[31]+"""; height: 42px; color:"""+cor_texto[31]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][31])+"""</th>
        <th>"""+str(dataframe[coluna2][31])+"""</th>
        <th>"""+str(dataframe[coluna3][31])+"""</th>
        <th>"""+str(dataframe[coluna4][31])+"""</th>
        <th>"""+str(dataframe[coluna5][31])+"""</th>
        <th>"""+str(dataframe[coluna6][31])+"""</th>
        <th>"""+str(dataframe[coluna7][31])+"""</th>
        <th>"""+str(dataframe[coluna8][31])+"""</th>
        <th>"""+str(dataframe[coluna9][31])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[32]+"""; height: 42px; color:"""+cor_texto[32]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][32])+"""</th>
        <th>"""+str(dataframe[coluna2][32])+"""</th>
        <th>"""+str(dataframe[coluna3][32])+"""</th>
        <th>"""+str(dataframe[coluna4][32])+"""</th>
        <th>"""+str(dataframe[coluna5][32])+"""</th>
        <th>"""+str(dataframe[coluna6][32])+"""</th>
        <th>"""+str(dataframe[coluna7][32])+"""</th>
        <th>"""+str(dataframe[coluna8][32])+"""</th>
        <th>"""+str(dataframe[coluna9][32])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[33]+"""; height: 42px; color:"""+cor_texto[33]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][33])+"""</th>
        <th>"""+str(dataframe[coluna2][33])+"""</th>
        <th>"""+str(dataframe[coluna3][33])+"""</th>
        <th>"""+str(dataframe[coluna4][33])+"""</th>
        <th>"""+str(dataframe[coluna5][33])+"""</th>
        <th>"""+str(dataframe[coluna6][33])+"""</th>
        <th>"""+str(dataframe[coluna7][33])+"""</th>
        <th>"""+str(dataframe[coluna8][33])+"""</th>
        <th>"""+str(dataframe[coluna9][33])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[34]+"""; height: 42px; color:"""+cor_texto[34]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][34])+"""</th>
        <th>"""+str(dataframe[coluna2][34])+"""</th>
        <th>"""+str(dataframe[coluna3][34])+"""</th>
        <th>"""+str(dataframe[coluna4][34])+"""</th>
        <th>"""+str(dataframe[coluna5][34])+"""</th>
        <th>"""+str(dataframe[coluna6][34])+"""</th>
        <th>"""+str(dataframe[coluna7][34])+"""</th>
        <th>"""+str(dataframe[coluna8][34])+"""</th>
        <th>"""+str(dataframe[coluna9][34])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[35]+"""; height: 42px; color:"""+cor_texto[35]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][35])+"""</th>
        <th>"""+str(dataframe[coluna2][35])+"""</th>
        <th>"""+str(dataframe[coluna3][35])+"""</th>
        <th>"""+str(dataframe[coluna4][35])+"""</th>
        <th>"""+str(dataframe[coluna5][35])+"""</th>
        <th>"""+str(dataframe[coluna6][35])+"""</th>
        <th>"""+str(dataframe[coluna7][35])+"""</th>
        <th>"""+str(dataframe[coluna8][35])+"""</th>
        <th>"""+str(dataframe[coluna9][35])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[36]+"""; height: 42px; color:"""+cor_texto[36]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][36])+"""</th>
        <th>"""+str(dataframe[coluna2][36])+"""</th>
        <th>"""+str(dataframe[coluna3][36])+"""</th>
        <th>"""+str(dataframe[coluna4][36])+"""</th>
        <th>"""+str(dataframe[coluna5][36])+"""</th>
        <th>"""+str(dataframe[coluna6][36])+"""</th>
        <th>"""+str(dataframe[coluna7][36])+"""</th>
        <th>"""+str(dataframe[coluna8][36])+"""</th>
        <th>"""+str(dataframe[coluna9][36])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[37]+"""; height: 42px; color:"""+cor_texto[37]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][37])+"""</th>
        <th>"""+str(dataframe[coluna2][37])+"""</th>
        <th>"""+str(dataframe[coluna3][37])+"""</th>
        <th>"""+str(dataframe[coluna4][37])+"""</th>
        <th>"""+str(dataframe[coluna5][37])+"""</th>
        <th>"""+str(dataframe[coluna6][37])+"""</th>
        <th>"""+str(dataframe[coluna7][37])+"""</th>
        <th>"""+str(dataframe[coluna8][37])+"""</th>
        <th>"""+str(dataframe[coluna9][37])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[38]+"""; height: 42px; color:"""+cor_texto[38]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][38])+"""</th>
        <th>"""+str(dataframe[coluna2][38])+"""</th>
        <th>"""+str(dataframe[coluna3][38])+"""</th>
        <th>"""+str(dataframe[coluna4][38])+"""</th>
        <th>"""+str(dataframe[coluna5][38])+"""</th>
        <th>"""+str(dataframe[coluna6][38])+"""</th>
        <th>"""+str(dataframe[coluna7][38])+"""</th>
        <th>"""+str(dataframe[coluna8][38])+"""</th>
        <th>"""+str(dataframe[coluna9][38])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[39]+"""; height: 42px; color:"""+cor_texto[39]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][39])+"""</th>
        <th>"""+str(dataframe[coluna2][39])+"""</th>
        <th>"""+str(dataframe[coluna3][39])+"""</th>
        <th>"""+str(dataframe[coluna4][39])+"""</th>
        <th>"""+str(dataframe[coluna5][39])+"""</th>
        <th>"""+str(dataframe[coluna6][39])+"""</th>
        <th>"""+str(dataframe[coluna7][39])+"""</th>
        <th>"""+str(dataframe[coluna8][39])+"""</th>
        <th>"""+str(dataframe[coluna9][39])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[40]+"""; height: 42px; color:"""+cor_texto[40]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][40])+"""</th>
        <th>"""+str(dataframe[coluna2][40])+"""</th>
        <th>"""+str(dataframe[coluna3][40])+"""</th>
        <th>"""+str(dataframe[coluna4][40])+"""</th>
        <th>"""+str(dataframe[coluna5][40])+"""</th>
        <th>"""+str(dataframe[coluna6][40])+"""</th>
        <th>"""+str(dataframe[coluna7][40])+"""</th>
        <th>"""+str(dataframe[coluna8][40])+"""</th>
        <th>"""+str(dataframe[coluna9][40])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[41]+"""; height: 42px; color:"""+cor_texto[41]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][41])+"""</th>
        <th>"""+str(dataframe[coluna2][41])+"""</th>
        <th>"""+str(dataframe[coluna3][41])+"""</th>
        <th>"""+str(dataframe[coluna4][41])+"""</th>
        <th>"""+str(dataframe[coluna5][41])+"""</th>
        <th>"""+str(dataframe[coluna6][41])+"""</th>
        <th>"""+str(dataframe[coluna7][41])+"""</th>
        <th>"""+str(dataframe[coluna8][41])+"""</th>
        <th>"""+str(dataframe[coluna9][41])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[42]+"""; height: 42px; color:"""+cor_texto[42]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][42])+"""</th>
        <th>"""+str(dataframe[coluna2][42])+"""</th>
        <th>"""+str(dataframe[coluna3][42])+"""</th>
        <th>"""+str(dataframe[coluna4][42])+"""</th>
        <th>"""+str(dataframe[coluna5][42])+"""</th>
        <th>"""+str(dataframe[coluna6][42])+"""</th>
        <th>"""+str(dataframe[coluna7][42])+"""</th>
        <th>"""+str(dataframe[coluna8][42])+"""</th>
        <th>"""+str(dataframe[coluna9][42])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[43]+"""; height: 42px; color:"""+cor_texto[43]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][43])+"""</th>
        <th>"""+str(dataframe[coluna2][43])+"""</th>
        <th>"""+str(dataframe[coluna3][43])+"""</th>
        <th>"""+str(dataframe[coluna4][43])+"""</th>
        <th>"""+str(dataframe[coluna5][43])+"""</th>
        <th>"""+str(dataframe[coluna6][43])+"""</th>
        <th>"""+str(dataframe[coluna7][43])+"""</th>
        <th>"""+str(dataframe[coluna8][43])+"""</th>
        <th>"""+str(dataframe[coluna9][43])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[44]+"""; height: 42px; color:"""+cor_texto[44]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][44])+"""</th>
        <th>"""+str(dataframe[coluna2][44])+"""</th>
        <th>"""+str(dataframe[coluna3][44])+"""</th>
        <th>"""+str(dataframe[coluna4][44])+"""</th>
        <th>"""+str(dataframe[coluna5][44])+"""</th>
        <th>"""+str(dataframe[coluna6][44])+"""</th>
        <th>"""+str(dataframe[coluna7][44])+"""</th>
        <th>"""+str(dataframe[coluna8][44])+"""</th>
        <th>"""+str(dataframe[coluna9][44])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[45]+"""; height: 42px; color:"""+cor_texto[45]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][45])+"""</th>
        <th>"""+str(dataframe[coluna2][45])+"""</th>
        <th>"""+str(dataframe[coluna3][45])+"""</th>
        <th>"""+str(dataframe[coluna4][45])+"""</th>
        <th>"""+str(dataframe[coluna5][45])+"""</th>
        <th>"""+str(dataframe[coluna6][45])+"""</th>
        <th>"""+str(dataframe[coluna7][45])+"""</th>
        <th>"""+str(dataframe[coluna8][45])+"""</th>
        <th>"""+str(dataframe[coluna9][45])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[46]+"""; height: 42px; color:"""+cor_texto[46]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][46])+"""</th>
        <th>"""+str(dataframe[coluna2][46])+"""</th>
        <th>"""+str(dataframe[coluna3][46])+"""</th>
        <th>"""+str(dataframe[coluna4][46])+"""</th>
        <th>"""+str(dataframe[coluna5][46])+"""</th>
        <th>"""+str(dataframe[coluna6][46])+"""</th>
        <th>"""+str(dataframe[coluna7][46])+"""</th>
        <th>"""+str(dataframe[coluna8][46])+"""</th>
        <th>"""+str(dataframe[coluna9][46])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[47]+"""; height: 42px; color:"""+cor_texto[47]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][47])+"""</th>
        <th>"""+str(dataframe[coluna2][47])+"""</th>
        <th>"""+str(dataframe[coluna3][47])+"""</th>
        <th>"""+str(dataframe[coluna4][47])+"""</th>
        <th>"""+str(dataframe[coluna5][47])+"""</th>
        <th>"""+str(dataframe[coluna6][47])+"""</th>
        <th>"""+str(dataframe[coluna7][47])+"""</th>
        <th>"""+str(dataframe[coluna8][47])+"""</th>
        <th>"""+str(dataframe[coluna9][47])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[48]+"""; height: 42px; color:"""+cor_texto[48]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][48])+"""</th>
        <th>"""+str(dataframe[coluna2][48])+"""</th>
        <th>"""+str(dataframe[coluna3][48])+"""</th>
        <th>"""+str(dataframe[coluna4][48])+"""</th>
        <th>"""+str(dataframe[coluna5][48])+"""</th>
        <th>"""+str(dataframe[coluna6][48])+"""</th>
        <th>"""+str(dataframe[coluna7][48])+"""</th>
        <th>"""+str(dataframe[coluna8][48])+"""</th>
        <th>"""+str(dataframe[coluna9][48])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[49]+"""; height: 42px; color:"""+cor_texto[49]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][49])+"""</th>
        <th>"""+str(dataframe[coluna2][49])+"""</th>
        <th>"""+str(dataframe[coluna3][49])+"""</th>
        <th>"""+str(dataframe[coluna4][49])+"""</th>
        <th>"""+str(dataframe[coluna5][49])+"""</th>
        <th>"""+str(dataframe[coluna6][49])+"""</th>
        <th>"""+str(dataframe[coluna7][49])+"""</th>
        <th>"""+str(dataframe[coluna8][49])+"""</th>
        <th>"""+str(dataframe[coluna9][49])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[50]+"""; height: 42px; color:"""+cor_texto[50]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][50])+"""</th>
        <th>"""+str(dataframe[coluna2][50])+"""</th>
        <th>"""+str(dataframe[coluna3][50])+"""</th>
        <th>"""+str(dataframe[coluna4][50])+"""</th>
        <th>"""+str(dataframe[coluna5][50])+"""</th>
        <th>"""+str(dataframe[coluna6][50])+"""</th>
        <th>"""+str(dataframe[coluna7][50])+"""</th>
        <th>"""+str(dataframe[coluna8][50])+"""</th>
        <th>"""+str(dataframe[coluna9][50])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[51]+"""; height: 42px; color:"""+cor_texto[51]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][51])+"""</th>
        <th>"""+str(dataframe[coluna2][51])+"""</th>
        <th>"""+str(dataframe[coluna3][51])+"""</th>
        <th>"""+str(dataframe[coluna4][51])+"""</th>
        <th>"""+str(dataframe[coluna5][51])+"""</th>
        <th>"""+str(dataframe[coluna6][51])+"""</th>
        <th>"""+str(dataframe[coluna7][51])+"""</th>
        <th>"""+str(dataframe[coluna8][51])+"""</th>
        <th>"""+str(dataframe[coluna9][51])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[52]+"""; height: 42px; color:"""+cor_texto[52]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][52])+"""</th>
        <th>"""+str(dataframe[coluna2][52])+"""</th>
        <th>"""+str(dataframe[coluna3][52])+"""</th>
        <th>"""+str(dataframe[coluna4][52])+"""</th>
        <th>"""+str(dataframe[coluna5][52])+"""</th>
        <th>"""+str(dataframe[coluna6][52])+"""</th>
        <th>"""+str(dataframe[coluna7][52])+"""</th>
        <th>"""+str(dataframe[coluna8][52])+"""</th>
        <th>"""+str(dataframe[coluna9][52])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[53]+"""; height: 42px; color:"""+cor_texto[53]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][53])+"""</th>
        <th>"""+str(dataframe[coluna2][53])+"""</th>
        <th>"""+str(dataframe[coluna3][53])+"""</th>
        <th>"""+str(dataframe[coluna4][53])+"""</th>
        <th>"""+str(dataframe[coluna5][53])+"""</th>
        <th>"""+str(dataframe[coluna6][53])+"""</th>
        <th>"""+str(dataframe[coluna7][53])+"""</th>
        <th>"""+str(dataframe[coluna8][53])+"""</th>
        <th>"""+str(dataframe[coluna9][53])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[54]+"""; height: 42px; color:"""+cor_texto[54]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][54])+"""</th>
        <th>"""+str(dataframe[coluna2][54])+"""</th>
        <th>"""+str(dataframe[coluna3][54])+"""</th>
        <th>"""+str(dataframe[coluna4][54])+"""</th>
        <th>"""+str(dataframe[coluna5][54])+"""</th>
        <th>"""+str(dataframe[coluna6][54])+"""</th>
        <th>"""+str(dataframe[coluna7][54])+"""</th>
        <th>"""+str(dataframe[coluna8][54])+"""</th>
        <th>"""+str(dataframe[coluna9][54])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[55]+"""; height: 42px; color:"""+cor_texto[55]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][55])+"""</th>
        <th>"""+str(dataframe[coluna2][55])+"""</th>
        <th>"""+str(dataframe[coluna3][55])+"""</th>
        <th>"""+str(dataframe[coluna4][55])+"""</th>
        <th>"""+str(dataframe[coluna5][55])+"""</th>
        <th>"""+str(dataframe[coluna6][55])+"""</th>
        <th>"""+str(dataframe[coluna7][55])+"""</th>
        <th>"""+str(dataframe[coluna8][55])+"""</th>
        <th>"""+str(dataframe[coluna9][55])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[56]+"""; height: 42px; color:"""+cor_texto[56]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][56])+"""</th>
        <th>"""+str(dataframe[coluna2][56])+"""</th>
        <th>"""+str(dataframe[coluna3][56])+"""</th>
        <th>"""+str(dataframe[coluna4][56])+"""</th>
        <th>"""+str(dataframe[coluna5][56])+"""</th>
        <th>"""+str(dataframe[coluna6][56])+"""</th>
        <th>"""+str(dataframe[coluna7][56])+"""</th>
        <th>"""+str(dataframe[coluna8][56])+"""</th>
        <th>"""+str(dataframe[coluna9][56])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[57]+"""; height: 42px; color:"""+cor_texto[57]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][57])+"""</th>
        <th>"""+str(dataframe[coluna2][57])+"""</th>
        <th>"""+str(dataframe[coluna3][57])+"""</th>
        <th>"""+str(dataframe[coluna4][57])+"""</th>
        <th>"""+str(dataframe[coluna5][57])+"""</th>
        <th>"""+str(dataframe[coluna6][57])+"""</th>
        <th>"""+str(dataframe[coluna7][57])+"""</th>
        <th>"""+str(dataframe[coluna8][57])+"""</th>
        <th>"""+str(dataframe[coluna9][57])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[58]+"""; height: 42px; color:"""+cor_texto[58]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][58])+"""</th>
        <th>"""+str(dataframe[coluna2][58])+"""</th>
        <th>"""+str(dataframe[coluna3][58])+"""</th>
        <th>"""+str(dataframe[coluna4][58])+"""</th>
        <th>"""+str(dataframe[coluna5][58])+"""</th>
        <th>"""+str(dataframe[coluna6][58])+"""</th>
        <th>"""+str(dataframe[coluna7][58])+"""</th>
        <th>"""+str(dataframe[coluna8][58])+"""</th>
        <th>"""+str(dataframe[coluna9][58])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[59]+"""; height: 42px; color:"""+cor_texto[59]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][59])+"""</th>
        <th>"""+str(dataframe[coluna2][59])+"""</th>
        <th>"""+str(dataframe[coluna3][59])+"""</th>
        <th>"""+str(dataframe[coluna4][59])+"""</th>
        <th>"""+str(dataframe[coluna5][59])+"""</th>
        <th>"""+str(dataframe[coluna6][59])+"""</th>
        <th>"""+str(dataframe[coluna7][59])+"""</th>
        <th>"""+str(dataframe[coluna8][59])+"""</th>
        <th>"""+str(dataframe[coluna9][59])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[60]+"""; height: 42px; color:"""+cor_texto[60]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][60])+"""</th>
        <th>"""+str(dataframe[coluna2][60])+"""</th>
        <th>"""+str(dataframe[coluna3][60])+"""</th>
        <th>"""+str(dataframe[coluna4][60])+"""</th>
        <th>"""+str(dataframe[coluna5][60])+"""</th>
        <th>"""+str(dataframe[coluna6][60])+"""</th>
        <th>"""+str(dataframe[coluna7][60])+"""</th>
        <th>"""+str(dataframe[coluna8][60])+"""</th>
        <th>"""+str(dataframe[coluna9][60])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[61]+"""; height: 42px; color:"""+cor_texto[61]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][61])+"""</th>
        <th>"""+str(dataframe[coluna2][61])+"""</th>
        <th>"""+str(dataframe[coluna3][61])+"""</th>
        <th>"""+str(dataframe[coluna4][61])+"""</th>
        <th>"""+str(dataframe[coluna5][61])+"""</th>
        <th>"""+str(dataframe[coluna6][61])+"""</th>
        <th>"""+str(dataframe[coluna7][61])+"""</th>
        <th>"""+str(dataframe[coluna8][61])+"""</th>
        <th>"""+str(dataframe[coluna9][61])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[62]+"""; height: 42px; color:"""+cor_texto[62]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][62])+"""</th>
        <th>"""+str(dataframe[coluna2][62])+"""</th>
        <th>"""+str(dataframe[coluna3][62])+"""</th>
        <th>"""+str(dataframe[coluna4][62])+"""</th>
        <th>"""+str(dataframe[coluna5][62])+"""</th>
        <th>"""+str(dataframe[coluna6][62])+"""</th>
        <th>"""+str(dataframe[coluna7][62])+"""</th>
        <th>"""+str(dataframe[coluna8][62])+"""</th>
        <th>"""+str(dataframe[coluna9][62])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[63]+"""; height: 42px; color:"""+cor_texto[63]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][63])+"""</th>
        <th>"""+str(dataframe[coluna2][63])+"""</th>
        <th>"""+str(dataframe[coluna3][63])+"""</th>
        <th>"""+str(dataframe[coluna4][63])+"""</th>
        <th>"""+str(dataframe[coluna5][63])+"""</th>
        <th>"""+str(dataframe[coluna6][63])+"""</th>
        <th>"""+str(dataframe[coluna7][63])+"""</th>
        <th>"""+str(dataframe[coluna8][63])+"""</th>
        <th>"""+str(dataframe[coluna9][63])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[64]+"""; height: 42px; color:"""+cor_texto[64]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][64])+"""</th>
        <th>"""+str(dataframe[coluna2][64])+"""</th>
        <th>"""+str(dataframe[coluna3][64])+"""</th>
        <th>"""+str(dataframe[coluna4][64])+"""</th>
        <th>"""+str(dataframe[coluna5][64])+"""</th>
        <th>"""+str(dataframe[coluna6][64])+"""</th>
        <th>"""+str(dataframe[coluna7][64])+"""</th>
        <th>"""+str(dataframe[coluna8][64])+"""</th>
        <th>"""+str(dataframe[coluna9][64])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[65]+"""; height: 42px; color:"""+cor_texto[65]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][65])+"""</th>
        <th>"""+str(dataframe[coluna2][65])+"""</th>
        <th>"""+str(dataframe[coluna3][65])+"""</th>
        <th>"""+str(dataframe[coluna4][65])+"""</th>
        <th>"""+str(dataframe[coluna5][65])+"""</th>
        <th>"""+str(dataframe[coluna6][65])+"""</th>
        <th>"""+str(dataframe[coluna7][65])+"""</th>
        <th>"""+str(dataframe[coluna8][65])+"""</th>
        <th>"""+str(dataframe[coluna9][65])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[66]+"""; height: 42px; color:"""+cor_texto[66]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][66])+"""</th>
        <th>"""+str(dataframe[coluna2][66])+"""</th>
        <th>"""+str(dataframe[coluna3][66])+"""</th>
        <th>"""+str(dataframe[coluna4][66])+"""</th>
        <th>"""+str(dataframe[coluna5][66])+"""</th>
        <th>"""+str(dataframe[coluna6][66])+"""</th>
        <th>"""+str(dataframe[coluna7][66])+"""</th>
        <th>"""+str(dataframe[coluna8][66])+"""</th>
        <th>"""+str(dataframe[coluna9][66])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[67]+"""; height: 42px; color:"""+cor_texto[67]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][67])+"""</th>
        <th>"""+str(dataframe[coluna2][67])+"""</th>
        <th>"""+str(dataframe[coluna3][67])+"""</th>
        <th>"""+str(dataframe[coluna4][67])+"""</th>
        <th>"""+str(dataframe[coluna5][67])+"""</th>
        <th>"""+str(dataframe[coluna6][67])+"""</th>
        <th>"""+str(dataframe[coluna7][67])+"""</th>
        <th>"""+str(dataframe[coluna8][67])+"""</th>
        <th>"""+str(dataframe[coluna9][67])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[68]+"""; height: 42px; color:"""+cor_texto[68]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][68])+"""</th>
        <th>"""+str(dataframe[coluna2][68])+"""</th>
        <th>"""+str(dataframe[coluna3][68])+"""</th>
        <th>"""+str(dataframe[coluna4][68])+"""</th>
        <th>"""+str(dataframe[coluna5][68])+"""</th>
        <th>"""+str(dataframe[coluna6][8])+"""</th>
        <th>"""+str(dataframe[coluna7][68])+"""</th>
        <th>"""+str(dataframe[coluna8][68])+"""</th>
        <th>"""+str(dataframe[coluna9][68])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[69]+"""; height: 42px; color:"""+cor_texto[69]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][69])+"""</th>
        <th>"""+str(dataframe[coluna2][69])+"""</th>
        <th>"""+str(dataframe[coluna3][69])+"""</th>
        <th>"""+str(dataframe[coluna4][69])+"""</th>
        <th>"""+str(dataframe[coluna5][69])+"""</th>
        <th>"""+str(dataframe[coluna6][69])+"""</th>
        <th>"""+str(dataframe[coluna7][69])+"""</th>
        <th>"""+str(dataframe[coluna8][69])+"""</th>
        <th>"""+str(dataframe[coluna9][69])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[70]+"""; height: 42px; color:"""+cor_texto[70]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][70])+"""</th>
        <th>"""+str(dataframe[coluna2][70])+"""</th>
        <th>"""+str(dataframe[coluna3][70])+"""</th>
        <th>"""+str(dataframe[coluna4][70])+"""</th>
        <th>"""+str(dataframe[coluna5][70])+"""</th>
        <th>"""+str(dataframe[coluna6][70])+"""</th>
        <th>"""+str(dataframe[coluna7][70])+"""</th>
        <th>"""+str(dataframe[coluna8][70])+"""</th>
        <th>"""+str(dataframe[coluna9][70])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[71]+"""; height: 42px; color:"""+cor_texto[71]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][71])+"""</th>
        <th>"""+str(dataframe[coluna2][71])+"""</th>
        <th>"""+str(dataframe[coluna3][71])+"""</th>
        <th>"""+str(dataframe[coluna4][71])+"""</th>
        <th>"""+str(dataframe[coluna5][71])+"""</th>
        <th>"""+str(dataframe[coluna6][71])+"""</th>
        <th>"""+str(dataframe[coluna7][71])+"""</th>
        <th>"""+str(dataframe[coluna8][71])+"""</th>
        <th>"""+str(dataframe[coluna9][71])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[72]+"""; height: 42px; color:"""+cor_texto[72]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][72])+"""</th>
        <th>"""+str(dataframe[coluna2][72])+"""</th>
        <th>"""+str(dataframe[coluna3][72])+"""</th>
        <th>"""+str(dataframe[coluna4][72])+"""</th>
        <th>"""+str(dataframe[coluna5][72])+"""</th>
        <th>"""+str(dataframe[coluna6][72])+"""</th>
        <th>"""+str(dataframe[coluna7][72])+"""</th>
        <th>"""+str(dataframe[coluna8][72])+"""</th>
        <th>"""+str(dataframe[coluna9][72])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[73]+"""; height: 42px; color:"""+cor_texto[73]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][73])+"""</th>
        <th>"""+str(dataframe[coluna2][73])+"""</th>
        <th>"""+str(dataframe[coluna3][73])+"""</th>
        <th>"""+str(dataframe[coluna4][73])+"""</th>
        <th>"""+str(dataframe[coluna5][73])+"""</th>
        <th>"""+str(dataframe[coluna6][73])+"""</th>
        <th>"""+str(dataframe[coluna7][73])+"""</th>
        <th>"""+str(dataframe[coluna8][73])+"""</th>
        <th>"""+str(dataframe[coluna9][73])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[74]+"""; height: 42px; color:"""+cor_texto[74]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][74])+"""</th>
        <th>"""+str(dataframe[coluna2][74])+"""</th>
        <th>"""+str(dataframe[coluna3][74])+"""</th>
        <th>"""+str(dataframe[coluna4][74])+"""</th>
        <th>"""+str(dataframe[coluna5][74])+"""</th>
        <th>"""+str(dataframe[coluna6][74])+"""</th>
        <th>"""+str(dataframe[coluna7][74])+"""</th>
        <th>"""+str(dataframe[coluna8][74])+"""</th>
        <th>"""+str(dataframe[coluna9][74])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[75]+"""; height: 42px; color:"""+cor_texto[75]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][75])+"""</th>
        <th>"""+str(dataframe[coluna2][75])+"""</th>
        <th>"""+str(dataframe[coluna3][75])+"""</th>
        <th>"""+str(dataframe[coluna4][75])+"""</th>
        <th>"""+str(dataframe[coluna5][75])+"""</th>
        <th>"""+str(dataframe[coluna6][75])+"""</th>
        <th>"""+str(dataframe[coluna7][75])+"""</th>
        <th>"""+str(dataframe[coluna8][75])+"""</th>
        <th>"""+str(dataframe[coluna9][75])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[76]+"""; height: 42px; color:"""+cor_texto[76]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][76])+"""</th>
        <th>"""+str(dataframe[coluna2][76])+"""</th>
        <th>"""+str(dataframe[coluna3][76])+"""</th>
        <th>"""+str(dataframe[coluna4][76])+"""</th>
        <th>"""+str(dataframe[coluna5][76])+"""</th>
        <th>"""+str(dataframe[coluna6][76])+"""</th>
        <th>"""+str(dataframe[coluna7][76])+"""</th>
        <th>"""+str(dataframe[coluna8][76])+"""</th>
        <th>"""+str(dataframe[coluna9][76])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[77]+"""; height: 42px; color:"""+cor_texto[77]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][77])+"""</th>
        <th>"""+str(dataframe[coluna2][77])+"""</th>
        <th>"""+str(dataframe[coluna3][7])+"""</th>
        <th>"""+str(dataframe[coluna4][77])+"""</th>
        <th>"""+str(dataframe[coluna5][77])+"""</th>
        <th>"""+str(dataframe[coluna6][77])+"""</th>
        <th>"""+str(dataframe[coluna7][77])+"""</th>
        <th>"""+str(dataframe[coluna8][77])+"""</th>
        <th>"""+str(dataframe[coluna9][77])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[78]+"""; height: 42px; color:"""+cor_texto[78]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][78])+"""</th>
        <th>"""+str(dataframe[coluna2][78])+"""</th>
        <th>"""+str(dataframe[coluna3][78])+"""</th>
        <th>"""+str(dataframe[coluna4][78])+"""</th>
        <th>"""+str(dataframe[coluna5][78])+"""</th>
        <th>"""+str(dataframe[coluna6][78])+"""</th>
        <th>"""+str(dataframe[coluna7][78])+"""</th>
        <th>"""+str(dataframe[coluna8][78])+"""</th>
        <th>"""+str(dataframe[coluna9][78])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[79]+"""; height: 42px; color:"""+cor_texto[79]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][79])+"""</th>
        <th>"""+str(dataframe[coluna2][79])+"""</th>
        <th>"""+str(dataframe[coluna3][79])+"""</th>
        <th>"""+str(dataframe[coluna4][79])+"""</th>
        <th>"""+str(dataframe[coluna5][79])+"""</th>
        <th>"""+str(dataframe[coluna6][79])+"""</th>
        <th>"""+str(dataframe[coluna7][79])+"""</th>
        <th>"""+str(dataframe[coluna8][79])+"""</th>
        <th>"""+str(dataframe[coluna9][79])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[80]+"""; height: 42px; color:"""+cor_texto[80]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][80])+"""</th>
        <th>"""+str(dataframe[coluna2][80])+"""</th>
        <th>"""+str(dataframe[coluna3][80])+"""</th>
        <th>"""+str(dataframe[coluna4][80])+"""</th>
        <th>"""+str(dataframe[coluna5][80])+"""</th>
        <th>"""+str(dataframe[coluna6][80])+"""</th>
        <th>"""+str(dataframe[coluna7][80])+"""</th>
        <th>"""+str(dataframe[coluna8][80])+"""</th>
        <th>"""+str(dataframe[coluna9][80])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[81]+"""; height: 42px; color:"""+cor_texto[81]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][81])+"""</th>
        <th>"""+str(dataframe[coluna2][81])+"""</th>
        <th>"""+str(dataframe[coluna3][81])+"""</th>
        <th>"""+str(dataframe[coluna4][81])+"""</th>
        <th>"""+str(dataframe[coluna5][81])+"""</th>
        <th>"""+str(dataframe[coluna6][81])+"""</th>
        <th>"""+str(dataframe[coluna7][81])+"""</th>
        <th>"""+str(dataframe[coluna8][81])+"""</th>
        <th>"""+str(dataframe[coluna9][81])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[82]+"""; height: 42px; color:"""+cor_texto[82]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][82])+"""</th>
        <th>"""+str(dataframe[coluna2][82])+"""</th>
        <th>"""+str(dataframe[coluna3][82])+"""</th>
        <th>"""+str(dataframe[coluna4][82])+"""</th>
        <th>"""+str(dataframe[coluna5][82])+"""</th>
        <th>"""+str(dataframe[coluna6][82])+"""</th>
        <th>"""+str(dataframe[coluna7][82])+"""</th>
        <th>"""+str(dataframe[coluna8][82])+"""</th>
        <th>"""+str(dataframe[coluna9][82])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[83]+"""; height: 42px; color:"""+cor_texto[83]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][83])+"""</th>
        <th>"""+str(dataframe[coluna2][83])+"""</th>
        <th>"""+str(dataframe[coluna3][83])+"""</th>
        <th>"""+str(dataframe[coluna4][83])+"""</th>
        <th>"""+str(dataframe[coluna5][83])+"""</th>
        <th>"""+str(dataframe[coluna6][83])+"""</th>
        <th>"""+str(dataframe[coluna7][83])+"""</th>
        <th>"""+str(dataframe[coluna8][83])+"""</th>
        <th>"""+str(dataframe[coluna9][83])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[84]+"""; height: 42px; color:"""+cor_texto[84]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][84])+"""</th>
        <th>"""+str(dataframe[coluna2][84])+"""</th>
        <th>"""+str(dataframe[coluna3][84])+"""</th>
        <th>"""+str(dataframe[coluna4][84])+"""</th>
        <th>"""+str(dataframe[coluna5][84])+"""</th>
        <th>"""+str(dataframe[coluna6][84])+"""</th>
        <th>"""+str(dataframe[coluna7][84])+"""</th>
        <th>"""+str(dataframe[coluna8][84])+"""</th>
        <th>"""+str(dataframe[coluna9][84])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[85]+"""; height: 42px; color:"""+cor_texto[85]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][85])+"""</th>
        <th>"""+str(dataframe[coluna2][85])+"""</th>
        <th>"""+str(dataframe[coluna3][85])+"""</th>
        <th>"""+str(dataframe[coluna4][85])+"""</th>
        <th>"""+str(dataframe[coluna5][85])+"""</th>
        <th>"""+str(dataframe[coluna6][85])+"""</th>
        <th>"""+str(dataframe[coluna7][85])+"""</th>
        <th>"""+str(dataframe[coluna8][85])+"""</th>
        <th>"""+str(dataframe[coluna9][85])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[86]+"""; height: 42px; color:"""+cor_texto[86]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][86])+"""</th>
        <th>"""+str(dataframe[coluna2][86])+"""</th>
        <th>"""+str(dataframe[coluna3][86])+"""</th>
        <th>"""+str(dataframe[coluna4][86])+"""</th>
        <th>"""+str(dataframe[coluna5][86])+"""</th>
        <th>"""+str(dataframe[coluna6][86])+"""</th>
        <th>"""+str(dataframe[coluna7][86])+"""</th>
        <th>"""+str(dataframe[coluna8][86])+"""</th>
        <th>"""+str(dataframe[coluna9][86])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[87]+"""; height: 42px; color:"""+cor_texto[87]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][87])+"""</th>
        <th>"""+str(dataframe[coluna2][87])+"""</th>
        <th>"""+str(dataframe[coluna3][87])+"""</th>
        <th>"""+str(dataframe[coluna4][87])+"""</th>
        <th>"""+str(dataframe[coluna5][87])+"""</th>
        <th>"""+str(dataframe[coluna6][87])+"""</th>
        <th>"""+str(dataframe[coluna7][87])+"""</th>
        <th>"""+str(dataframe[coluna8][87])+"""</th>
        <th>"""+str(dataframe[coluna9][87])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[88]+"""; height: 42px; color:"""+cor_texto[88]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][88])+"""</th>
        <th>"""+str(dataframe[coluna2][88])+"""</th>
        <th>"""+str(dataframe[coluna3][88])+"""</th>
        <th>"""+str(dataframe[coluna4][88])+"""</th>
        <th>"""+str(dataframe[coluna5][88])+"""</th>
        <th>"""+str(dataframe[coluna6][88])+"""</th>
        <th>"""+str(dataframe[coluna7][88])+"""</th>
        <th>"""+str(dataframe[coluna8][88])+"""</th>
        <th>"""+str(dataframe[coluna9][88])+"""</th>
      </tr>
      <tr style="background-color:"""+cor_back[89]+"""; height: 42px; color:"""+cor_texto[89]+"""; font-size: 16px;text-align: center">
        <th>"""+str(dataframe[coluna1][89])+"""</th>
        <th>"""+str(dataframe[coluna2][89])+"""</th>
        <th>"""+str(dataframe[coluna3][89])+"""</th>
        <th>"""+str(dataframe[coluna4][89])+"""</th>
        <th>"""+str(dataframe[coluna5][89])+"""</th>
        <th>"""+str(dataframe[coluna6][89])+"""</th>
        <th>"""+str(dataframe[coluna7][89])+"""</th>
        <th>"""+str(dataframe[coluna8][89])+"""</th>
        <th>"""+str(dataframe[coluna9][89])+"""</th>
      </tr>
      
      
    </table>
    """
    return html_table_questoes