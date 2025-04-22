n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Outro número inteiro: '))
n3 = int(input('Outro número inteiro: '))
n4 = int(input('Outro número inteiro: '))
pares = 0
tuple = (n1, n2, n3, n4)
print('Entre os números', end=' ')
for c in tuple:
    print(c, end=' ')
# Apareceu 9?
print(f'O valor "9" apareceu {tuple.count(9)} vezes')
# Posição do primeiro valor 3
if 3 in tuple:
    print(f'O primeiro valor "3" está na posição {tuple.index(3) + 1}.')
else:
    print(f'Não há valores 3.')
# Quais foram os números pares
for c in tuple:
    if c % 2 == 0:
        print(f'{c} é par', end=', ')
        pares += 1
print(f'Há {pares} números pares')
print('FIM')
