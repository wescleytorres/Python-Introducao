dados = dict()
lista = list()
somaidade = 0

while True:
    dados['nome'] = input('Nome: ')
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if dados['sexo'] == 'M' or dados['sexo'] == 'F':
            break
        print('Erro. favor informar M ou F.')
    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    lista.append(dados.copy())

    print('-=' * 30)
    while True:
        r = input('Deseja continuar? [S/N]: ').upper()
        if r in 'NS':
            break
        print('Erro. Por favor digite S ou N.')
    if r in 'N':
        break
m = (somaidade/len(lista))
print('-='*30)

print(f'- {len(lista)} Pessoas foram cadastradas!')
print(f'- A média de idade do grupo foi de {m:.0f} anos.')
print('- Mulheres no grupo: ', end='')
for v in lista:
    if v['sexo'] in 'F':
        print(v['nome'], end='. ')

print()

print(f'- Pessoas com idade acima da média {m:.0f}: ')
for c in lista:
    if c['idade'] > m:
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
