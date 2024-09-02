# 40. Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

numero1 = int(input('diga um numero '))
numero2 = int(input('diga outro numero '))
numero3 = int(input('diga outro numero '))


if numero1 == numero2 and numero1 == numero3:
    print('os 3 numeros sao iguais')
else:
    print('algum numero(s) está diferente')
