# Utilizando pandas como selecionar uma coluna específica
# e filtrar linhas em um “DataFrame” com base em uma condição?

import pandas as pd

# Leitura do .csv em um DataFrame.
data_frame = pd.read_csv('arquivo.csv')

coluna = data_frame["Nome_da_coluna"]

# Cria uma condição, nesse exemplo filtra as linhas do DataFrame onde os valores são menores que x.
x = 1000
condicao = data_frame['Nome_da_coluna'] < x

# Retorna e imprime as linhas que atendem a condição.
linhas_filtradas = data_frame[condicao]
print(linhas_filtradas)

"""
O nome da coluna e a condição serão ajustados de acordo com a necessidade.
"""