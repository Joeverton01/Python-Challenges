cont = valor_5 = 0
valores = []
while True:
    num = int(input('Digite um número inteiro: '))
    valores.append(num)
    cont += 1

    if 5 == valores[len(valores)-1]:
        valor_5 += 1
    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while opcao != 'S':
        if opcao != 'N':
            print("COMANDO INVÁLIDO!")
            opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
            print(opcao)
        elif opcao == 'N':
            break
    if opcao == 'N':
        break

print(f'Você digitou {cont} valores que em ordem decrescente são:')
print(f'{sorted(valores, reverse=True)}')
print(f'Você digitou o valor 5 um total de {valor_5} vezes.')
