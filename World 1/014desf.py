# Converter Temperaturas
print('Vamos converter uma medida de Celsius para Fahrenheit:')
c = float(input('Digite a temperatura em graus Celsius: \n'))
f = (1.8*c + 32)
print('{} graus celsius equivalem a {} graus fahrenheit'.format(c, f))
print('Agora vamos converter de Fahrenheit para Celsius:')
f2 = float(input('Digite a temperatura em Fahrenheit: \n'))
c2 = (f-32)/1.8
print('{} graus fahrenheit equivalem a {} graus Celsius'.format(f2,c2))
print('-'*20)