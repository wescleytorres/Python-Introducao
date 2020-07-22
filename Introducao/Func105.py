def notas(*n, sit=False):
    """
    -> Função de Analise: com Qdtde de notas, o valor maior; menor e média da turma.
    :param n: uma ou mais notas dos alunos para analise.
    :param sit: valor opcional para saber situação da média dos alunos.
    :return: Dicionario com varias informações sobre a analise.
    """
    from math import ceil  # Biblioteca para arrendondamento do valor da média
    Alunos = dict()
    prov = list()
    m = 0
    Alunos['Total'] = float(len(n))
    for c in n:
        prov.append(float(c))
        m += float(c)
    prov.sort()
    Alunos['maior'] = max(prov)
    Alunos['menor'] = min(prov)
    Alunos['média'] = ceil(m / Alunos['Total'])
    if sit:
        if Alunos['média'] <= 4:
            Alunos['situação'] = 'RUIM'
        if 5 <= Alunos['média'] <= 7:
            Alunos['situação'] = 'RAZOAVEL'
        elif Alunos['média'] > 7:
            Alunos['situação'] = 'OTIMO'

    return Alunos


# Programa principal
resp = notas(4, 4, 4, sit=True)
print(resp)
