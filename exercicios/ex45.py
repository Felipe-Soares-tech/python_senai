# 45. Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.


maior = None

for numero in range(5):
    num = int(input('digite um numero: '))

    if maior is None or num > maior:
        maior = num

print(f'O maior numero digitado é {maior}')
