# cadastro de produtos e preço
'''
soma = contador = barato = more_than_1000 = 0
while True:  # NOME
    contador += 1
    nome = input('Digite o nome do produto: ').capitalize().strip()
    while nome.isnumeric():
        nome = input('INVÁLIDO, apenas números. Digite o nome do produto: ')

# PREÇO

    preço = float(input('Digite o preço: R$'))
    soma += preço
    if preço > 1000:
        more_than_1000 += 1
    if contador == 1:
        barato = preço
        nome_barato = nome
    elif preço < barato:
        barato = preço
        nome_barato = nome
# OPÇÃO
    opcao = input('Quer cadastrar outro produto? [S/N]').strip().upper()[0]
    if opcao not in ('S', 'N'):
        while opcao not in ('S', 'N'):
            opcao = input(
                'Quer cadastrar outro produto? [S/N]').strip().upper()[0]
    if opcao == 'N':
        break

# RESULTADO
print(f'Você cadastrou {contador} produtos que custam R${soma:.2f}')
print(f'Destes, {more_than_1000} custam mais que R$1000')
print(f'E o mais barato foi "{nome_barato}" que custa R${barato:.2f}')
'''
