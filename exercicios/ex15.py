# 15. Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

idade = int(input('qual sua idade '))
lista = [13,14,15,16,17]

if idade in lista:
    print('voce é adolescente')
else:
    print('voce nao é adolescente')