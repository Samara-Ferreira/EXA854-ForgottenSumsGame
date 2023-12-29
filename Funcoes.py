# ----------------------------- FUNÇÕES GERAIS  ----------------------------- #

# ------ Importações de minha autoria ------ #

from Impressoes import *
from Validacoes import *


# ------ Importações com autorida de terceiros ------ #

from random import randint  # Números pseudoaleatórios
# Código fonte: https://github.com/python/cpython/tree/3.10/Lib/random.py

from time import sleep  # Suspense a execução do código por determinado tempo
# Código fonte: https://github.com/python/cpython/blob/main/Modules/timemodule.c

# ----------------------------------------------------------------------------- #

# Escolhe as casas que serão reveladas
def Escolha_Casa(diferencas, colunas, jogadores, linhas, matriz, montagem, parcial, partidas, respostas, somas, tabuleiro):

    if partidas[0] > partidas[1]:   # Caso a pontuação do jogador 1 for maior que a do jogador 2
        if tabuleiro == 1:

            # Escolhe casa que será revelada na partida
            retornos = Partida_Casa(colunas[0], diferencas, jogadores[0],
                                    linhas[0], matriz, montagem, parcial, respostas[0], somas[0])

            parcial = retornos[0]
            jogadores[0] = retornos[1]

        else:
            # Mesma função da anterior
            retornos = Partida_Casa(colunas[0], diferencas, jogadores[0], linhas[0],
                                    matriz[0], montagem, parcial[0], respostas[0], somas[0])

            parcial[0] = retornos[0]
            jogadores[0] = retornos[1]

    # Caso a pontuação do jogador 2 for maior que a do jogador 1
    elif partidas[0] < partidas[1]:

        diferencas = [diferencas[1], diferencas[0]]

        if tabuleiro == 1:
            retornos = Partida_Casa(colunas[1], diferencas, jogadores[1], linhas[1], matriz, montagem, parcial, respostas[1], somas[1])

            parcial = retornos[0]
            jogadores[1] = retornos[1]

        else:
            retornos = Partida_Casa(colunas[1], diferencas, jogadores[1], linhas[1], matriz[1], montagem, parcial[1], respostas[1], somas[1])

            parcial[1] = retornos[0]
            jogadores[1] = retornos[1]

    else:   # Caso a pontuação do jogador 1 e do jogador 2 forem iguais

        # Caso tenham escolhido a mesma linha ou coluna em um mesmo tabuleiro, a resposta é igual e apenas uma casa é revelada
        if tabuleiro == 1 and (linhas[0] == linhas[1]):
            retornos = Partida_Casa(colunas[0], diferencas, jogadores, linhas[0], matriz, montagem, parcial, respostas[0], somas[0])

            parcial = retornos[0]
            jogadores = retornos[1]

        elif tabuleiro == 1 and (colunas[0] == colunas[1]):
            retornos = Partida_Casa(colunas[0], diferencas, jogadores, linhas[0], matriz, montagem, parcial, respostas[0], somas[0])

            parcial = retornos[0]
            jogadores = retornos[1]

        else:

            if tabuleiro == 1:
                retornos = Partida_Casa(colunas[0], diferencas, jogadores[0], linhas[0], matriz, montagem, parcial, respostas[0], somas[0])

                parcial = retornos[0]
                jogadores[0] = retornos[1]

                diferencas = [diferencas[1], diferencas[0]]
                retornos = Partida_Casa(colunas[1], diferencas, jogadores[1], linhas[1], matriz, montagem, parcial, respostas[1], somas[1])

                parcial = retornos[0]
                jogadores[1] = retornos[1]

            else:
                retornos = Partida_Casa(colunas[0], diferencas, jogadores[0], linhas[0], matriz[0], montagem, parcial[0], respostas[0], somas[0])

                parcial[0] = retornos[0]
                jogadores[0] = retornos[1]

                diferencas = [diferencas[1], diferencas[0]]
                retornos = Partida_Casa(colunas[1], diferencas, jogadores[1], linhas[1], matriz[1], montagem, parcial[1], respostas[1], somas[1])

                parcial[1] = retornos[0]
                jogadores[1] = retornos[1]

    return (colunas, linhas, parcial)

