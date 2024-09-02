# 65. Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.
lista = []

num = 0

for i in range(5):
    num = int(input(f'{i+1}) escreva um numero: '))
    lista.append(num)

maior = max(lista)

menor = min(lista)

print(f'o menor numero é {menor}, e o maior é {maior}!')
# lucianolpsf