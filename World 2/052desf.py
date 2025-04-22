num = int(input('Digite um numero inteiro: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print(c, end=" ")
        cont += 1
print(f'\n{num} tem {cont} divisores, e eles estão logo acima')
if cont == 2:
    print(f'Por isso {num} é primo')
else:
    print(f'Por isso {num} NÃO é primo')
