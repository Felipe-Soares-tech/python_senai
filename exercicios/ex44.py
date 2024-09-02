# 44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

number_list = []

for pergunta in range(10):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        number_list.append(num)

for pergunta in range(10):
    print(f'Os números pares são: {number_list[pergunta]}')


