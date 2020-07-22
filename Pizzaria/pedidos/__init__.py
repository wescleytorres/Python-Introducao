def pizza():
    from time import sleep
    # Biblioteca criada por mim 'fontes': para formatar texto
    import fontes

    # Dicionario dos sabores que tem no cardapio
    sabores = {'Mussarela': 25.00, 'Calabresa': 25.00, 'Carne de Sol': 30.00, 'MODA CASA': 35.00}

    lista_sabores = list()
    lista_principal = list()

    # MENU DO CARDAPIO
    fontes.color(f='negrito', t='white', b='yellow')
    print(f'{"MENU PIZZA".center(52)}\033[m')
    fontes.color(f='negrito', t='yellow')
    print(f'{"COD"}   {"SABORES":<38}   {"PREÇO"}')
    print('-' * 52)
    fontes.color(fim=True)

    # TABELA DE SABORES E PREÇOS
    cont = 0
    for k, v in sabores.items():
        print(f' {cont:<4}{k:.<39}R$ ', end='')
        print(f'{float(v):.2f}'.replace('.', ','))
        cont += 1
        lista_sabores.append(k)
        lista_sabores.append(v)
        lista_principal.append(lista_sabores.copy())
        lista_sabores.clear()

    # LISTA "COMANDA" DOS PEDIDOS: efetuando o pedido
    lista_pedido = list()
    calculo = 0
    while True:
        # caso de digitação errada, sera tratado o erro
        try:
            print('-=' * 26)
            qtde = input('Informe o código da PIZZA que deseja: ')
            lista_pedido.append(lista_principal[int(qtde)][0])
            calculo += float(lista_principal[int(qtde)][1])
        except (ValueError, IndexError):
            fontes.color(f='negrito', t='red')
            print(f'ERRO! COD informado não encontrado, favor informar COD válido!')
            fontes.color(fim=True)
            sleep(1)
            continue
        fontes.color(f='negrito', t='green')
        print('Sabor adicionado com sucesso!')
        fontes.color(fim=True)
        sleep(1)
        print()

        # para sair ou fazer mais um pedido
        while True:
            r = input('Deseja  outro sabor? [S/N]: ')
            if r in 'SsNn':
                break
            fontes.color(f='negrito', t='red')
            print(f'ERRO! Valor inválido. Favor informar N ou S!')
            fontes.color(fim=True)
            sleep(1)
        if r in 'nN':
            break
    print('-=' * 26)

    # IMPRIMIR OS SABORES DO PEDIDO
    fontes.color(f='negrito', t='white', b='blue')
    print(f' Os sabores adicionados foram: ', end='')
    cont = len(lista_pedido)
    for p in lista_pedido:
        print(p, end='')
        if cont > 1:
            print(',', end=' ')
        else:
            print('. \033[m', end='')
        cont -= 1
    print()

    # IMPRIMIR O TOTAL DO PEDIDO
    fontes.color(f='negrito', t='white', b='blue')
    print(f' O Total do seu pedido foi R$ {calculo:.2f} \033[m'.replace('.', ','))
