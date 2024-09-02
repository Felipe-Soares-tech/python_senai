# 7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = int(input('dê uma nota de 0 a 10 '))

# lista1 = [1,2,3]
# lista2 = [4,5,6]
# lista3 = [7,8,9,10]
while nota > 10:
    nota = int(input('dê uma nota de 0 a 10!!!  '))


if nota == 1 or nota == 2 or nota == 3:
    print('nota baixa')
elif nota == 4 or nota == 5 or nota == 6:
    print('nota média')
elif nota == 7 or nota == 8 or nota == 9:
    print('nota alta')
elif nota == 10:
    print('nota maxima')
else:
    print('nao existe essa nota')
