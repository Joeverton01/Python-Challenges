# Alistamento militar
from datetime import date
print('''Você é homem ou mulher?
      [ 1 ] Homem
      [ 2 ] Mulher''')

sexo = int(input('Digite 1 ou 2: '))


if sexo == 2:
    print('AAHAHHA você é mulher não deve se alistar')
elif sexo == 1:
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual-nasc
    print(f'Quem nasceu em {nasc} tem em {atual}, {idade} anos')
    # Maior de 18 anos
    if idade > 18:
        print(f'Você já deveria ter se alistado a {idade-18} anos!')
        print(f'Seu alistamento foi em {nasc+18}')
        # menor de 18 anos
    elif idade < 18:
        print(f'Você deve se alistar em {18-idade} anos!')
        print(f'Você deve se alistar em {nasc+18}')
        # tem 18 anos
    else:
        print(f'Seu alistamento é em {atual}')
        print(f'Você deve se alistar IMEDIATAMENTE!')
