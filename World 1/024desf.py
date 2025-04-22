# Santo in city
'''c = str(input('Em que cidade você nasceu? ')).strip().split()
formatado = c[0].lower()
santo = 'santo' in formatado
print(santo)

'''
# duas-formas
c = str(input('Em que cidade você nasceu? ')).strip()
print((c[:5].upper()) == 'SANTO')
