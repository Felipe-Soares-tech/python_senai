# 51. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).

num = 1
soma = 0

while num != 0:
    num = int(input('digite um numero '))
    soma += num
print(f'a soma é {soma}')
    





