# JOKENPO 2 SOLUÇÕES
from time import sleep
from random import randint
print('{:=^40}'.format(' JO-KEN-PO!! '))
computador = randint(1, 3)
print("""VAMOS PRA BATALHA:
      [1] -> PEDRA
      [2] -> PAPEL
      [3] -> TESOURA """)
jogador = int(input('Escolha 1, 2 ou 3: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
# print(f'Você escolheu {jogador} e eu escolhi {computador}')
# Empate
# Pedra x Papel (1 , 2) jogador perde x
# Pedra x Tesoura (1 , 3) jogador ganha
# Papel x PEDRA (2, 1) jogador ganha
# Papel x TESOURA (2, 3) jogador perde x
# Tesoura x PEDRA (3, 1) jogador perde x
# Tesoura x PAPEL (3, 2) jogador ganha
if jogador == computador:
    if jogador == 1:
        print('-=-'*15)
        print('Computador jogou PEDRA')
        print('Jogador jogou PEDRA')
        print('-=-'*15)
    elif jogador == 2:
        print('-=-'*15)
        print('Computador jogou PAPEL')
        print('Jogador jogou PAPEL')
        print('-=-'*15)
    elif jogador == 3:
        print('-=-'*15)
        print('Computador jogou TESOURA')
        print('Jogador jogou TESOURA')
        print('-=-'*15)
    print('EMPATE')
    print('Que pena que dessa vez eu não te venci de novo, AHAHAHA')
# JOGADOR PERDE:
elif jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
    if jogador == 1 and computador == 2:
        print('-=-'*15)
        print('Computador jogou PAPEL')
        print('Jogador jogou PEDRA')
        print('-=-'*15)
    elif jogador == 2 and computador == 3:
        print('-=-'*15)
        print('Computador jogou TESOURA')
        print('Jogador jogou PAPEL')
        print('-=-'*15)
    elif jogador == 3 and computador == 1:
        print('-=-'*15)
        print('Computador jogou PEDRA')
        print('Jogador jogou TESOURA')
        print('-=-'*15)
    print('AHAHAHHA VOCÊ PERDEU DE NOVO!!')
else:
    if jogador == 1 and computador == 3:
        print('-=-'*15)
        print('Computador jogou TESOURA')
        print('Jogador jogou PEDRA')
        print('-=-'*15)
    elif jogador == 2 and computador == 1:
        print('-=-'*15)
        print('Computador jogou PEDRA')
        print('Jogador jogou PAPEL')
        print('-=-'*15)
    elif jogador == 3 and computador == 2:
        print('-=-'*15)
        print('Computador jogou PAPEL')
        print('Jogador jogou TESOURA')
        print('-=-'*15)
    print('Você venceu...')

'''from time import sleep
from random import randint
print('{:=^40}'.format(' JO-KEN-PO!! '))
computador = randint(1, 3)
print("""VAMOS PRA BATALHA:
      [ 1 ] -> PEDRA
      [ 2 ] -> PAPEL
      [ 3 ] -> TESOURA """)
jogador = int(input('Escolha 1, 2 ou 3: '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)
'''
