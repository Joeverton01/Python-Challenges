# Primeiro-ultimo-nomepessoas
'''
nome = str(input('Digite seu nome completo:\n')).strip().split()

print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu ultimo nome é: {nome[-1]}')
'''

nome = str(input('Digite seu nome completo:\n')).strip().split()
primeiro = nome[0]
ult = len(nome)
ultimo = nome[(ult-1)]

print(f'Seu primeiro nome é: {primeiro}')
print(f'Seu ultimo nome é: {nome[(ult-1)]}')
