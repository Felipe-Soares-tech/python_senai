# 5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero1 = int(input('diga um numero: '))
numero2 = int(input('diga outro numero: '))

if numero1%2 == 0 and numero2%2 == 0:
    print('ambos numeros sao pares')
elif numero1%2 != 0 and numero2%2 == 0:
    print(f'apenas o numero {numero2} é par')
elif numero2%2 != 0 and numero1%2 == 0:
    print(f'apenas o numero {numero1} é par')
elif numero2%2 != 0 and numero1%2 != 0:
    print('nenhum dos numeros sao pares')







