# 56. Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

mensagem = input('escreva uma mensagem qualquer: ')
vezes = int(input('quantas vezes voce quer que essa mensagem apareça? '))
valor = 0
while valor < vezes:
    print(mensagem)
    valor+=1
