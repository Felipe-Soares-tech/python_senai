# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = input('escolha uma cor entre vermelho, verde e azul: ').lower().strip()

if cor == 'vermelho':
    print('voce tem um bom gosto pra cores')
elif cor == 'verde':
    print('pessima escolha de cor')
elif cor == 'azul':
    print('é uma boa cor')
else:
    print('nao pedi essa cor amigão')

