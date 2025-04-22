n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
# Verifique quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor é {menor}')
# Verifique quem é maior
maior = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
print(f'O maior valor é {maior}')
