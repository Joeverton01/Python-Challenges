# PARES E IMPARES NUMA LISTA (LISTAS com % solução 2, 3 )
'''numeros = [[], []]
for p in range(7):
    num = int(input(f'Digite o {p+1}º número inteiro: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('Valores pares e impares formatados: ')
print(numeros[0])
print(numeros[1])
'''

numeros = [[], []]
for c in range(7):
    num = int(input(f'Digite o {c+1}º valor: '))
    numeros[num % 2].append(num)
numeros[1].sort()
numeros[0].sort()
print(f'numeros pares {numeros[0]}')
print(f'numeros impares {numeros[1]}')


'''valores = [[], []]
for c in range(1, 8):
    numero = int(input(f'Numero {c}°'))
    valores[numero % 2].append(numero)
print(f'Valores pares digitados: {sorted(valores[0])}')
print(f'Valores impares digitados: {sorted(valores[1])}')
'''
