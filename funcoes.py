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