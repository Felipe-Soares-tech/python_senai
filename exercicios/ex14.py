# 14. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

numero1 = int(input('diga um numero '))
numero2 = int(input('diga outro numero '))
soma = numero1 + numero2

if numero1 + numero2 > 100:
    print(f'seu numero({soma}) é maior que 100')

elif numero1 + numero2 == 100:
    print(f'seu numero({soma}) é igual a 100')

else:
    print(f'seu numero({soma}) é menor que 100')






