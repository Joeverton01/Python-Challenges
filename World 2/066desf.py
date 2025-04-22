cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
if cont > 0:
    if cont == 1:
        print(f'Voce digitou apenas o numero {soma}')
    elif cont >= 2:
        print(f'Voce digitou {cont} numeros e a soma foi {soma}')
print('--FIM--')
