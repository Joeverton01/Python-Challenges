# classificação nadadores
from datetime import date
nasc = int(input('Ano de nascimeto: '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JÚNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER INFANTE')
