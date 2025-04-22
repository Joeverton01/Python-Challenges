# Aluguel de carro
d = float(input('Quantos dias o carro foi alugado? \n'))
km = float(input('Quantos km o carro rodou? \n'))
custo = 60*d + 0.15*km
print('O total a pagar é de R${:.2f}'.format(custo))
