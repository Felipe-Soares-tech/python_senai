# 57. Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

from random import randint 

secreto = randint(1,10)

numero = int(input('digite um numero: '))
while secreto != numero:
    numero = int(input('tente descobrir o numero secreto: '))
    if numero == secreto:
        print('parabens seu tchola')
    






