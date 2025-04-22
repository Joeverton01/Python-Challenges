from random import randint
from time import sleep
print('{:=^40}'.format(" JO-KEN-PO "))
itens = ["PEDRA", "PAPEL", "TESOURA"]
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = randint(0, 2)
jogador = int(input('O que você quer jogar? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
print(f'''\n\nO computador jogou {itens[computador]}
O jogador jogou {itens[jogador]}\n\n''')
if jogador == computador:
    print('EMPATE!!')
    '''JOGADORGANHA:
    PEDRA-TESOURA(0,2)
    PAPEL-PEDRA(1,0)
    TESOURA-PAPEL(2,1)
        JOGADORPERDE
    PEDRA-PAPEL(0,1)
    PAPEL-TESOURA(1,2)
    TESOURA-PEDRA(2,0)'''
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('JOGADOR GANHOU!!')
else:
    print('COMPUTADOR GANHOU!!!!!')
