# 52. Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

senha = 0

while senha != 1234:
    senha = int(input('digite uma senha: '))
    if senha == 1234:
        print('parabens seu tchola')





