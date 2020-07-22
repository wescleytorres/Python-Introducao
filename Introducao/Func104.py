def leiaInt(num):
    while True:
        f = input(num)
        if f.isnumeric():
            f = int(f)
            break
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return f


n = leiaInt('Digite um número: ')
print(f'\033[34mVocê acabou de digitar o número: {n}\033[m')
