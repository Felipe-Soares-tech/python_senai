# 22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.
numero1 = int(input('diga um numero '))
numero2 = int(input('diga outro numero '))

if numero1 > numero2:
    print(f'primeiro numero ({numero1}) é maior que o segundo ({numero2})')

if numero1 < numero2:
    print(f'segundo numero ({numero2}) é maior que o primero ({numero1})')
