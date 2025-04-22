# converter moedas
r = float(input('Quanto dinheiro você tem no nubank? \n -->> R$'))
d = 3.27
q = r/3.27
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(r,q))
