# 64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.
import random
lista = []
for i in range(10):
    i = random.randint(1,100)

    if i%3 == 0:
        lista.append(i)
        print(i)
    
