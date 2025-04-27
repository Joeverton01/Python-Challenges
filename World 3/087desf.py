# Matrix V2.0
soma_3col = soma_par = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-='*20)
for l in range(3):
    soma_3col += matriz[l][2]
    for c in range(3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print('-='*20)
print(f'A soma dos pares é {soma_par}')
print(f'A soma dos números na 3º coluna é {soma_3col}')
print(f'Maior valor da 2º linha: {max(matriz[1])}')
