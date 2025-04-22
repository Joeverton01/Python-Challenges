# idade, sexo de varias pessoas:
'''

# CADASTRO DAS PESSOAS:
maioridade = 0
homens = 0
mulherjovem = 0
while True:
    print('-='*15,  '\n CADASTRE UMA PESSOA \n',  '-='*10)
    idade = input('Digite a idade da pessoa: ')
    while idade.isnumeric() != True:
        idade = input('Digite uma idade válida: ')
    print(f'Idade {idade} registrada com sucesso!')
    idade = int(idade)
    if idade >= 18:
        maioridade += 1

    sexo = input('Digite o Sexo da pessoa [M/F]: ').strip().upper()[0]
    while sexo != 'F' and sexo != "M":
        print('ok')
        sexo = input('Digite [M/F]: ').strip().upper()[0]
    print(f'Sexo {sexo} registrado com sucesso!')
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherjovem += 1

    opcao = input('Quer cadastrar mais pessoas [S/N]? ').strip().upper()[0]
    while opcao != 'S':
        if opcao == 'N':
            break
        else:
            opcao = input('INVÁLIDO. Mais pessoas [S/N]? ').strip().upper()[0]
    if opcao == 'N':
        break
# Resultado
print(f'Você cadastrou {maioridade} pessoas maiores de idade')
print(f'Você cadastrou {homens} homens')
print(f'Você cadastrou {mulherjovem} mulheres com menos de 20 anos.')

'''
