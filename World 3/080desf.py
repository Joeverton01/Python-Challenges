lista = []
for c in range(1, 6):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    if c == 1:
        menor = maior = num
for pos, i in enumerate(lista):
    if i == min(lista):


print(f'Lista formatada: \n {lista}')
