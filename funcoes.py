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