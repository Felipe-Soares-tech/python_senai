# 37. Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.
numero = int(input('digite um numero '))
if numero%2 == 0:
    print('seu numero é multiplo de 2')
    if numero%5 == 0:
        print('seu numero tambem é multiplo de 5')
else:
    print('seu numero nao é multiplo de nenhum')