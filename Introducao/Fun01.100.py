from random import randint
numeros = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for v in lista:
        print(v, end=' ')
    print('PRONTO!')


def somarpar(lista):
    cont = 0
    for v in lista:
        if v % 2 == 0:
            cont += v
    print(f'Somando os valores pares de {numeros}, temos {cont}')


sorteia(numeros)
somarpar(numeros)
