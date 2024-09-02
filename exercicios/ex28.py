# 28. Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

palavra = input('insira aqui uma palavra aleatoria ')

leitura = len(palavra)

if leitura >5:
    print('sua palavra tem mais de 5 letras')

elif leitura == 5:
    print('sua palavra tem 5 letras')

else:
    print('sua palavra tem menos q 5 letras')





