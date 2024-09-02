# 62. Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

lista = []

for i in range(3):
    name = input('diga um nome: ')
    lista.append(name)

for i in lista:
    print(i)