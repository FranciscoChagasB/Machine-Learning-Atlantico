#Dada uma lista de strings ['banana', 'maça', 'laranja', 'abacaxi'], crie uma nova lista com as palavras que tem
#mais de 5 letras e outra lista com as palavras que terminam com a letra a.

# Cria a lista proposta na questão.
lista = ['banana', 'maça', 'laranja', 'abacaxi']

# Lista para armazenar as palavras que tem 5 letras.
lista_cinco_letras = []

# Lista para armazenar as palavras que terminam com a letra 'a'.
lista_termina_coma = []

# Laço 'for' percorrendo cada item da lista
for fruta in lista:
    # Caso a palavra tenha 5 letras armazena na lista 'lista_cinco_letras'.
    if len(fruta) == 5:
        lista_cinco_letras.append(fruta)

    # Caso a palavra termine com a letra 'a' armazena na lista 'lista_termina_coma'.
    if fruta[-1] == 'a':
        lista_termina_coma.append(fruta)

# Imprime a lista com as palavras de 5 letras
print("Palavras que tem cinco letras: ", lista_cinco_letras)

# Imprime a lista com as palavras que terminam com 'a'.
print("Palavras que terminam com a letra a: ", lista_termina_coma)