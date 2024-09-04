# 46. Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

soma = 0

for numero in range(10):
    num = int(input('digite um numero: '))
    soma += num

print(soma/10)