# Escolhe se a casa a ser revelada é a maior, a menor ou todas de uma linha ou coluna
def Escolhe_Casas(diferencas, variavel, resposta, soma):

    maior = -1
    menor = -1
    toda = -1

    if diferencas[0] <= diferencas[1]:

        if soma > resposta:
            maior = variavel

        elif soma < resposta:
            menor = variavel

        else:
            toda = variavel

    return (maior, menor, toda)

# Separa as principais escolhas dos jogadores
def Escolhas_Jogadores(historicos, historicos_LC, matriz, montagem, nivel, nomes_jogadores, parcial, tabuleiro):

    # Duas rodadas, uma para cada jogador fazer as suas escolhas
    for c in range(2):

        # Impressão dos nomes dos jogadores em cada rodada
        if c == 0:
            Imprime_Nomes(nomes_jogadores[0])

        else:
            Imprime_Nomes(nomes_jogadores[1])

        # Imprime os textos em uma formatação específica
        texto = [' LINHAS E COLUNAS ', ' Linhas ', ' Colunas ']
        Imprime_Entradas(texto)

        # Escolha: linha ou coluna
        escolha = Valida_Entradas()

        # Separação dos dados em variáveis
        if tabuleiro == 1:
            # Entradas das linhas, soma e organização dos históricos
            retornos_organiza = Organiza_Escolhas(escolha, historicos, historicos_LC, matriz, montagem, nivel, parcial)

            if c == 0:

                historicos = retornos_organiza[0]

                historicos_LC = retornos_organiza[1]

                linha_1 = retornos_organiza[2][0]
                coluna_1 = retornos_organiza[2][1]

                diferenca_1 = retornos_organiza[3][0]
                resposta_1 = retornos_organiza[3][1]

                soma_1 = retornos_organiza[4]

            else:

                historicos = retornos_organiza[0]

                historicos_LC = retornos_organiza[1]

                linha_2 = retornos_organiza[2][0]
                coluna_2 = retornos_organiza[2][1]

                diferenca_2 = retornos_organiza[3][0]
                resposta_2 = retornos_organiza[3][1]

                soma_2 = retornos_organiza[4]

        else:

            if c == 0:
                # Mesma funcionalidade da anterior, mas agora é somente para a primeira matriz
                retornos_organiza = Organiza_Escolhas(escolha, historicos, historicos_LC, matriz[0], montagem, nivel, parcial[0])

                historicos = retornos_organiza[0]

                historicos_LC = retornos_organiza[1]

                linha_1 = retornos_organiza[2][0]
                coluna_1 = retornos_organiza[2][1]

                diferenca_1 = retornos_organiza[3][0]
                resposta_1 = retornos_organiza[3][1]

                soma_1 = retornos_organiza[4]

            else:
                # Mesma coisa das anteriores, mas agora é para a segunda matriz
                retornos_organiza = Organiza_Escolhas(escolha, historicos, historicos_LC, matriz[1], montagem, nivel, parcial[1])

                historicos = retornos_organiza[0]

                historicos_LC = retornos_organiza[1]

                linha_2 = retornos_organiza[2][0]
                coluna_2 = retornos_organiza[2][1]

                diferenca_2 = retornos_organiza[3][0]
                resposta_2 = retornos_organiza[3][1]

                soma_2 = retornos_organiza[4]

    # Organização das variáveis em listas para retornar
    colunas = [coluna_1, coluna_2]
    linhas = [linha_1, linha_2]
    diferencas = [diferenca_1, diferenca_2]
    respostas = [resposta_1, resposta_2]
    somas = [soma_1, soma_2]

    return [colunas, linhas, diferencas, historicos, historicos_LC, respostas, somas]

