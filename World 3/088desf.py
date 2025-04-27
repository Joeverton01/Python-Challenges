# MEGA SENA
print('-='*20)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-='*20)
quantidade = int(input('Digite quantos jogos serão sorteados: '))
for jogadas in range(1, quantidade+1):
    opcoes = []
    for c in range(61):
        opcoes.append(c)
    print(opcoes)
