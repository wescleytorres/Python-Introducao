matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    print(f"{l + 1:>10}ª LINHA:")
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da matriz [{l+1},{c+1}]: '))
print()
print('*'*40)
print(f'{"MATRIZ":^40}')
print('*'*40)

print(f'\n\033[1;30;45m{1:>6}{2:>6}{3:>6}    \033[m')
for l in range(0, 3):
    print(f'\033[1;30;45m {l + 1} \033[m', end='')
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
print()

print('*'*40)
print(f'{"SOMA ENTRE COLUNAS":^40}')
print('*'*40)
print()
print(f'O soma entre elementos da Coluna 1: {matriz[0][0]+matriz[1][0]+matriz[2][0]}.')
print(f'O soma entre elementos da Coluna 2: {matriz[0][1]+matriz[1][1]+matriz[2][1]}.')
print(f'O soma entre elementos da Coluna 3: {matriz[0][2]+matriz[1][2]+matriz[2][2]}.')
