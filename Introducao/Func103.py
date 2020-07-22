def ficha(jog='<Desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato.')


n = input('Nome do Jogador: ')
g = input('Numeros de Gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
