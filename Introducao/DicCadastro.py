from datetime import date
dados = dict()
pessoa = list()
idade = date.today().year

dados['Nome'] = input('Nome: ')
ano = int(input('Ano de Nasc.: '))
dados['Idade'] = idade - ano
dados['CTPS'] = int(input('Nº CTPS (0 para não tenho): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Informe Salario: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - idade)
else:
    dados['CTPS'] = 'Não tem'

for k, v in dados.items():
    print(f'{k} é igual a {v}.')
