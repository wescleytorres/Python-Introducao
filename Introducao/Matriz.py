from time import sleep
from random import randint
lista = []
print('-'*30)
print(f'{"JOGAR NA MEGA SENA":^30}')
print('-'*30)
vezes = int(input('Quantos jogos deseja efetuar?: '))
print(f'-=-=-= SORTEANDO {vezes} JOGOS =-=-=-')
for c in range(0, vezes):
    n = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
    lista.append(n)
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(1)
print(f'{" < BOA SORTE! > ":-^30}')
