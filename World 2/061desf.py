print('---- PROGRESSÃO ARITMETICA ----')
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
an = n1
while an != n1 + (r*10):
    print(an, end=' -> ')
    an += r
print('FIM')