# Separa os dados necessários para a construção do tabuleiro
def Dados_Tabuleiros(nivel):

    if nivel == 1:
        montagem = 5    # Valor mais elevado, pois além da matriz em si, têm também as partes que indica as linhas/colunas e a reservada para a soma
        contagem = 30   # Intervalo dos números pseudoaleatórios. O mesmo vale para os demais, que indicam 60 e 100

    elif nivel == 2:
        montagem = 6    # Mesma coisa da anterior
        contagem = 60

    else:
        montagem = 7    # Mesma coisa da anterior
        contagem = 100

    return (contagem, montagem)

# Guarda o histórico de cada rodada
def Historico(diferenca, resposta, soma):

    temporario = {}

    if soma < resposta:
        temporario[soma] = ['Menor', diferenca]

    elif soma > resposta:
        temporario[soma] = ['Maior', diferenca]

    else:
        temporario[soma] = ['Igual', diferenca]

    return temporario

# Verifica as entradas das linhas e das colunas
def Linha_Coluna(escolha, montagem, parcial):

    linha = -1
    coluna = -1

    c = True

    while c == True:

        try:

            # Caso o jogador escolha uma linha
            if escolha == 1:
                print(f'\n\t Dica: digite um número de 1 a {montagem-2}!')
                linha = int(input('\n\t>>> Digite uma opção: '))

                nome = 'linha'
                # Verifica se a linha é um valor válido e também se já não está preenchida
                linha = Valida_LC(parcial, montagem, nome, linha)

                # A linha não pode ser um valor menor que 1 e nem maior do que a montagem - 2 (retira as partes reservadas à identificação das linhas/colunas e às somas)
                while linha < 1 or linha > montagem-2:
                    print(f'\n\tNúmero Inválido!\n\tEssa linha não existe, digite um valor entre 0 e {montagem-1}')
                    print(f'\n\t Dica: digite um número de 1 a {montagem-2}!')
                    linha = int(input('\n\t>>> Digite uma opção: '))

            else:
                # Mesmas lógica usada na linha
                print(f'\n\t Dica: digite um número de 1 a {montagem-2}!')
                coluna = int(input('\n\t>>> Digite uma opção: '))

                nome = 'coluna'
                coluna = Valida_LC(parcial, montagem, nome, coluna)

                while coluna < 1 or coluna > montagem-2:
                    print(f'\n\tNúmero Inválido!\n\tEssa coluna não existe, digite uma valor entre 0 e {montagem-1}')
                    print(f'\n\t Dica: digite um número de 1 a {montagem-2}!')
                    coluna = int(input('\n\t>>> Digite uma opção: '))

        except:
            print('\n\tNúmero Inválido! Tente novamente')

        else:
            c = False

    return (linha, coluna)

# Monta as matrizes
def Monta_Matrizes(contagem, montagem):

    # Pega uma matriz vazia, de acordo com o tamanho escolhido
    matriz_vazia = Monta_Vazia(montagem)

    for i in range(montagem-2):
        for j in range(montagem-2):
            # Escolhe o número pseudoaleatório, verificando se ele já está na matriz
            numero = Numero_Aleatorio(contagem, matriz_vazia, montagem)

            matriz_vazia[i+1][j+1] = numero

    return matriz_vazia

# Monta matrizes parciais
def Monta_Parciais(montagem):

    if montagem == 5:
        parcial = [['   ', 'C1', 'C2', 'C3', 'SOMA'], ['L1', '   ', '   ', '   ', '   '], ['L2', '   ', '   ', '   ', '   '], ['L3', '   ', '   ', '   ', '   '], ['SOMA', '   ', '   ', '   ', '   ']]

    elif montagem == 6:
        parcial = [['   ', 'C1', 'C2', 'C3', 'C4', 'SOMA'], ['L1', '   ', '   ', '   ', '   ', '   '], ['L2', '   ', '   ', '   ', '   ', '   '], ['L3', '   ', '   ', '   ', '   ', '   '], ['L4', '   ', '   ', '   ', '   ', '   '], ['SOMA', '   ', '   ', '   ', '   ', '   ']]

    else:
        parcial = [['   ', 'C1', 'C2', 'C3', 'C4', 'C5', 'SOMA'], ['L1', '   ', '   ', '   ', '   ', '   ', '   '], ['L2', '   ', '   ', '   ', '   ', '   ', '   '], ['L3', '   ', '   ', '   ', '   ', '   ', '   '], ['L4', '   ', '   ', '   ', '   ', '   ', '   '], ['L5', '   ', '   ', '   ', '   ', '   ', '   '], ['SOMA', '   ', '   ', '   ', '   ', '   ', '   ']]

    return parcial

