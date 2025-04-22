# modo de pagar produto
preço = float(input('Digite o preço de um produto: R$'))
print('''FORMAS DE PAGAMENTO:
    [ 1 ] À vista (Dinheiro ou PIX)
    [ 2 ] À vista (Cartão)
    [ 3 ] Até 2x no cartão
    [ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Escolha um método de pagamento (1,2,3 ou 4): \n'))
if opcao == 1:
    juro = 0.9*preço
    print(f'O valor do produto aqui será {juro}')
elif opcao == 2:
    juro = 0.95*preço
    print(f'O valor do produto aqui será {juro}')
elif opcao == 3:
    juro = preço
    parc = int(input('Quantas parcelas? '))
    print(
        f'O valor do produto aqui será {juro}\n com {parc} parcelas de {juro/parc}')
elif opcao == 4:
    juro = 1.2*preço
    parc = int(input('Quantas parcelas? '))
    print(
        f'O valor do produto aqui será {juro}\n com {parc} parcelas de {juro/parc}')
else:
    print('Digite um número de 1 a 4')
