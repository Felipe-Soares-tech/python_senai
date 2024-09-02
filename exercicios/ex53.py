# 53. Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.



import time

numero = int(input('digite um numero: '))

for num in range(numero,0, -1):
    print(num)
    time.sleep(1)
print('boom modafucker')