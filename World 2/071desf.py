# Caixa eletronico 071b Tem soluções MELHORES (3)
print('-='*15, 'CAIXA ELETRÔNICO [SAQUE]', '=-'*15)
valor = int(input('Digite o valor a ser sacado: R$'))
quant_50 = valor // 50
quant_20 = (valor - 50*quant_50)//20
valor10_1 = valor - (50*quant_50 + 20*quant_20)
quant_10 = valor10_1 // 10
quant_1 = valor10_1-10*quant_10
# RESULTADO


print('-='*20)
print(f' O total de cédulas de R$50 é {quant_50}') if quant_50 > 0 else None
print(f' O total de cédulas de R$20 é {quant_20}') if quant_20 > 0 else None
print(f' O total de cédulas de R$10 é {quant_10}') if quant_10 > 0 else None
print(f' O total de cédulas de R$1 é {quant_1}') if quant_1 > 0 else None
print('-='*20)
print('Volte sempre!')
'''
if quant_50 > 0:
    print(f'O total de cédulas de R$50 é {quant_50}')
if quant_20 > 0:
    print(f'O total de cédulas de R$20 é {quant_20}')
if quant_10 > 0:
    print(f'O total de cédulas de R$10 é {quant_10}')
if quant_1 > 0:
    print(f'O total de cédulas de R$1 é {quant_1}')
'''
