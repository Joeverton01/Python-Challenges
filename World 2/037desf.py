# caculadora base numerica
# binario (b); OCTAL (c); HEXADECIMAL (X)maiusculo ou minusculo(x)
n = int(input('Digite um número inteiro: '))
print('[ 1 ] converter para Base Binária ')
print('[ 2 ] converter para Base Octal ')
print('[ 3 ] converter para Base hexadecimal ')
opcao = int(input('Sua opção:\n'))
if opcao == 1:
    print(f'o número {n} em binário é:\n {n:b}')
elif opcao == 2:
    print(f'O número {n} em OCTAL é: \n{n:c}')
elif opcao == 3:
    print('O número {} em HEXADECIMAL é:\n {:X}'.format(n, n))
else:
    print('Recomece o programae escolha 1, 2 ou 3')