# Monta matrizes vazias
def Monta_Vazia(montagem):

    if montagem == 5:
        matriz_vazia = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    elif montagem == 6:
        matriz_vazia = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    else:
        matriz_vazia = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    return matriz_vazia

# Gera números pseudoaleatórios
def Numero_Aleatorio(contagem, matriz_vazia, montagem):

    numero_aleatorio = randint(1, contagem)
    c = 1

    while c > 0:
        c -= 1

        for x in range(montagem-2):  # Não pode repetir os números
            for y in range(montagem-2):

                # Esse +1 serve para não pegar as linhas/colunas destinadas as somas e as indicações
                if numero_aleatorio == matriz_vazia[x+1][y+1]:
                    numero_aleatorio = randint(1, contagem)
                    c += 1

    return numero_aleatorio

# Nomes dos jogadores
def Nomes_Jogadores():

    c = True

    while c == True:
        try:
            nome = str(input(f'\n\t>>> Digite o nome do jogador: ')).strip().upper()

            while nome.isalpha() == False:    # Somente letras do alfabeto
                print('\n\tNome inválido!\n\tPor favor, tente novamente.\n')
                nome = str(input(f'\n\t>>> Digite o nome do jogador: ')).strip().upper()

        except:
            print('\n\tNome inválido!\n\tPor favor, tente novamente.')

        else:
            c = False

    return nome

# Escolhe as linhas/colunas e somas. Organiza os demais dados de acordo com essas respostas
def Organiza_Escolhas(escolha, historicos, historicos_LC, matriz, montagem, nivel, parcial):

    # Recebe a linha/coluna digitada pelo usuário e verifica se ela é válida
    linha_coluna = Linha_Coluna(escolha, montagem, parcial)

    # Recebe soma do usuário e verifica se ela é válida
    soma = Soma(nivel)

    # Retorna a resposta (valor da soma correta) e a diferenca entre o chute e a soma
    retornos = Soma_Tabuleiro(linha_coluna[1], linha_coluna[0], matriz, montagem, soma)

    historicos = Organiza_Historicos(
        retornos[0], historicos, retornos[1], soma)

    historicos_LC = Organiza_Historico_LC(linha_coluna, historicos_LC)

    return (historicos, historicos_LC, linha_coluna, retornos, soma)

# Organiza o histórico com a soma e a omparação dessa com o resultado (soma correta)
def Organiza_Historicos(diferenca, historicos, resposta, soma):

    historico_retorno = Historico(diferenca, resposta, soma)

    historicos.append(historico_retorno)

    return historicos

# Organiza o histórico das linhas e das colunas
def Organiza_Historico_LC(linha_coluna, historicos_LC):

    if linha_coluna[0] >= 0:
        variavel = f'Linha: {linha_coluna[0]} '
        historicos_LC.append(variavel)

    else:
        variavel = f'Coluna: {linha_coluna[1]}'
        historicos_LC.append(variavel)

    return historicos_LC

# Escolhe o resultado do jogo e retorna o texto para ser impresso no programa principal
def Organiza_Vencedores(jogadores, nomes_jogadores):

    # Caso a pontuação do jogador 1 seja maior que a do jogador 2
    if jogadores[0] > jogadores[1]:
        texto = f' PARABÉNS, {nomes_jogadores[0]} '

    elif jogadores[0] < jogadores[1]:   # Contrário da última opção
        texto = f' PARABÉNS, {nomes_jogadores[1]} '

    else:   # Caso as pontuações sejam iguais
        texto = ' EMPATE '

    Imprime_Vencedores(texto)

# Escolhe o vencedor de cada partida
    # Essa função não é para o placar parcial, e sim para decidir qual dos jogadores terá uma casa revelada
