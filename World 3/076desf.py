print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)

cadernos = ('mod1', 2.65,
            'mod2', 3.4,
            'aula1', 4.25,
            'soft', 50.2,
            'tens', 1.75)

for c in range(0, len(cadernos)):
    if c % 2 == 0:
        print(f'{cadernos[c]:.<20} R$', end=' ')
    else:
        print(f'{cadernos[c]:>5}')
print('-'*40)
