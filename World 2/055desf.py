# metodo ''principal''
'''lista = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    lista.append(peso)
print(f'O menor peso foi: {min(lista)} ')
print(f'O maior peso foi: {max(lista)}')'''

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(maior)
print('menor ', menor)