def Partidas(diferencas, respostas, somas):

    p1 = 0
    p2 = 0

    if diferencas[0] == diferencas[1]:
        p1 += 1
        p2 += 1

    elif (respostas[0] == somas[0]) and (respostas[1] == somas[1]):
        p1 += 1
        p2 += 1

    elif diferencas[0] < diferencas[1] or respostas[0] == somas[0]:
        p1 += 1

    elif diferencas[1] < diferencas[0] or respostas[1] == somas[1]:
        p2 += 1

    return (p1, p2)

# Chama função para escolher a casa que será revelada
def Partida_Casa(coluna, diferencas, jogador, linha, matriz, montagem, parcial, resposta, soma):

    if linha >= 0:
        casa = Escolhe_Casas(diferencas, linha, resposta, soma)

        retornos = Revela_Casas(casa, jogador, linha, matriz, montagem, parcial)

    else:
        casa = Escolhe_Casas(diferencas, coluna, resposta, soma)

        retornos = Revela_Casas(casa, jogador, linha, matriz, montagem, parcial)

    return retornos

# Percorre matrizes para verificar se existe casas vazias
def Percorre_Matriz(montagem, parcial):

    cont = 0

    # Procura números diferentes de 0 na matriz do segundo tabuleiro
    for x in range(montagem-2):
        for y in range(montagem-2):

            if parcial[x+1][y+1] == '   ':
                cont += 1

    return cont

# Revela as somas das linhas ou colunas
def Revela_Somas(matriz, montagem, parcial):

    for i in range(montagem-2):
        soma_linha = 0
        soma_coluna = 0
        for j in range(montagem-2):
            soma_linha += matriz[i+1][j+1]
            soma_coluna += matriz[j+1][i+1]

        if soma_linha == 0:
            parcial[i+1][montagem-1] = matriz[i+1][montagem-1]

        if soma_coluna == 0:
            parcial[montagem-1][i+1] = matriz[montagem-1][i+1]

    return parcial

# Revela as casas dos tabuleiros
def Revela_Casas(casa, jogadores, linha, matriz, montagem, parcial):

    pos1 = 0
    pos2 = 0

    maior = casa[0]
    menor = casa[1]
    toda = casa[2]

    if menor >= 0:      # Caso tenha que pegar o menor valor, a variável utilizada como resposta terá o maior valor possível
        resposta = 150
    else:               # Caso tenha que pegar o maior valor, a variável utilizada como resposta terá zero
        resposta = 0

    # Percorre os elementos das colunas e linhas procurando pelo maior, menor, ou todos os elemnentos da linha/coluna que serão revelados
    for i in range(montagem-2):

        if toda >= 0:
            for j in range(montagem-2):

                if toda == i+1:

                    if linha >= 0:

                        if matriz[i+1][j+1] != 0:
                            parcial[i+1][j+1] = matriz[i+1][j+1]
                            matriz[i+1][j+1] = 0

                            # Se for apenas um vencedor, jogadores não deve vir como uma lista
                            if type(jogadores) is not list:
                                jogadores += 1

                            else:                   # Se forem dois vencedores, jogadores vem como uma lista
                                jogadores[0] += 1
                                jogadores[1] += 1

                    else:

                        if matriz[j+1][i+1] != 0:
                            parcial[j+1][i+1] = matriz[j+1][i+1]
                            matriz[j+1][i+1] = 0

                            # Se for apenas um vencedor, jogadores não deve vir como uma lista
                            if type(jogadores) is not list:
                                jogadores += 1

                            else:                   # Se forem dois vencedores, jogadores vem como uma lista
                                jogadores[0] += 1
                                jogadores[1] += 1

        elif maior >= 0:

            for j in range(montagem-2):
                if maior == i+1:

                    if linha >= 0:

                        if matriz[i+1][j+1] > resposta and matriz[i+1][j+1] != 0:
                            resposta = matriz[i+1][j+1]
                            pos1 = i+1
                            pos2 = j+1

                    else:
                        if matriz[j+1][i+1] > resposta and matriz[j+1][i+1] != 0:
                            resposta = matriz[j+1][i+1]
                            pos1 = j+1
                            pos2 = i+1

        else:

            for j in range(montagem-2):
                if menor == i+1:

                    if linha >= 0:
                        if matriz[i+1][j+1] < resposta and matriz[i+1][j+1] != 0:
                            resposta = matriz[i+1][j+1]
                            pos1 = i+1
                            pos2 = j+1

                    else:
                        if matriz[j+1][i+1] < resposta and matriz[j+1][i+1] != 0:
                            resposta = matriz[j+1][i+1]
                            pos1 = j+1
                            pos2 = i+1

    if toda <= 0:

        # Substituição da casa vazia pelo número correspondente
        parcial[pos1][pos2] = resposta
        matriz[pos1][pos2] = 0

        if type(jogadores) is not list:
            jogadores += 1

        else:
            jogadores[0] += 1
            jogadores[1] += 1

    # Revelar a soma das linhas ou colunas, caso já estejam preenchidas
    parcial = Revela_Somas(matriz, montagem, parcial)

    return (parcial, jogadores)

