from time import sleep


def maior(* inteiros):
    cont = list()
    print(f'\nAnalizando os valores passados...')
    for v in inteiros:
        for c in v:
            print(c, end=' ')
            sleep(0.4)
            cont.append(int(c))
        print('.')
    print(f'O maior valor digitado foi {max(cont)}.')


num = list()
while True:
    n = int(input('Digite um valor [999 para encerrar]: '))
    if n == 999:
        break
    num.append(n)

maior(num)
