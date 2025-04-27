# Matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(3):
    for i in range(3):
        matriz[c][i] = int(
            input(f'Digite o inteiro para a posição [{c}, {i}] da matriz: '))
print('-='*20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
