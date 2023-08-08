# Escreva um programa que solicite ao usuário uma palavra e verifique se ela é um palíndromo
# (igual ao ler de trás para frente).

# Recebe uma string do usuário.
string = str(input("Insira uma palavra: "))

# Cria uma string auxiliar com a string do usuário invertida.
string_aux = string[::-1]

# Verifica se as strings são iguais, caso sim, é um palíndromo.
if (string == string_aux):
    print("A palavra que você digitou é um palíndromo!")
else:
    print("A palavra que você digitou não é um palíndromo!")