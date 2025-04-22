print('GERADOR DE PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
while cont != 10:
    print(n1, end=' -> ')
    n1 += r
    cont += 1
print('PAUSA')
opcao = int(input('Quantos termos você quer mostrar a mais? '))
contotal = cont+opcao
cont = 0
while opcao != 0:
    while cont != opcao:
        print(n1, end=' -> ')
        n1 += r
        cont += 1
    print('PAUSA')
    opcao = int(input('Quantos termos você quer mostrar a mais? '))
    cont = 0
    contotal += opcao
print('FIM')
print('Progressão finalizada com {} termos mostrados.'.format(contotal))
