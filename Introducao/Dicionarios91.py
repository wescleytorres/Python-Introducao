from operator import itemgetter
from time import sleep
from random import randint
jogo = {'Jogador01': randint(1, 6),
        'Jogador02': randint(1, 6),
        'Jogador03': randint(1, 6),
        'Jogador04': randint(1, 6)}
ranked = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'{"VALORES SORTEADOS":^30}')
print('-'*30)
for k, v in jogo.items():
    print(f'O {k} tirou o numero {v} no dado.')
    sleep(1)

print('-'*30)
for i, v in enumerate(ranked):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
