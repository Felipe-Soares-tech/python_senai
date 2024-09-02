# 49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10

lista = []


for num in range(7):
    num1 = int(input('digite um numero '))
    if num1 > 10:
        lista.append(num1)

for num in lista:
    print(num)

    