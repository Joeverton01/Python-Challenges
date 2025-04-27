# Matriz 3x3
matriz = [[[], [], []], [[], [], []], [[], [], []]]
for c in range(3):
    for i in range(3):
        matriz[c][i].append(
            int(input(f'Digite o inteiro para a posição [{c}, {i}] da matriz: ')))
print('-='*20)
for p in (matriz):
    print(*p)
