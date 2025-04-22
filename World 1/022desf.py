# Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join(). split()
# Nome completo characteristcs
nome = str(input('Digite seu nome completo: \n'))
mai = nome.upper()
min = nome.lower()
# sspace = (len(nome.replace(' ', '')))
sspace = len(nome) - nome.count(' ')
nome1 = nome.split()[0]
Q_nome1 = (len(nome1))

print('Seu nome em maiusculas é {}'.format(mai))
print('Seu nome em minusculas é {}'.format(min))
print('Seu nome tem ao todo {} letras'.format(sspace))
print('seu primeiro nome é {} e ele possui {} letras'.format(nome1, Q_nome1))
