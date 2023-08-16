# Utilizando pandas, como remover uma coluna de um DataFrame?

import pandas as pd

# Leitura do .csv em um DataFrame.
data_frame = pd.read_csv('arquivo.csv')

# Removendo uma coluna pelo nome com .drop().
data_frame_coluna_removida = data_frame.drop("Nome da Coluna", axis=1) # axis=1 se refere ao eixo das colunas.

# Removendo uma coluna pelo índice com .drop().
indice = 2
data_frame_coluna_removida = data_frame.drop(data_frame.columns[indice], axis=1) # axis=1 se refere ao eixo das colunas.

"""
O nome da coluna ou índice deve ser ajustado de acordo com a coluna a ser removida
*O método .drop() vem por padrao com inplace=False, ou seja, o DataFrame original não é modificado,
em vez disso é criado outro DataFrame.
"""