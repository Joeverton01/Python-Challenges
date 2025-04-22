print('-=-'*25)
print('EMPRÉSTIMO BANCÁRIO')
print('-=-'*25)
casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Sálario do comprador: R$'))
tempo = float(input('Em quantos anos quer pagar essa casa? '))
prest = float(casa/(tempo*12))
print(f'O valor da prestação será de R${prest:.2f}')
if prest > 0.3*sal:
    print('Infelizmente esse empréstimo foi negado para você.')
else:
    print('Empréstimo concedido!')
