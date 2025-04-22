# Fatorial de um número
'''import math
n = int(input('Vamos calcular o fatorial de um número. Digite um número: \n'))
fatorial = math.factorial(n)  # ou fatorial = math.factorial(5)
print(f'o fatorial é {fatorial}')
'''

n = int(input('Vamos calcular o fatorial de um número. Digite um número: \n'))
fatorial = 1
while n != 0:
    if n > 0:
        fatorial = n*fatorial
        n -= 1
    else:
        print('O fatorial de um número negativo não existe. Tente novamente\n')
        n = int(input('Digite um número: \n'))
print(f'o fatorial é {fatorial}')

'''
n = int(input('Vamos calcular o fatorial de um número. Digite um número: \n'))
fatorial = 1
if n < 0:
    while n < 0:
        print('O fatorial de um número negativo não existe. Tente novamente\n')
        n = int(input('Digite um número: \n'))
        if n == 0:
            print('O fatorial de 0 é 1')
        elif n > 0:
            for c in range(n, 0, -1):
                fatorial = c*fatorial
            print(f'O fatorial é {fatorial}')
elif n == 0:
    print('O fatorial de 0 é 1')
elif n > 0:
    for c in range(n, 0, -1):
        fatorial = c*fatorial
    print(f'O fatorial é {fatorial}')
'''
