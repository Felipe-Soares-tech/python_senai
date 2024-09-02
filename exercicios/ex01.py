# 1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").


numero = int(input('diga um numero de 1 a 3: '))

match numero:
    case 1:
        print('um')
    case 2:
        print('dois')
    case 3:
        print('tres')
    case _:
        print('nao se encaixa no que eu te pedi')