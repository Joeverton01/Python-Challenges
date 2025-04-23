# Cadastro em lista
numeros = list()
while True:
    num = int(input('Digite um número inteiro: '))
    if num not in numeros:
        numeros.append(num)
        print(f'Número cadastrado com sucesso!')
    else:
        print('número já cadastrado.')
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while opcao != 'S':
        if opcao != 'N':
            print('COMANDO INVÁLIDO!')
            opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        else:
            break
    if opcao == 'N':
        break
print(f'Todos os valores que você digitou em ordem crescente: ')
print(*sorted(numeros), sep=", ")


'''
num = []
while True:
    novos = int(input('Novo número: '))
    if novos not in num:
        num.append(novos)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor duplicado! Não vou adicionar.")
    
    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break

print("Valores únicos digitados, em ordem crescente:")
print(sorted(num))
'''
