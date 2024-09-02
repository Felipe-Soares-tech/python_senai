# 13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input('diga um mes entre o numero 1 e 12 '))

if mes == 3:
    print('transição do verao para o outono')
elif mes == 4 or mes == 5:
    print('nesses meses acontecem o outono')
elif mes == 6:
    print('transição do outono para inverno')
elif mes == 7 or mes == 8:
    print('está no inverno')
elif mes == 9:
    print('transição do inverno para a primavera')
elif mes == 10 or mes == 11:
    print('meses da primavera')

elif mes == 12:
    print('transição da primavera pro verao')

elif mes == 1 or mes == 2:
    print('meses do verao')









