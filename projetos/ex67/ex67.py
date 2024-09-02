# 67. desenvolve um jogo da velha desenvolvido em python que funcione no terminal

from os import system
import funcoes as jv


system('cls')


jogador = 'X'
vencedor = False

while vencedor == False:
    jv.hud()
    jogada = int(input('onde deseja jogar? '))

    jv.jogar(jogada, jogador)
    jv.hud()


    vencedor = jv.vitoria()
    jogador = jv.troca_jogador(jogador)
    











































































































