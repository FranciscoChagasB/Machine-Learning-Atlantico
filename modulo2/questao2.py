# Utilizando o matplotlib, utilize a função subplot() para mostrar 6 gráficos.

import matplotlib.pyplot as plt
import numpy as np

# Definindo dados para o gráfico.
x = np.linspace(0, 2*np.pi, 100) # Cria uma sequência de valores igualmente espaçados.
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x
y4 = x**2
y5 = np.exp(x)
y6 = np.log(x + 1)

# Cria uma grade de 2x3 para os gráficos.
plt.figure(figsize=(12, 8))

# Gráfico 1.
plt.subplot(2, 3, 1)
plt.plot(x, y1)
plt.title('Seno')

# Gráfico 2.
plt.subplot(2, 3, 2)
plt.plot(x, y2)
plt.title('Cosseno')

# Gráfico 3.
plt.subplot(2, 3, 3)
plt.plot(x, y3)
plt.title('Linear')

# Gráfico 4.
plt.subplot(2, 3, 4)
plt.plot(x, y4)
plt.title('Quadrático')

# Gráfico 5.
plt.subplot(2, 3, 5)
plt.plot(x, y5)
plt.title('Exponencial')

# Gráfico 6.
plt.subplot(2, 3, 6)
plt.plot(x[1:], y6[1:])
plt.title('Logarítmico')

# Mostra o gráfico.
plt.show()