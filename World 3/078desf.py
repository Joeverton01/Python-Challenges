# minimos e maximos valores | listas
valores = [int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiroo número: ')),
           int(input('Digite o quarto número: ')),
           int(input('Digite o quinto número: ')),
           ]

print(f'Você digitou os valores {valores}')
print(f'O menor valor foi {min(valores)} e apareceu nas posições ', end='')
for c, num in enumerate(valores):
    if min(valores) == num:
        print(f'{c+1} ', end='')
print(f'\nO maior valor foi {max(valores)} e apareceu nas posições ', end='')
for c, num in enumerate(valores):
    if max(valores) == num:
        print(f'{c+1} ', end='')

'''num = [1, 2, 3, 4]
# '*' mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista
print(*num)
'''
