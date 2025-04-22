print('---TABUADA---\n')
while True:
    num = int(input('Digite um numero inteiro > 0: '))
    if num < 0:
        break
    print('-='*15)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-='*15)
print('Fim do programa. Volte sempre!')
