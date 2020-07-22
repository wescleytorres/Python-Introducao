from time import sleep


def lin():
    print('-=' * 20)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.4)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.4)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
contador(i=int(input('Inicio: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))
lin()
