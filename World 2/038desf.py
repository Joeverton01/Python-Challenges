# comparando 2 numeros
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 == n2:
    print(f'Os valores são iguais')
elif n1 > n2:
    print(f'O primeiro valor é maior ({n1})')
else:
    print(f'O segundo valor é maior ({n2})')
