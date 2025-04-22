# Fogos de artificio
from time import sleep
fogos = int(input('Quantos fogos de artificio soltar? '))
for c in range(0, fogos):
    for c in range(10, 0, -1):
        print(c)
        sleep(0.3)
    print('Bum bum POW')
    sleep(0.7)
