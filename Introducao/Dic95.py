jogadores = list()
dados = dict()
gols = list()
tot = cont = 0
while True:
    dados['Nome'] = input('Nome do Jogador: ')
    part = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
    cont += 1
    for c in range(0, part):
        g = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(g)
        tot += g
        dados['Gols'] = gols.copy()
        dados['Total'] = tot
    jogadores.append(dados.copy())
    tot = 0
    gols.clear()
    while True:
        print('-='*30)
        r = input('Deseja continuar? [S/N]: ').upper()
        if r in 'SN':
            break
        print('Erro. Favor digite S ou N.')
    if r in 'N':
        print('-=' * 30)
        break
    print('-='*30)

print(f'Cod {"Nome":<20} {"Gols":<20} {"Total":<20}')
print('-'*60)
for e, j in enumerate(jogadores):
    print(f'{e:<3} ', end='')
    for v in j.values():
        print(f'{str(v):<20}', end=' ')
    print()
print('-='*30)

while True:
    while True:
        n = int(input('Mostrar dados de qual jogador?: '))
        if n < cont:
            break
        print('ERRO! Não existe jogador com esse código')
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["Nome"]} --')
    for c, g in enumerate(jogadores[n]["Gols"]):
        print(f'  No jogo {c+1} fez {g} gols.')
    print('-' * 60)
    while True:
        r = input('Deseja continuar?: ').upper()
        if r in 'SN':
            break
        print('ERRO! Favor digitar S ou N.')
    if r == 'N':
        break
print('<< VOLTE SEMPRE >>')
