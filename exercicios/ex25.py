# 25. Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

numero = int(input('diga um numero de 1 a 20 '))
lista = [10,11,12,13,14,15]

if numero in lista:
    print(f'seu numero {numero} está entre 10 e 15')
elif numero > 20:
    print('está fora do que eu pedi')
else:
    print(f'seu numero {numero} nao esta entre 10 e 15')










