# 16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = input('escolha um combustivel entre gasolina, etanol ou diesel: ')

if combustivel == 'gasolina':
    print('o preço é R$5,35 p/litro')
elif combustivel == 'etanol':
     print('o preço é R$3,44 p/litro')
elif combustivel == 'diesel':
     print('o preço é R$5,68 p/litro')
else:
     print('essa nao é uma opção')












