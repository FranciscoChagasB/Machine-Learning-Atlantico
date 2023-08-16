# Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd

# Leitura do .csv em um DataFrame.
data_frame = pd.read_csv('arquivo.csv')

# Exibir as primeiras linhas do DataFrame.
x = 5
# .head() exibe as primeiras 5 linhas e .head(x) exibe as primeiras x linhas do DataFrame.
print(data_frame.head(x))

"""
Essa é uma abordagem fundamental para realizar a leitura e 
observar os conteúdos de um arquivo CSV em um DataFrame utilizando a biblioteca Pandas.
"""