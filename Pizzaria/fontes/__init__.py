# deixar o menu bonitinho
def menu(msg):
    r = msg
    print('-' * 52)
    print(f'{r}'.center(52))
    print('-' * 52)


# função para dar cores
def color(f='', t='', b='', fim=False):
    fonte = {'negrito': 1, 'sublinhado': 4, "Negativo": 7}

    texto = {'white': 30, 'red': 31, 'green': 32, 'yellow': 33,
             'blue': 34, 'purple': 35, 'anil': 36, 'gray': 37}

    back = {'white': 40, 'red': 41, 'green': 42, 'yellow': 43,
            'blue': 44, 'purple': 45, 'anil': 46, 'gray': 47}
    c1 = f
    c2 = t
    c3 = b

    if fim:
        print('\033[m', end='')
    else:
        if c1.isalpha():
            for k, v in fonte.items():
                if c1 == k:
                    c1 = v

        if c2.isalpha():
            for k, v in texto.items():
                if c2 == k:
                    c2 = v

        if c3.isalpha():
            for k, v in back.items():
                if c3 == k:
                    c3 = str(v)

        if c3.isalnum():
            print(f'\033[{c1};{c2};{c3}m', end='')
        else:
            print(f'\033[{c1};{c2}m', end='')
