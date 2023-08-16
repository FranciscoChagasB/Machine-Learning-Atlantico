# Complete o código

import numpy as np
import matplotlib as mpl # Biblioteca matplotlib.
import matplotlib.pyplot as plt # Biblioteca matplotlib.
x = np.linspace(-2 * np.pi, 2 * np.pi, 100) # Função linspace para criar uma sequência de valores igualmente espaçados.
y = np.sin(x) # Seno.
fig, ax = plt.subplots() # Variável da figura (fig) e eixo (ax).
ax.plot(x, y) # Plota o gráfico com as variáveis x e y.