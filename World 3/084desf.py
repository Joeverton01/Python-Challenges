# nome e peso de varias pessoas | mostrar quantas pessoas foram cadastradas | lista com as pessoas mais pesadas | lista com as pessoas mais leves
#  solução 1
'''pessoas = 0
pesos = []
nomes = []
while True:  # cadastro
    nome = input('Nome: ').strip()
    peso = float(input('Peso: '))
    pessoas += 1
    pesos.append(peso)
    nomes.append(nome)

    opcao = input('Quer continuar [S/N]? ').strip().upper()[0]  # opcao
    while opcao != 'S':
        if opcao == 'N':
            break
        print('COMANDO INVÁLIDO!')
        opcao = input('Quer continuar [S/N]? ').strip().upper()[0]
    if opcao == 'N':
        break
# Visualizar pesos
maior = max(pesos)
menor = min(pesos)
index = []

for pos, c in enumerate(pesos):  # indice dos maiores pesos
    if c == maior:
        index.append(pos)


print(f'Você cadastrou {pessoas} pessoas.')
print(f'Entre essas pessoas o maior peso foi {maior} das pessoas: ')
for pos, c in enumerate(nomes):
    if pos in index:
        print(c)
index.clear()

print(f'E o menor peso {menor}, foram das pessoas: ')

for pos, c in enumerate(pesos):  # indice dos menores pesos
    if c == menor:
        index.append(pos)
for pos, c in enumerate(nomes):
    if pos in index:
        print(c)
index.clear()
'''
maior = menor = 0
temp = []
main = []
while True:  # registro
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    main.append(temp[:])
    # maior menor
    if len(main) == 1:
        for p in main:
            maior = menor = p[1]
    if len(main) > 1:
        for p in main:
            if p[1] > maior:
                maior = p[1]
            if p[1] < menor:
                menor = p[1]
    temp.clear()
    opcao = input('Quer continuar [S/N]? ').strip().upper()[0]  # opcao
    while opcao != 'S':
        if opcao == 'N':
            break
        print('COMANDO INVÁLIDO!')
        opcao = input('Quer continuar [S/N]? ').strip().upper()[0]
    if opcao == 'N':
        break

print(f'Você cadastrou {len(main)} pessoas.')  # resultado
print(f'Pessoas mais pesadas:')
for p in main:
    if p[1] == maior:
        print(f'{p[0]}')

print(f'Pessoas mais leves:')
for p in main:
    if p[1] == menor:
        print(f'{p[0]}')


'''temp = []
main = []
while True:  # registro
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    main.append(temp[:])
    temp.clear()
    opcao = input('Quer continuar [S/N]? ').strip().upper()[0]  # opcao
    while opcao != 'S':
        if opcao == 'N':
            break
        print('COMANDO INVÁLIDO!')
        opcao = input('Quer continuar [S/N]? ').strip().upper()[0]
    if opcao == 'N':
        break

print(f'Você cadastrou {len(main)} pessoas.')  # resultado maior e menor:

maior = max(main, key=lambda p: p[1])
menor = min(main, key=lambda p: p[1])


print(f'Pessoas mais pesadas:')
for p in main:
    if p[1] == maior[1]:
        print(f'{p[0]}')

print(f'Pessoas mais leves:')
for p in main:
    if p[1] == menor[1]:
        print(f'{p[0]}')
'''
