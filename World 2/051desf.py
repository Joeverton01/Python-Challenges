print("10 termos de uma PA:")
n1 = int(input("Digite o primeiro termo dessa PA: "))
r = int(input("Digite a razão dessa PA: "))
cont = 1
for c in range(n1, n1+r*10, r):
    print(f'O {cont}º termo da PA é {c}')
