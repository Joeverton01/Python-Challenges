times_brasileiros = (
    "Flamengo", "Palmeiras", "Santos", "São Paulo", "Corinthians",
    "Grêmio", "Internacional", "Atlético Mineiro", "Cruzeiro", "Fluminense",
    "Botafogo", "Vasco da Gama", "Athletico Paranaense", "Chapecoense", "Bahia",
    "Sport Recife", "Ceará", "Fortaleza", "Goiás", "Coritiba"
)
print(f'5 Primeiros times do Brasileirão:\n\n {times_brasileiros[:5]}')
print(f'Ultimos quatro colocados da tabela:\n\n {times_brasileiros[-4:]}')
print(
    f'Times em ordem alfabetica:\n\n {sorted(times_brasileiros)}')
print(
    f'Posição da Chapecoense na tabela:\n\n {times_brasileiros.index('Chapecoense')+1}ª')
