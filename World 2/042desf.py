# Tipos de triângulos
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
s1 = l1 + l2
s2 = l1 + l3
s3 = l3 + l2
if s1 > l3 and s2 > l2 and s3 > l1:
    print('Esses segmentos PODEM FORMAR um triângulo')
    if l1 != l2 != l3 != l1:
        print('E esse triângulo é ESCALENO')
    elif l1 == l2 == l3:
        print('E esse triângulo é EQUILÁTERO')
    else:
        print('E esse triângulo é ISÓSCELES')
else:
    print('Esses segmentos NÃO PODEM FORMAR um triângulo')
