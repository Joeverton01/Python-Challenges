# Desafio 057 - Verificando se o sexo é M ou F
sexo = str(input('Digite o sexo de uma pessoa [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo inválido!')
    sexo = str(input('Digite o sexo de uma pessoa [M/F]: ')).strip().upper()
if sexo == 'M':
    print('essa pessoa é masculina')
else:
    print('essa pessoa é feminina')
print('FIM!!')

# solução 2

sexo = input('Sexo de uma pessoa [M/F]: ').strip().upper()[0]
print(sexo)
while sexo not in "MF":
    sexo = input(
        'Sexo inválido! Digite o sexo de uma pessoa [M/F]: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
# FIM!!