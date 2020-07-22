def fim():
    f = 'ATE LOGO'
    print('\033[1;30;41m~' * (len(f) + 4))
    print(f'  {f}')
    print('~' * (len(f) + 4))


def sist():
    s = 'SISTEMA DE AJUDA PyHELP'
    print('\033[1;30;42m~' * (len(s)+4))
    print(f'  {s}')
    print('~' * (len(s) + 4))


def acesso():
    a = f'Acessando o manual do comando: {r}'
    print('\033[1;30;44m~' * (len(a) + 4))
    print(f'  {a}')
    print('~' * (len(a) + 4))


def ajuda(msg):
    from time import sleep
    global r
    r = input(msg)
    if r in 'fimFIM':
        return r
    acesso()
    sleep(1)

    return r


while True:
    sist()
    sos = ajuda('\033[mFunção ou Biblioteca> ')
    if sos in 'fimFIM':
        break
    print('\033[m', end='')
    print('\033[7;30m')
    help(sos)
    print('\033[m', end='')
    if sos in 'fimFIM':
        break
fim()
