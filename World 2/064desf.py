'''sum = 0
num = 0
cont = 0
while num != 999:
    num = int(input('Digite um número inteiro. digite 999 para sair: '))
    if num != 999:
        print(f'Você digitou o número {num}')
        sum += num
        cont += 1
    else:
        print(f'Você pediu para sair!')
print(f'Você digitou {cont} números e a soma deles é {sum}')
'''

sum = cont = 0
num = int(input('Digite um número inteiro [999 para sair]: '))
while num != 999:
    print(f'Você digitou o número {num}')
    sum += num
    cont += 1
    num = int(input('Digite um número inteiro [999 para sair]: '))
print(f'Você digitou {cont} números e a soma deles é {sum}')
print('fim')
