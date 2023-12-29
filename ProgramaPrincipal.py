'''
Autor: Sanara dos Santos Ferreira
Componente Curricular: MI - Algoritmos e Programação I
Concluido em: 21/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''

# ----------------------------- PROGRAMA PRINCIPAL  ----------------------------- #

# ------ Importações com autoria de terceiros ------ #

from time import sleep  # Suspense a execução do código por determinado tempo
# Código fonte: https://github.com/python/cpython/blob/main/Modules/timemodule.c


# ------ Importações de minha autoria ------ #

# Importa arquivos das funções gerais e da função que roda o jogo
from Funcoes import *   # Funções gerais
from Jogo import Joga   # Corpo do jogo

# ------------------------------------------------------------------------------ #

# ------ Impressões Iniciais do Jogo ------ #

print(f'''
▄▀▄▀▄▀
                ▄▀▀▀▀   ▄▀▀▀▀▄  █▄▄ ▄▄█  ▄▀▀▀▄  ▄▀▀▀▀ 
                ▀▄▄▄▄   █    █  █  ▀  █  █▄▄▄█  ▀▄▄▄▄ 
                     █  █    █  █     █  █   █       █
                ▀▀▀▀▀    ▀▀▀▀   ▀     ▀  ▀   ▀  ▀▀▀▀▀  

█▀▀▀▀  ▄▀▀▀▀   ▄▀▀▀▀▀▄  █    █  █▀▀▀▀  ▄▀▀▀▀   ▄▀▀▀▀▀▄  ▀█▀  █▀▀▀▀▄  ▄▀▀▀▄  ▄▀▀▀▀
█▄▄▄   ▀▄▄▄▄   █     █  █    █  █▄▄▄   ▀▄▄▄▄   █         █   █    █  █▄▄▄█  ▀▄▄▄▄
█           █  █   ▄ █  █    █  █           █  █     ▄   █   █    █  █   █       █
▀▀▀▀▀  ▀▀▀▀▀    ▀▀▀▀▀▄   ▀▀▀▀   ▀▀▀▀▀  ▀▀▀▀▀    ▀▀▀▀▀   ▀▀▀  ▀▀▀▀▀   ▀   ▀  ▀▀▀▀▀
                                                                                        ▀▄▀▄▀▄
