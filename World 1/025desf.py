# nome_com_silva
nome = str(input('Qual seu nome completo? \n')).strip().lower().split()
silva = 'silva' in nome
print(f'Seu nome tem Silva? {silva}')
# se nao usar.split() identifica-se SILVANA como silva tambem
