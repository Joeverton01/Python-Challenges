# caixa eletronico SOLUÇÃO 3 é A MEHOR!
'''
print('-='*15, 'CAIXA ELETRÔNICO [SAQUE]', '=-'*15)
valor = int(input('Digite o valor a ser sacado: R$'))
valores = (50, 20, 10, 1)
for c in valores:
    quant_c = valor // c
    if quant_c > 0:
        print(f'{quant_c} Cédulas de R${c}')
    # valor muda pro restante para ser analisado pelo prox valor de C
    valor = valor - (c*quant_c)
'''

# caixa eletronico
'''
print('-=' * 15)
print(f'{"CAIXA ELETRÔNICO [SAQUE]":^40}')
print('-=' * 15)

dinheiro = int(input('Digite o valor a ser sacado: R$'))
ced = 50
totalced = 0

while True:
    if dinheiro >= ced:
        dinheiro -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} cédula(s) de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if dinheiro == 0:
            break

print('FIM')
'''


print('-='*15)
print(f'{'CAIXA ELETRÔNICO [SAQUE]':40}')
print('-='*15)

valor = int(input('Digite o valor a ser sacado: R$'))
valores = (50, 20, 10, 1)

for c in valores:
    quant_c = valor // c
    if quant_c > 0:
        print(f'{quant_c} cédula(s) de R$ {c}')
    valor -= quant_c * c  # Atualiza o valor restante
