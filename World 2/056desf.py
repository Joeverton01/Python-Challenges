# DESAFIO(MEUCODIGO:ABAIXO)
'''soma = 0
maioridadehomem = 0
nomehomemvelho = ""
cont_mulher = 0
for c in range(1, 5):
    title = (' {}ª PESSOA '.format(c))
    print('{:=^20}'.format(title))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma += idade
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo == "F" and idade < 20:
        cont_mulher += 1
m_soma = soma/4
print(f'A media da idade do grupo é {m_soma}')
if nomehomemvelho != "":
    print(
        f'O nome do homem mais velho é {nomehomemvelho}, tem {maioridadehomem} anos')
else:
    print('Por que não há homens [M] aqui?')
print(f'Ao todo há {cont_mulher} mulheres com menos de 20 anos.')
'''
