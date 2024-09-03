nomes = [ 'Neymar', 'Mesi', 'Cris', 'Mbappe']

posicao2 = int()

#def para enumerar a lista de a
def enum():
    for enumeracao, names in enumerate(nomes, start=1 ):
        print(f'{enumeracao}: {names} \n') 

# enumeração igual a zero para poder substituir dps
enumeracao = 0

#def para adcicionar nome novo na lista
def add(a):
    nomes.append(a)
#def para selecionar o nome que o usuario escolher
def subs(a,b):
    match a:
        case 1:
            nomes[0] = b
        case 2:
            nomes[1] = b
        case 3:
            nomes[2] = b
        case 4:
            nomes[3] = b


def excluir2(b):
    match b:
        case 1:
            nomes.pop(1)
        case 2:
            nomes.pop(2)
        case 3:
            nomes.pop(3)
        case 4:
            nomes.pop(4)
 
#def para excluir nome da lista segundo o que o usuario escolher
def excluir(b):
    nomes.pop(b)


#hud(tela)para interação das opções sobre oq fazer
def hud():
    print('''1) digite 1 para cadastrar um nome na lista
2) digite 2 para adicionar um nome no lugar de outro
3) digite 3 para excluir um nome
4) digite 4 para listar a parada 
    ''')
    print('+='*40)