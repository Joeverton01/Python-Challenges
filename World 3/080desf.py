lista = list()
'''for c in range(0, 5):
    num = int(input('Digite um numero inteiro: '))
    if c == 0 or num > lista[-1]:  # ultimo da lista
        lista.append(num)
        print(f'valor adicionado na posição {c}')
    else:  # primeiro da lista ou varrer a lista ate achar a posição correta
        if num < lista[0]:
            lista.insert(0, num)
            print(f'valor adicionado na posição 0')  # primeiro
        else:
            for pos, c in enumerate(lista):
                if num < c:  # menor q lista[pos] entao vai ao lugar dela
                    lista.insert(pos, num)
                    print(f'valor adicionado na posição {pos}')
                    break
print(lista)
'''
# ex = [ 14, 20, 13, 17, 15]
# ex = [13,14,15,17,20]


# Solução com WHILE:
for c in range(5):
    num = int(input('Digite um número inteiro: '))
    if c == 0 or num > lista[-1]:  # Adiciona ao final da lista
        lista.append(num)
    else:
        pos = 0  # varre a lista ate achar um num menor
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)
