menor = maior = soma = cont = 0
opcao = 's'
lista = []
while opcao == "s":
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    lista.append(n)
    opcao = str(input('Quer continuar [S/N]? ').lower().strip())[0]
media = soma/cont
print(f'Voce escreveu {cont} numeros e a media foi {media}')
print(
    f'O maior e o menor numero que voce escreveu foi {max(lista)} e {min(lista)}')
