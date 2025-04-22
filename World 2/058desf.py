# QUAL NUM ESTOU PENSANDO?
from time import sleep
from random import randint
print('-------- ADIVINHAÇÃO --------\n')
''' NIVEL HARD
computador = ''
jogador = ' '
cont = 1
while computador != jogador:
    if cont > 1:
        print(f'O numero que pensei foi {computador}\n')
    computador = randint(0, 10)
    print('Pensando em um numero de 0 a 10...')
    sleep(0.5)
    jogador = int(input('Qual numero estou pensando? '))
    cont += 1
print(f'Você acertou! acertou na {cont} tentativa')
'''

computador = randint(0, 10)
jogador = ' '
cont = 0
while computador != jogador:
    jogador = int(input('Adivinhe o numero quer estou pensando: '))
    sleep(0.5)
    if computador > jogador:
        print('é um numero maior...')
    elif computador < jogador:
        print('é um numero menor...')
    cont += 1
print(f'Você acertou na {cont} tentativa')