# Pega o número de rodadas e verifica se é válido
def Rodadas(nivel, tabuleiro):

    c = True
    while c == True:

        try:
            rodadas = int(input('\n\t>>> Digite o número de rodadas: '))

            # Caso o jogo tenha apenas um tabuleiro, tem essas validações de acordo com o nível que o usuário escolher
            if tabuleiro == 1:

                if nivel == 1:
                    num = 9
                elif nivel == 2:
                    num = 16
                else:
                    num = 25

            # Caso o jogo tenha dois tabuleiros
            else:

                if nivel == 1:
                    num = 18
                elif nivel == 2:
                    num = 32
                else:
                    num = 50

            rodadas = Valida_Rodadas(num, rodadas)

        except:
            print('\n\tEntrada Inválida! Por favor, tente novamente.')

        else:
            c = False

    return rodadas

# Verifica se as somas são válidas
def Soma(nivel):

    c = True
    while c == True:

        try:
            soma = int(input('\n\t>>> Digite a soma: '))

            if nivel == 1:
                num1 = 6
                num2 = 87

            elif nivel == 2:
                num1 = 10
                num2 = 234

            else:
                num1 = 15
                num2 = 490

            # Chama a função que irá fazer essa validação, após ter separado todos os dados necessários
            soma = Valida_Soma(soma, num1, num2)

        except:
            print('\n\tSoma Inválida! Tente novamente')

        else:
            c = False

    return soma

# Soma os valores das elementos das linhas e das colunas
def Somas_LC(matriz, montagem):

    soma_linha = []
    soma_coluna = []

    for i in range(montagem-2):
        linha = 0
        coluna = 0

        for j in range(montagem-2):
            # Todos os elementos da linha são somados e armazenados nessa variável
            linha += matriz[i+1][j+1]
            # Mesma coisa do que foi dito acima, porém se aplica às colunas
            coluna += matriz[j+1][i+1]

        # A soma daquela linha é armazenada em uma lista
        soma_linha.append(linha)
        # Mesma coisa do que foi dito acima, porém se aplica às colunas
        soma_coluna.append(coluna)

    # Colocando as somas em seus locais
    for y in range(montagem-2):
        matriz[y+1][montagem-1] = soma_linha[y]
        matriz[montagem-1][y+1] = soma_coluna[y]

    return matriz

# Faz as somas das linhas e colunas e retorna o resultado (soma correta) e a diferença entre o resultado e a soma
def Soma_Tabuleiro(coluna, linha, matriz, montagem, soma):

    for i in range(montagem):
        for j in range(montagem):

            if linha >= 0:  # Caso o usuário tenha escolhido uma linha
                resposta = matriz[linha][montagem-1]

            else:   # Caso o usuário tenha escolhido uma coluna
                resposta = matriz[montagem-1][coluna]

            if resposta > soma:
                diferenca = resposta - soma

            elif resposta < soma:
                diferenca = soma - resposta

            else:
                diferenca = 0

    return (diferenca, resposta)
