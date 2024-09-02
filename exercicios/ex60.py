# 60. Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

num = int(input('digite um numero: '))

lista = []

for divisor in range(1,num+1):
    if num%divisor==0:
        lista.append(divisor)
        
print(f'os divisores de {num} sao {lista}')

