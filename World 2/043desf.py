# IMC
h = float(input("Quantos metros de altura você tem? "))
p = float(input('Quantos quilos você pesa? '))
imc = float(p/h**2)
print(f'O IMC é de {imc:.1f} ')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('Parabéns você está no PESO IDEAL!')
elif imc < 30:
    print('Você está com SOBREPESO.')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA, CUIDADO!')
