# MAIORIDADE
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {c}º pessoa: '))
    idade = (atual - nasc)
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'\n{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')
