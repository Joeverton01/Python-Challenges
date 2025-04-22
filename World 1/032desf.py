# Ano bissexto?
ano = int(input('Informe um ano para analisar. Digite 0 se o ano for o ano atual.\n'))
if ano == 0:
    import datetime
    agora = datetime.date.today().year
    if agora % 4 == 0 and agora % 100 != 0 or agora % 400 == 0:
        print(f'O ano de {agora} é bissexto')
    else:
        print(f'O ano de {agora} não é bissexto')
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano de {ano} é bissexto')
    else:
        print(f'O ano de {ano} não é bissexto')
