dados = dict()
gols = list()
tot = 0
dados['Nome'] = input('Nome do Jogador: ')
part = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))

for c in range(0, part):
    g = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(g)
    tot += g
dados['Gols'] = gols
dados['Total'] = tot

print('-='*30)
print(dados)
print('-='*30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)

print(f'O jogador {dados["Nome"]} jogou {part} partidas.')
for i, v in enumerate(gols):
    print(f'{"=>":>10} Na partida {i+1}, fez {v} Gols.')
print(f'Foi um total de {dados["Total"]} Gols.')
