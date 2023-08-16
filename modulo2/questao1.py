# Utilizando o matplotlib, crie e mostre um gráfico de linha simples e adicione títulos aos eixos X e Y do gráfico.

import matplotlib.pyplot as plt

# Cria uma figura e um conjunto de eixos.
fig, ax =  plt.subplots()

# Configurações do gráfico.
ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")

# Mostra o gráfico.
plt.show()