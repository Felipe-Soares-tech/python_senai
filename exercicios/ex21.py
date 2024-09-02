# 21. Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10

numero1 = int(input('diga um numero '))
numero2 = int(input('diga outro numero '))
soma = numero1 + numero2

if numero1 + numero2 > 10:
    print(f'seu numero({soma}) é maior que 10')

elif numero1 + numero2 == 10:
    print(f'seu numero({soma}) é igual a 10')

else:
    print(f'seu numero({soma}) é menor que 10')