''')

print('\t\t\t\t    ███████▒▒▒\n')

print('\t\t\t\tCarregando o jogo...\n')

sleep(1)


# ------ Entrada dos Dados ------ #

# Nomes dos jogadores
texto = [' NOMES DOS JOGADORES ']
Imprime_Entradas(texto)   # Imprime os textos na formatação desejada
# O mesmo se aplica aos tabuleiros, níveis e términos

nomes_jogadores = []    # Guarda os nomes dos jogadores

for i in range(2):  # Entrada dos nomes dos jogadores (um por vez))
    nome = Nomes_Jogadores()
    Imprime_Nomes(nome)
    nomes_jogadores.append(nome)

    sleep(0.1)


# Visualização do manual de instruções
resp_manual = str(input(
    '\n\t>>> Deseja consultar o manual antes de inciar o jogo?  ')).strip().lower()

if resp_manual == 's' or resp_manual == 'sim':
    Imprime_Manual()


print('\n\t\t\t\t\tVamos iniciar o jogo...\n')

sleep(0.2)


# Quantidade de tabuleiros
texto = [' QUANTIDADE DE TABULEIROS ', ' Um Tabuleiro', ' Dois Tabuleiros']
Imprime_Entradas(texto)
# Valida as entradas. O mesmo se aplica a função "Valida_Nívieis" e "Valida_Entadas", na parte de finalização
tabuleiro = Valida_Entradas()
# Não são aceitos números menores que um ou maiores que dois

print(f'\n\t\t> Quantidade de tabuleiros escolhida: {tabuleiro}\n')

sleep(0.2)


# Níveis
texto = [' NÍVEIS ', ' Nível Fácil ', ' Nível Médio ', ' Nível Difícil ']
Imprime_Entradas(texto)
# Mesma funcionalidade que a enterior, porém essa há três opções de entradas (três níveis))
nivel = Valida_Niveis()

print(f'\n\t\t> Nível escolhido: {nivel}\n')

sleep(0.2)


# Forma de finalização do jogo
texto = [' TÉRMINO ', ' Número de Rodadas ', ' Tabuleiro Completo ']
Imprime_Entradas(texto)
finalizacao = Valida_Entradas()

if finalizacao == 1:
    # Finaliza com um número de rodadas. Função chamada para que o usuário digite o número de rodadas que deseja e o valide
    rodadas = Rodadas(nivel, tabuleiro)
    print(f'\n\t\t> O jogo irá finalizar quando a quantidade de rodadas ({rodadas}) acabar!\n')

else:   # Jogo termina quando um dos tabuleiros estiver completo
    if tabuleiro == 1:
        print(f'\n\t\t> O jogo irá finalizar quando todas as casas do tabuleiro forem reveladas!\n')
    else:
        print(f'\n\t\t> O jogo irá finalizar quando todas as casas de pelo menos um tabuleiro forem reveladas!\n')

sleep(0.2)


# Um tabuleiro
if tabuleiro == 1:
    # Escolhe variáveis de contagem e monragem do jogo, de acordo com o nível
    dados_tabuleiros = Dados_Tabuleiros(nivel)

    # Define intervalo dos números pseudoalatórios
    contagem = dados_tabuleiros[0]
    montagem = dados_tabuleiros[1]  # Define tamanho da matriz

    matriz = Monta_Matrizes(contagem, montagem)  # Monta uma matriz zerada
    matriz = Somas_LC(matriz, montagem)    # Soma os elementos das linhas/coluna e coloca essa soma em uma casa nas extremidades da matr\
    parcial = Monta_Parciais(montagem)  # Monta matrizes parciais (com as casas vazias)


# Dois tabuleiros
else:
    # Mesmas funcionalidades do que foi explicado acima
    dados_tabuleiros = Dados_Tabuleiros(nivel)

    contagem = dados_tabuleiros[0]
    montagem = dados_tabuleiros[1]

    # Dados da primeira matriz
    matriz_1 = Monta_Matrizes(contagem, montagem)
    matriz_1 = Somas_LC(matriz_1, montagem)
    parcial_1 = Monta_Parciais(montagem)

    # Dados da segunda matirz
    matriz_2 = Monta_Matrizes(contagem, montagem)
    matriz_2 = Somas_LC(matriz_2, montagem)
    parcial_2 = Monta_Parciais(montagem)


historicos = []     # Históricos gerais: soma, menor/maior que a soma
historicos_LC = []   # Linhas e colunas escolhidas pelos jogadores

jogadores = [0, 0]


c = 0

# ------ Início do Jogo ------ #

if tabuleiro == 1:

    if finalizacao == 1:    # Finaliza com um número de rodadas definido

        # Enquanto o número de rodadas for maior que zero, o jogo continua rodando
        while rodadas > 0:

            Joga(historicos, historicos_LC, jogadores, matriz, montagem, nivel, nomes_jogadores, parcial, tabuleiro)

            rodadas -= 1

            print(' ' * 20, f'Número de rodadas restantes: {rodadas}')

        # Imprime o vencedor da rodada ou empate, caso a pontuação dos dois seja a mesma
        Organiza_Vencedores(jogadores, nomes_jogadores)

    else:   # Finaliza quando todas as casas forem reveladas

        cont = 0
        while cont >= 0:

            Joga(historicos, historicos_LC, jogadores, matriz, montagem, nivel, nomes_jogadores, parcial, tabuleiro)

            cont = -1

            # Procura na matriz se tem somente zeros ou se é preenchidas com outros números
            for x in range(montagem-2):
                for y in range(montagem-2):

                    if matriz[x+1][y+1] != 0:
                        cont += 1

        Organiza_Vencedores(jogadores, nomes_jogadores)


else:

    matrizes = [matriz_1, matriz_2]
    parciais = [parcial_1, parcial_2]

    if finalizacao == 1:    # Finaliza com um número de rodadas definido

        while rodadas > 0:

            Joga(historicos, historicos_LC, jogadores, matrizes, montagem, nivel, nomes_jogadores, parciais, tabuleiro)

            rodadas -= 1

            # Caso as casas de um dos tabuleiros já estejam todas reveladas, o jogo termina, mesmo que o número de rodadas restantes não seja igual a zero
            cont1 = Percorre_Matriz(montagem, parcial_1)
            cont2 = Percorre_Matriz(montagem, parcial_2)

            if cont1 == 0 or cont2 == 0:
                rodadas = 0

            print(' ' * 20, f'Número de rodadas restantes: {rodadas}')

        Organiza_Vencedores(jogadores, nomes_jogadores)

    else:    # Finaliza quando todas as casas de pelo menos um dos tabuleiros forem reveladas

        c = True

        while c == True:

            Joga(historicos, historicos_LC, jogadores, matrizes, montagem, nivel, nomes_jogadores, parciais, tabuleiro)

            cont1 = Percorre_Matriz(montagem, parcial_1)
            cont2 = Percorre_Matriz(montagem, parcial_2)

            if cont1 == 0 or cont2 == 0:
                c = False

        Organiza_Vencedores(jogadores, nomes_jogadores)
