
from math import sqrt
ca = float(input('Digite o valor do cateto oposto de um triângulo retangulo: \n'))
co = float(input('Digite o valor do cateto oposto de um triângulo retangulo: \n'))
h = sqrt(ca**2+co**2)
print('O valor da hipotenusa é \
    h²=c²+b² \
  -->> hipotenusa desse triângulo é {}'.format(h))
