def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade <= 15:
        return f'Com {idade} anos: NÃO VOTA'
    if 18 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    elif 16 == idade or idade == 17 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'


n = int(input('Informe o Ano de Nascimento [yyyy]: '))
agr = voto(n)
print(f'{agr}')
