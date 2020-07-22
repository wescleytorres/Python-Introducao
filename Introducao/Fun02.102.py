def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorialde um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Digite um valor: '))
while True:
    r = input('Deseja ver a conta do Fatorial? [S/N]: ').upper()
    if r in 'S':
        print(fatorial(n, show=True))
        break
    if r in 'N':
        print(fatorial(n))
        break
    print('ERRO! Favor informar S ou N.')
print('FIM!')
