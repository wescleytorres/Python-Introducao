from uteis import moedas
from uteis.moedas import monet

p = float(input('Digite o valor: R$ ').replace(',', '.'))
print(f'A metade do número {monet(p)} é igual a R$ {moedas.metade(p)}')
print(f'O dobro do número {monet(p)} é igual a R$ {moedas.dobro(p)}')
print(f'Aumentando 10%, temos R$ R$ {moedas.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R$ R$ {moedas.reduzir(p, 13)}')
print(monet(520.00))
