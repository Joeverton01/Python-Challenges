# Situação escolar
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('O aluno ficou com uma média pessima e foi REPROVADO!')
elif media >= 7:
    print('O aluno ficou com uma média boa e foi APROVADO!')
elif media >= 5 and media < 7:
    print('O aluno ficou de RECUPERAÇÃO')
