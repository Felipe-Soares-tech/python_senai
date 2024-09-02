# 26. Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.
numero1 = int(input('diga um numero '))
numero2 = int(input('diga outro numero '))

if numero1%5 == 0 and numero2%5 == 0:
    print('seu numeros sao multiplo de 5')
else:
    print('nem todos seus numeros sao multiplos de 5')
