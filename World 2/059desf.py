#   menu de operações
from time import sleep
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
opcao = 0

while opcao != 5:
    soma = n1+n2
    multiplicação = n1*n2
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA ''')
    opcao = int(input('Escolha a opção: '))
    sleep(0.7)
    if opcao == 1:
        print(f'{n1} + {n2} é {soma}')
        sleep(1)
    elif opcao == 2:
        print(f'{n1} x {n2} é {multiplicação}')
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior é {n2}')
        else:
            print('Os números são iguais')
        sleep(1)
    elif opcao == 4:
        n1 = float(input('Digite o primeiro numero'))
        n2 = float(input('Digite o segundo numero'))
        sleep(1)
    elif opcao == 5:
        print('FIM DO PROGRAMA')
    else:
        print('opção inválida. Digite um número de 1 a 5')
        sleep(1)
