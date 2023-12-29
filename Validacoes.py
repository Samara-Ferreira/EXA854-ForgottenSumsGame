# ----------------------------- VALIDAÇÕES  ----------------------------- #

# Valida as entradas com até duas opções
def Valida_Entradas():

    c = True
    while c == True:

        try:
            variavel = int(input(f'\n\t>>> Digite uma das opções: '))

            while variavel < 1 or variavel > 2:
                print('\n\tNúmero Inválido!\n\tPor favor, digite "1" para a primeira opção e "2" para a segunda.\n')
                variavel = int(input(f'\n\t>>> Digite uma das opções: '))

        except:
            print('\n\tEntrada Inválida!\n\tPor favor, digite "1" para a primeira opção e "2" para a segunda.\n')

        else:
            c = False

    return variavel

# Valida se uma linha ou uma coluna estão preenchidas
def Valida_LC(parcial, montagem, nome_variavel, variavel):

    while variavel < 1 or variavel > montagem-2:
        print(f'\n\tNúmero Inválido!\n\tEssa {nome_variavel} não existe, digite um valor entre 0 e {montagem-1}')
        print(f'\n\t Dica: digite um número de 1 a {montagem-2}!')
        variavel = int(input('\n\t>>> Digite uma opção: '))

    cond = 0

    for i in range(montagem-2):    # Verifica se a linha ainda tem espaços em branco

        if nome_variavel == 'linha':     # Serve para as linhas
            if parcial[variavel][i+1] == '   ':
                cond += 1

        else:                       # Serve para as colunas
            if parcial[i+1][variavel] == '   ':
                cond += 1

    while cond == 0:    # Se essa variável for igual a zero, significa que não tem mais casas para serem reveladas
        print(f'\n\tEssa {nome_variavel} já está preenchida!')

        variavel = int(input('\n\t>>> Digite uma opção: '))

        while variavel < 1 or variavel > montagem-2:
            print(f'\n\tNúmero Inválido!\n\tEssa {nome_variavel} não existe, digite um valor entre 0 e {montagem-1}')
            print(f'\n\t Dica: digite um número de 1 a {montagem-2}!')
            variavel = int(input('\n\t>>> Digite uma opção: '))

        cond = 0

        for i in range(montagem-2):    # Verifica se a linha ainda tem espaços em branco

            if nome_variavel == 'linha':     # Serve para as linhas
                if parcial[variavel][i+1] == '   ':
                    cond += 1

            else:                       # Serve para as colunas
                if parcial[i+1][variavel] == '   ':
                    cond += 1

    return variavel

# Pega o nível escolhido e verifica se é válido
def Valida_Niveis():
    c = True

    while c == True:

        try:
            nivel = int(input('\n\t>>> Digite uma das opções: '))

            while nivel < 1 or nivel > 3:
                print('\n\tNúmero Inválido!\n\tDigite 1, 2, ou 3')
                nivel = int(input('\n\tDigite uma das opções: '))

        except:
            print('\n\tEntrada Inválida!\n\tDigite 1, 2 ou 3')

        else:
            c = False

    return nivel

# Verifica se número de rodadas é válido
def Valida_Rodadas(num, rodadas):

    while (rodadas < 1 or rodadas > num) or rodadas % 2 == 0:
        print(f'\n\tNúmero Inválido!\n\tPor favor, digite um número maior que 0 e menor que {num}')
        rodadas = int(input('\n\t>>> Digite o número de rodadas: '))

    return rodadas

# Verifica se a soma é válida
def Valida_Soma(soma, num1, num2):

    while soma > num2 or soma < num1:
        print(f'\n\tSoma Inválida!\n\tPor favor, digite uma soma entre {num1 - 1} e {num2 + 1}.')

        soma = int(input('\n\t>>> Digite a soma: '))

    return soma
