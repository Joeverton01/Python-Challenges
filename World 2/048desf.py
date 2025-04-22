# Soma impares multiplos de 3 entre 1 e 500(3soluções)
'''for c in range(3, 501, 6):
    print(c)
n1 = 3
nf = 495
n = (495//6)+1
print(f'O menor e o maior número procurado são respectivamente {n1} e {nf}')
print(f'E entre eles há {n} numeros')


soma = ((n1 + nf)*n)/2
print(f'A soma de todos eles é {soma}')
'''
from time import sleep
cont = 0
'''s = 0
print('Calculando a soma dos impares multiplos de 3 entre 1 e 500...')
sleep(1)
for c in range(3, 501, 6):
    cont += 1
    s = s+c
print(f'há {cont} numeros nesse intervalo e sua soma é {s}')
'''


print('Calculando a soma dos impares multiplos de 3 entre 1 e 500...')
sleep(1)
for c in range(3, 501, 6):
    cont += 1
soma = (3+c)*cont/2
print(f'há {cont} numeros nesse intervalo e sua soma é {soma:.0f}ahahah')
