# 66. Escreva um
# algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o
# nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar
# uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for
# inserida.
import operations as op
#lista:
nomes = [ 'Neymar', 'Mesi', 'Cris', 'Mbappe']
from os import system

system('cls')




#reações das ações de acordo oq o usuario vai escolher
operacao = 'sim'

while operacao == 'sim':

        
        print(op.hud())
        print(op.enum())
        ask = int(input('selecione um numero: '))

        

        while ask > 4 or ask < 0:
            print('ERRO!')

                
                    

        match ask:
                
            case 1:
                cadastro = input('digite um nome: ').strip().capitalize()
                op.add(cadastro)
                print(op.enum())
                

            case 2:
                posicao = int(input('digite a posição do numero que voce quer tirar: '))
                novo_nome = input('diga o novo nome: ').strip().capitalize()
                op.subs(posicao,novo_nome)
                print(op.enum())

            case 3:
                posicao2 = int(input('digite a posição do numero que voce quer excluir!: '))
                op.excluir(posicao2-1)
                print(op.enum())
            case 4:
                print(op.enum())
            case _:
                print('ERRO')
                ask = int(input('selecione um numero: '))
        operacao = input('Deseja realizar outra ação? ').strip().lower()

        if operacao == 'não':
            print('ok')
            break

        while operacao != 'sim' and operacao!= 'não' and operacao!= 'nao':
            print(f'\033[0;31;40m ERRO!Palavra inválida! \033[m')
            operacao = input('Deseja realizar outra ação? "sim" ou "não" ').strip().lower()
                



# 1 or ask != 2 or ask != 3 or ask != 4
