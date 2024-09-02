# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia = int(input('diga um numero de 1 a 7 para eu dizer que dia da semana ele é '))

match dia:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3: 
        print('terça')
    case 4:
        print('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sábado')
    case _:
        print('esse numero nao é reconhecido')
    









