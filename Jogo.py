# ----------------------------- FUNÇÃO PARA JOGAR  ----------------------------- #

# ------ Importações de minha autoria ------ #

from Funcoes import *
from Impressoes import *

# ----------------------------------------------------------------------------- #


def Joga(historicos, historicos_LC, jogadores, matriz, montagem, nivel, nomes_jogadores, parcial, tabuleiro):

    # Entradas das linhas e das colunas
    retornos = Escolhas_Jogadores(historicos, historicos_LC, matriz, montagem, nivel, nomes_jogadores, parcial, tabuleiro)

    # Colunas de ambos os jogadores (caso o valor seja igual a -1, significa que o jogador não escolheu uma coluna)
    colunas = retornos[0]
    # Linhas de ambos os jogadores (mesma coisa das colunas, caso o valor seja -1)
    linhas = retornos[1]

    # Diferenças entre o chute da soma e o valor correto de ambos os jogadores
    diferencas = retornos[2]

    # Respostas (valores corretos das somas) do jogador 1 e do jogaodr 2
    respostas = retornos[5]

    somas = retornos[6]    # Valores chutados pelo jogador 1 e o jogador 2

    # Escolhe quem marcou ponto na partida
    partidas = Partidas(diferencas, respostas, somas)

    # Escolhe a casa que será revelada
    retornos_escolha_casa = Escolha_Casa(
        diferencas, colunas, jogadores, linhas, matriz, montagem, parcial, partidas, respostas, somas, tabuleiro)

    colunas = retornos_escolha_casa[0]  # Colunas de ambos os jogadores

    linhas = retornos_escolha_casa[0]   # Linhas de ambos os jogadores

    # Caso a quantidade de tabuleiros for igual a 1, há retorno de apenas uma matriz parcial
    if tabuleiro == 1:
        parcial = retornos_escolha_casa[2]

    # Caso a quantidade de tabuleiros for maior que 1, há o retorno de duas matrizes parciais
    else:
        parcial[0] = retornos_escolha_casa[2][0]
        parcial[1] = retornos_escolha_casa[2][1]

    # Impressão do histórico de escolhas dos jogadores
    resp_historico = str(
        input('\n\t>>> Deseja visualizar o histórico? ')).lower().strip()

    if resp_historico == 's' or resp_historico == 'sim':
        texto = [' HISTÓRICO ']
        # Imprime o texto em uma formatação específica
        Imprime_Entradas(texto)
        # Chama a função para imprimir os históricos em uma formatação específica
        Imprime_Historicos(historicos, historicos_LC)

    # Impressões do tabuleiro parcial
    if tabuleiro == 1:

        texto = [' MATRIZ PARCIAL ']
        Imprime_Entradas(texto)

        # Imprime a matriz parcial em uma formatação específica
        Imprime_Matrizes(parcial, montagem)

    # Impressão dos tabuleiros parciais
    else:

        texto = [f' MATRIZ PARCIAL {nomes_jogadores[0]} ']
        Imprime_Entradas(texto)

        # Imprime a primeira matriz parcial
        Imprime_Matrizes(parcial[0], montagem)

        print()

        texto = [f' MATRIZ PARCIAL {nomes_jogadores[1]}']
        Imprime_Entradas(texto)

        # Imprime a segunda matriz parcial
        Imprime_Matrizes(parcial[1], montagem)

    # Impressão do placar parcial
    print('\n ------------------ PLACAR PARCIAL ------------------ ')
    print(' ' * 13, f'| JOGADOR 1: {jogadores[0]} pontos |')
    print(' ' * 13, f'| JOGADOR 2: {jogadores[1]} pontos |')
    print(' ---------------------------------------------------- ', '\n')
