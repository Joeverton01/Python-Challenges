# Desafio 63 - Fibonacci
t1 = 0
t2 = 1
r = t2+t1
cont = 0
quantidade = int(input("Quantos termos você quer mostrar? "))
while quantidade > cont:  # esse while so pode ter um t1 ou um t2 ou um r, teste.
    print(t1, end=" -> ")
    t1 = t2
    t2 = r
    r = t1 + t2
    cont += 1
print("FIM")

'''
n = int(input('Quantos termos quer? '))
a = 0
b = 1
c = 0
cont = 0
while cont < n:
    print('{} → '.format(c), end='')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')
'''

'''t1 = 0
t2 = 1
r = t2+t1
quantidade = int(input("Quantos termos você quer mostrar? "))
for c in range(1, quantidade+1):
    print(t1, end=" -> ")
    t1 = t2
    t2 = r
    r = t1 + t2
print("FIM")
print(f'foram mostrados {c} termos')
'''
