def leiadin(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)



def metade(num):
    r = num / 2
    return f'{monet(r)}'


def dobro(num):
    r = num * 2
    return f'{monet(r)}'


def aumentar(num, a):
    r = (num * a) / 100
    m = num + r
    return f'{monet(m)}'


def reduzir(num, a):
    r = (num * a) / 100
    m = num - r
    return f'{monet(m)}'


def monet(valor=0, sigla='R$'):
    return f'{sigla} {valor:.2f}'.replace('.', ',')


def resumo(p=0, aum=0, red=0):
    p = float(p)
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{monet(p)}')
    print(f'Dobro do preço: \t{dobro(p)}')
    print(f'Metade do preço: \t{metade(p)}')
    print(f'{aum}% de aumento: \t{aumentar(p,aum)}')
    print(f'{red}% de redução: \t{reduzir(p,red)}')
