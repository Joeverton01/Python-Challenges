'''print('{:-^40}'.format(" PALINDROMOS "))
frase = input('Digite uma frase: ').strip().lower().split()
# .replace tbm tira espaços*
junta = ''.join(frase)
invfrase = junta[::-1]
print(f'O inverso da frase {junta} é {invfrase}')
if junta == invfrase:
    print('Por isso essa frase é um palindromo')
else:
    print('NÃO é um palindromo')
'''
print('{:-^40}'.format(" PALINDROMOS "))
frase = input('Digite uma frase: ').strip().lower()
# .split() e ''.join(frase) tbm tira espaços*
cont = ""
s_frase = frase.replace(' ', '')
for c in range(len(s_frase)-1, -1, -1):
    cont += s_frase[c]
print(f'O inverso da frase {s_frase} é {cont}')
if s_frase == cont:
    print('Por isso essa frase é um palindromo')
else:
    print('NÃO é um palindromo')
