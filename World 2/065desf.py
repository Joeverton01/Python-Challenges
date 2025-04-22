soma = 0
cont = 1

num = int(input('Digite um número inteiro: '))
soma += num
maior = num
menor = num
opcao = str(input('Deseja continuar [S/N]? ').strip().lower())[0]
negativo = True
# resultado das opções: se opção = s ou se opção = n ou se opção invalida

while negativo:
    if opcao == 's':
        while opcao == 's':
            num = int(input('Digite um número inteiro: '))
            soma += num
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
            opcao = str(input('Deseja continuar [S/N]? ').strip().lower())[0]
            cont += 1

    elif opcao == 'n':
        negativo = False
    else:
        print('COMANDO INVÁLIDO!')
        opcao = str(input('Deseja continuar [S/N]? ').strip().lower())[0]
# maior e menor

media = soma/cont

# media
if cont > 1:
    print(f'Você digitou {cont} números. A média é {media:.2f}')
else:
    print(
        f'Você digitou {cont} número. A média de um número só é ele mesmo ({media:.2f})')
# maior e menor
if maior == menor:
    print(f'O maior e o menor número digitado é {maior}, são iguais.')
else:
    print(
        f'O maior número digitado é {maior} e o menor número digitado é {menor}.')
print('FIM')
