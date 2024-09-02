
# capitalize muda o primeiro caracter da string pra maiusculo







texto = '   felipe soares siqueira    '

print(texto)

print(texto.capitalize())

# slice manipula string por indice

cidade = 'procurando nemo'

print(cidade[3:5])

#metodos lista

# adiciona mais coisas na lista

lista = ['neymar', 'messi', 'cris','lista']

lista.extend(['penaldo', 'suarez'])

#inserir algo num posição especifica da lista

lista.insert(0,'lista')

print(lista)

# remove, exclui um elemento pelo valor

lista.remove('neymar')
print(lista)

# pop - exclui o ultimo elemento da lista ou o indice informado
lista.pop(4)

print(lista)

# index - retorna o indice da primeira ocorrencia de um valor procurado
print(lista.index('lista'))
#atualizar um elemento da lista
lista[lista.index('messi')] = 'lionel messi'
lista_legal = ['messi']

lista_legal[0] = 'legal'

print(lista_legal)

print(lista)
#contabilizando a quantidade de elementos repetidos

print(lista.count('lista'))

#sort, ordena a lista de forma cresente

num = [2,5,1,9,3]
lista.sort()


players = ['yamal','olmo', 'rodri', 'benzema']
lista.sort()
print(players)

#reverse, reverte a parada toda ai 

num.reverse()
players.reverse()

del players[1]

print(players)




