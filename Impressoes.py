# ----------------------------- IMPRESSÕES  ----------------------------- #

# Enfeita a matriz
def Enfeita_Matrizes(montagem):

    if montagem == 5:
        print(' ' * 20, '━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━')

    elif montagem == 6:
        print(' ' * 20, '━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━')

    else:
        print(' ' * 20, '━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━')

# Complemento aos enfeites da matriz
def Enfeita_Matrizes_2(montagem):

    if montagem == 5:
        print(' ' * 20, '--------------------------------------------')

    elif montagem == 6:
        print(' ' * 20, '-----------------------------------------------------')

    else:
        print(' ' * 20, '--------------------------------------------------------------')

# Imprime os dados das entradas
def Imprime_Entradas(texto):

    if len(texto) == 1:
        print('\n', "━═" * 16, f'{texto[0]}', "━═" * 16)

    else:
        print("━═" * 17, f'{texto[0]}', "━═" * 17)

        if len(texto) > 3:      # Caso o texto seja dividido por partes, como um menu, é utilizada esse print, pois imprime com as numerações
            # Caso a entrada tenha 3 opções
            print(f'\n[ 1 ] {texto[1]}\n[ 2 ] {texto[2]}\n[ 3 ] {texto[3]}')

        else:
            # Caso a entrada tenha 2 opções
            print(f'\n[ 1 ] {texto[1]}\n[ 2 ] {texto[2]}')

# Imprime os históricos
def Imprime_Historicos(historicos, historicos_LC):

    for i in range(len(historicos)):
        # Pega o primeiro histórico, que é um dicionário
        dicio = historicos[i]

        for chave in dicio:
            if i % 2 == 0:
                print(f'| Chute Jogador 1: {chave} | {historicos_LC[i]} | Compração com a soma: {dicio[chave][0]} |')
            else:
                print(f'| Chute Jogador 2: {chave} | {historicos_LC[i]} | Compração com a soma: {dicio[chave][0]} |')
    print()

# Imprime as matrizes
def Imprime_Matrizes(escolhida, montagem):

    print()
    if montagem == 5:
        print(' ' * 20, ' TABULEIRO DOS JOGADORES  ')
        Enfeita_Matrizes(montagem)

    elif montagem == 6:
        print(' ' * 20, '      TABULEIRO DOS JOGADORES      ')
        Enfeita_Matrizes(montagem)

    else:
        print(' ' * 20, '          TABULEIRO DOS JOGADORES           ')
        Enfeita_Matrizes(montagem)

    for i in range(montagem):
        print(' ' * 20, end=' ')
        for j in range(montagem):
            print(f'| {escolhida[i][j]:^4} |', end=' ')
        print()
        if i < montagem-1:
            Enfeita_Matrizes_2(montagem)

    Enfeita_Matrizes(montagem)

# Imprime os nomes dos jogadores
def Imprime_Nomes(nome):
    print(f'\n\t\t\tNome do jogador: > {nome} < \n')

# Imprime textos dos vencedores
def Imprime_Vencedores(texto):

    print()
    print('━═' * 20)
    print(f'│ {texto:^40}')
    print('━═' * 20)

# Imprime o manual de instruções
def Imprime_Manual():

    texto = [' MANUAL DE INSTRUÇÕES ']

    Imprime_Entradas(texto)

    print('''

    ❏ Precisa-se de dois jogadores para que possa jogar esse jogo;

    ❏ Esse jogo tem três níveis disponíveis para jogar: Fácil, Médio e Difícil;
    
    ❏ Nesse jogo, o jogador terá que escolher uma linha ou uma coluna e adivinhar a soma de todos os
    elementos dessa linha/coluna;
    
    ❏ Os jogadores poderão escolher jogar com um ou dois tabuleiros;
     
        » Caso os jogadores escolham a primeira opção, ambos tentarão adivinhar os valores das somas no
        mesmo tabuleiro;
        » Caso os jogadores escolham a segunda opção, cada um deles terá o seu próprio tabuleiro, cujo os
        elementos e as somas são valores distintos. 
    
    ❏ O vencedor da rodada será aquele que chegar mais próximo do valor da soma;

        » Caso o número que o jogador digitou seja maior do que a soma, é revelada a maior casa;
        » Caso o número que o jogador digitou seja menor do que a soma, é revelada a menor casa;
        » Caso o número que o jogador digitou seja igual a soma, todos os elementos da linha ou coluna
        serão revelados.

    ❏ Ao final do jogo, vence aquele que adivinhar o maior número de casas, ou seja, o que, ao final do 
    jogo, acumular mais pontos.
    

    \t\t\t *:･ﾟ✧*:･ﾟ ⇢ BOM JOGO! ࿐ྂ \n
    ''')
