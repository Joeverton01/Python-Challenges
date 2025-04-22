# Quantidade e posições e uma letra numa frase:
'''
frase = str(input('Digite uma frase:\n')).strip().lower()
e = int(frase.count('a'))
e2 = int(frase.count('ã'))
e3 = int(frase.count('á'))
e4 = int(frase.count('â'))
e5 = int(frase.count('à'))
se = e+e2+e3+e5+e4
a1 = int(frase.find('a'))
ultimo = len(frase)
invertea = int(frase[::-1].find('a'))
#frase.rfind('a')-->>Procurar 'a' a da direita para esquerda (right to left)

print(f'A letra "A" apareceu {se} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {a1+1}')
# -ultimo-1
print(f'A ultima letra "A" apareceu na posição {ultimo-invertea}')
# print('A ultima letra "A" apareceu na posição ')
'''


frase = str(input('Digite uma frase:\n')).strip().lower()
e = int(frase.count('a'))
e2 = int(frase.count('ã'))
e3 = int(frase.count('á'))
e4 = int(frase.count('â'))
e5 = int(frase.count('à'))
se = e+e2+e3+e5+e4
a1 = int(frase.find('a'))

print(f'A letra "A" aparece {se} vezes na frase.')
print(f'A primeira letra "A" aparece na posição {a1+1}')
print('A ultima letra "A" aparece na posição {}'.format((frase.rfind('a')+1)))
