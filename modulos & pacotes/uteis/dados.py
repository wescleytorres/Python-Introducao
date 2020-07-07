def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Valor inteiro inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu parar!')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Valor inválido!')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu parar!')
            break
        else:
            return n