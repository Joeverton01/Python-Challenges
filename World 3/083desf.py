# Expressão com parenteses
aux = []
expres = input('Digite a expressão: ')  # strip pq sim
for c in expres:
    if c == '(':
        aux.append(c)
    if len(aux) > 0:
        if c == ')':
            aux.pop()  # pop remove o ultimo [-1] automaticamente
    elif c == ')':
        aux.append(c)

if len(aux) > 0:
    print('Sua espressão está invalida!')
else:

    print(f'Sua expressão está valida')
