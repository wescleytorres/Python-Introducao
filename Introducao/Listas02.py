lista = []
nome = []
nota = []
while True:
    nome.append(input('Nome: '))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    nome.append(nota[:])
    lista.append(nome[:])
    nome.clear()
    nota.clear()
    r = input('Quer continuar? [S/N]: ')
    if r in 'Nn':
        break
print('-='*30)
print(f'Nº  {"NOME":<10} {"MÉDIA":^10}')
print('-'*50)
for c in range(0, len(lista)):
    print(f'{c} - {lista[c][0]:<10} {(lista[c][1][0]+lista[c][1][1])/2:^10}')
print('-' * 50)

r = input('Deseja verificar notas do alunos? [S/N]: ')
if r in 'Ss':
    while True:
        print('-' * 50)
        n = int(input('Mostrar notas de qual aluno?: '))
        print(f'Notas de {lista[n][0]} são: {lista[n][1]}')
        print()
        r = input('Quer continuar? [S/N]: ')
        if r in 'Nn':
            break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
