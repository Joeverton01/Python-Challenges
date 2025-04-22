print('Analisar triângulos')
l1 = float(input('Primeiro Segmento '))
l2 = float(input('Segundo Segmento '))
l3 = float(input('Terceiro Segmento '))
s1 = l1 + l2
s2 = l1 + l3
s3 = l2 + l3

if s1 > l3 and s2 > l2 and s3 > l1:
    print(f'Esses segmentos PODEM formar um triângulo')
else:
    print("Esses segmento NÃO PODEM formar um triângulo")
