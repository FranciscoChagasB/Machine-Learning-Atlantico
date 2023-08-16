# Complete o código

import matplotlib.pyplot as plt
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3)) # Pyplot que foi definido como plt.
plt.subplot(131)
plt.bar(names, values) # Adicionar os valores para o gráfico em barra.
plt.subplot(132)
plt.scatter(names, values) # Adicionar os valores para o gráfico de dispersão.
plt.subplot(133) # Criar terceiro subplot.
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show() # Mostrar os gráficos