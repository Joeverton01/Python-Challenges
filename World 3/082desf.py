# Pares e Impares numa Lista
'''valores = list()
pares_valores = list()
impar_valores = list()
while True:
    num = int(input('Digite um numero inteiro: '))
    valores.append(num)
    if num % 2 == 0:
        pares_valores.append(num)
    else:
        impar_valores.append(num)
    opcao = str(input('Quer continuar? [S/N]?')).strip().upper()[0]  # OPCAO
    while opcao != 'S':
        if opcao != 'N':
            print('COMANDO INVÁLIDO!')
            opcao = str(input('Quer continuar? [S/N]?')).strip().upper()[0]
        elif opcao == 'N':
            break
    if opcao == 'N':
        break
print(f'Lista: {valores}')
print(f'Valores pares {pares_valores}')
print(f'Valores impares {impar_valores}')
'''
valores = []
impar = []
pares = []
while True:
    num = int(input('Digite um numero inteiro: '))
    valores.append(num)
    opcao = input('Quer continuar [S/N]?').strip().upper()[0]
    while opcao != 'S':
        if opcao == 'N':
            break
        elif opcao != 'N':
            print('COMANDO INVÁLIDO!')
            opcao = input('Quer continuar [S/N]?').strip().upper()[0]
    if opcao == 'N':
        break
print(f'Valores digitados: {valores}')
for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impar.append(c)

print(f'pares {pares}\n impares {impar}')
