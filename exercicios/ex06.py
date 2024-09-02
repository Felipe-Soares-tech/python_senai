# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

simbolo = str(input('escolha entre: adição, multiplicação, subtração e divisão: ')).lower().strip()
numero1 = int(input('escolha um primeiro numero para a operação: '))
numero2 = int(input('escolha um segundo numero para a operação: '))
adição = numero1 + numero2
subtração = numero1 - numero2
multi = numero1 * numero2
divisao = numero1 / numero2
match simbolo:
    case 'adição':
        print(f'ja que escolheu adição, {numero1} mais {numero2} é igual {adição}')
    case 'subtração':
        print(f'ja que escolheu subtração, {numero1} menos {numero2} é igual {subtração}')
    case 'multiplicação':
        print(f'ja que escolheu multiplicação, {numero1} multiplicado por {numero2} é igual {multi}')
    case 'divisão':
        print(f'ja que escolheu divisão, {numero1} dividido por {numero2} é igual {divisao}')
    




