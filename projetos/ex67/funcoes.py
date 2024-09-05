from operator import truediv
from os import system


tabuleiro = [0,1,2,3,4,5,6,7,8]


def hud():
    system('cls')
    for posic, num in enumerate(tabuleiro):
        if posic == 2  or posic == 5 or posic == 8:
            print(num)       
        else:
            print(num, end= ' | ')



def jogar(jogada,jogador):
    tabuleiro[jogada] = jogador

def troca_jogador(jogador):
    jog = jogador
    if jog == 'X':
        jog = 'O'
    else:
        jog = 'X'
    return jog

def vitoria():
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or
       tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or
       tabuleiro[6] == tabuleiro[7] == tabuleiro[8]):
       return True
    elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or
         tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or
         tabuleiro[2] == tabuleiro[5] == tabuleiro[8]):
       return True
    elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or
         tabuleiro[2] == tabuleiro[4] == tabuleiro[6]):
       return True
    else:
        return False

def victory():
    tabuleiro = [0,1,2,3,4,5,6,7,8]

    combincoes_vitoria = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in combincoes_vitoria:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return True


































