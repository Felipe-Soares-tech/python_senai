# Cada aluno cadastrado deve ter atrelado a seus dados pessoais (nome, e-mail, data de nascimento, matricula), no caso de matricula você deve gerar uma matricula unica para cada aluno cadastrado.
# Cada um dos dados do aluno devem ser validade de forma o código não quebre ao serem informados valores incorretos.
# Para atualizar qualquer dado do aluno você deve localiza-lo utilizando de sua matricula para isso. Valide de forma que o sistema não quebre ao ser inserido uma matricula invalida.
# Para remover um aluno deve-se realizar esta ação usando de sua matricula, o sistema não pode quebrar ao ser inserido uma matricula errada.
# Ao listar todos os alunos mostre cada um de forma organizada e separada.
# Crie uma funcionalidade de mostre os dados de um aluno especifico usando apenas de sua matricula para isso.

import codigos as op
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
            ask = int(input('selecione um numero: '))

        match ask:
        

            case 1:
                cadastro = input('digite um nome: ').strip().capitalize()
                email = input('qual o email do aluno: ')
                nascimento_ = input('informe a data de nascimento do aluno: ')
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

        while operacao != 'sim' and operacao!= 'não':
            print(f'\033[0;31;40m ERRO!Palavra inválida! \033[m')
            operacao = input('Deseja realizar outra ação? "sim" ou "não" ').strip().lower()


