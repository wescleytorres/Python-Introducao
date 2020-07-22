def pizza():
    import fontes
    sabores = {'Mussarela': 25.00, 'Calabresa': 25.00, 'MODA CASA': 35.00}
    lista_sabores = list()
    lista_precos = list()
    fontes.color(f='negrito', t='white', b='yellow')
    print(f'{"MENU PIZZA".center(52)}\033[m')
    cont = 0
    fontes.color(f='negrito', t='yellow')
    print(f'{"COD"}   {"SABORES":<38}   {"PREÇO"}')
    print('-' * 52)
    fontes.color(fim=True)
    for k, v in sabores.items():
        lista_sabores.append(k)
        lista_precos.append(float(v))
        print(f' {cont:<4}{k:.<39}R$ ', end='')
        print(f'{float(v):.2f}'.replace('.', ','))
        cont += 1
    n = int(input('Digite: '))
    return f'{lista_sabores[n]} {lista_precos[n]:.2f}'.replace('.', ',')
