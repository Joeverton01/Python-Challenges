from random import randint
'''
x1 = randint(0, 10)
x2 = randint(0, 10)
x3 = randint(0, 10)
x4 = randint(0, 10)
x5 = randint(0, 10)
tuple = x1, x2, x3, x4, x5
print(f'Os números sorteados são: {tuple}')
print(
    f'Portanto o maior e o menor número são: \n {sorted(tuple)[-1]} e {sorted(tuple)[0]}')
'''
numeros = (randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10),
           randint(0, 10))
print(f'Os numeros são ', end='')
for c in numeros:
    print(c, end=' ')
print(f'\nO maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')
