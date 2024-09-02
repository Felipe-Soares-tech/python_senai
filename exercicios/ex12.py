# 12. Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.


transporte = input('escolha um meio de transporte entre carro, bicicleta ou a ir a pé: ') 
import random

if transporte == 'carro':
    print(f'a velocidade média deste veiculo é {random.randint(50,100)}km/h')
elif transporte == 'bicicleta':
    print(f'a velocidade média da bicicleta é {random.randint(20,30)}km/h')

elif transporte == 'a pé':
    print(f'a misera velociade média de alguem a pé é de {random.randint(1,10)}km/h')














