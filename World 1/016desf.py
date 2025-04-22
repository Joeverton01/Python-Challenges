# Mostrar a parte inteira de um número real
'''from math import floor
n = float(input('Digite um número: \n'))
print('parte inteira de {} é {}'.format(n, floor(n)))'''
from math import trunc
n = float(input('Digite um número: \n'))
print('O número digitado foi {} e sua parte inteira é {}'.format(n, trunc(n)))
