# Utilizando pandas, mostre uma forma de detectar e tratar valores outliers em um DataFrame.

import pandas as pd
import numpy as np

# Supondo um DataFrame já existente.
# Criando um DataFrame de exemplo.
data = {'Coluna1': [1, 2, 3, 4, 100],
        'Coluna2': [10, 20, 30, 40, 2000]}
data_frame = pd.DataFrame(data)

# Calculando os escores.
# .mean() calcula a média, .std() calcula o desvio padrão e np.abs() calcula o valor absoluto dos Z-Scores.
z_scores = np.abs((data_frame - data_frame.mean()) / data_frame.std()) 
# A fórmula divide cada valor do DataFrame que foi subtraído pela média da coluna pelo desvio padrão da mesma coluna.
# Isso é conhecido como Z-Score e é uma medida de quantos desvios padrão um valor está longe da média da coluna.

# Definindo um limite de 3 para considerar outliers
outliers = z_scores > 3
# As variáveis z_scores e outliers serão responsáveis por detectar os outliers.

# Tratando valores outliers.
data_frame[outliers] = np.nan # Substituindo outliers por NaN.
data_frame.fillna(data_frame.median(), inplace=True) # Preenchendo NaN com valores medianos.

"""
Nesse exemplo, Substituímos os outliers por NaN e preenchemos os valores NaN com os valores medianos
da coluna correspondente, mas, o tratamento de outliers vai variar de acordo com o contexto dos seus
dados e a sua necessidade.
"""