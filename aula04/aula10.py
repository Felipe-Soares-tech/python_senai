#funções 



num = [1,2,3,4,5,6,54,3]

print(max(num))
print(min(num))
print(len(num))
print(sum(num))
media = sum(num)/len(num)
print(media)

def media(num):
    soma = sum(num)/len(num)
    return soma 

print(media(num))

num1 = 2
num2 = 3



#com return
def soma(a, b):
    num3 = num1 + num2
    return num3

print(soma(num1,num2))  

# SEM RETURN
def futebol(jogador):
    print(f'melhor jogador do mundo {jogador}')
    

futebol('ney')   

def nominal(nome):
    nome = 'gay'
    input(f'qual seu nome, {nome}?')


def soma(a,b):
    somas = a+b
    return somas
print(soma(10,10))


somar = lambda a, b: a+b
print(somar(12,12))


def pinto(*args):
    print('argumentos posicionais: ',args)

pinto(1,4,'felipao','legal pora')

def informacoes(**args):
    print('argumentos posicionais:',args)

informacoes(jogador = 'neymar', idade = 30, time = 'flamengo')


pessoa = {
    'nome':'neymar',
    'time':'barcelona',
    'idade':30,
    'pronome':'delas',
    'estado': 'online e roteando'
}
{
    'nome': 'messi',
    'time': 'miami',
    'idade': 36,
    'estado': 'casadao'

}

print(pessoa)

pessoa1 = [{
    'nome':'neymar',
    'time':'barcelona',
    'idade':30,
    'pronome':'delas',
    'estado': 'online e roteando'
},
{
    'nome': 'messi',
    'time': 'miami',
    'idade': 36,
    'estado': 'casadao'

}]

print(pessoa1[1])


