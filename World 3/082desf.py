# Pares e Impares numa Lista
valores = list()
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
