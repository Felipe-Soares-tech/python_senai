# 27. Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero1 = int(input('diga um numero '))
numero2 = int(input('diga outro numero '))
numero3 = int(input('diga outro numero '))

if numero1 > numero2 and numero1>numero3:
    print(f'o primeiro numero {numero1} é o maior de todos')

elif numero2>numero1 and numero2>numero3:
    print(f'o segundo numero {numero2} é o maior de todos')

elif numero3>numero2 and numero3>numero1:
    print(f'o terceiro numero {numero3} é o maior de todos')




