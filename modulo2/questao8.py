# Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd

# Leitura do .csv em um DataFrame.
data_frame = pd.read_csv('arquivo.csv')

# Método .isna() que verifica se cada elemento no DataFrame é um valor NaN.
valores_ausentes = data_frame.isna() # .isna retorna um DataFrame com True onde há valores ausentes.

# Método .dropna() que remove linhas ou colunas com valores ausentes.
linhas_com_valores_ausentes = data_frame.dropna(axis=0) # axis=0 se refere ao eixo das linhas.
colunas_com_valores_ausentes = data_frame.dropna(axis=1) # axis=1 se refere ao eixo das colunas.

"""
Essas são apenas algumas maneiras de lidar com valores ausentes. Outras bibliotecas como notna(), .fillna(), etc.
A escolha da abordagem vai variar de acordo com o contexto dos seus dados e a sua necessidade.
"""