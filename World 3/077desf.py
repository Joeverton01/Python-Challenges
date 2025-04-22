tuple = ('tucano', 'salamandra', 'robinson', 'roberto', 'fernando', 'jubila', 'antonio',
         'manoel', 'marcos', 'tens', 'pe', 'lua', 'sol', 'man', 'ratata', 'kns', 'dnm', 'dns', 'gpu', 'tnm', 'mdlsw')

for palavras in tuple:
    print(f'\nNa palavra {palavras.upper()} temos as vogais: ', end='')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print(letras, end='')
