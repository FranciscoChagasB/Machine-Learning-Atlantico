# Complete o código

import matplotlib.pyplot as plt # Biblioteca matplotlib.
import numpy as np # Biblioteca numpy.
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
layout="constrained")
for row in range(2): # Percorre linha.
    for col in range(2): # Percorre coluna.
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
        transform=axs[row, col].transAxes,
        ha='center', va='center', fontsize=18, # Define o tamanho do texto.
        color='darkgrey')
fig.suptitle('plt.subplots()') 
