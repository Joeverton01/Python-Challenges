tuple_numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                 'seis', 'sete', 'oito',   'nove', 'dez', 'onze',
                 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                 'dezessete', 'dezoito', 'dezenove', 'vinte')
# OPÇÕES
'''escolha = -1
while escolha < 0 or escolha > 20:
    escolha = int(input('Digite um inteiro entre 0 e 20: '))
    if escolha < 0 or escolha > 20:
        print('INVÁLIDO')
'''

while True:
    escolha = int(input('Digite um inteiro entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('INVÁLIDO.', end=' ')

# Resultado

print(f'{escolha} por extenso é {tuple_numbers[escolha]}')
