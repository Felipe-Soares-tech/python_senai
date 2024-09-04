# 63. Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.


lista = []

num = 0

for i in range(5):
    num = int(input(f'{i+1})escreva um numero: '))

    lista.append(num)

soma = sum(lista)
print(soma)






