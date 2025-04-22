# valores de 1 a 10 para os catetos:
from random import randint
from math import sqrt
a = randint(1, 10)
b = randint(1, 10)
h = sqrt(a*a+b*b)
print('Aqui está o valor da hipotenusa de um triângulo retângulo de catetos {} e {}'.format(a, b))
print('h²=a²+b² \n -->> h²={}²+{}²'.format(a, b))
print('h = {:.2f}'.format(h))
