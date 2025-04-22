# MULTIPLOS DO METRO
n = float(input('Digite um valor em metros: \n '))
print('{}m são \n {:15}km \n {:15}hm \n {:14}dam \n {:15}dm \n {:15}cm \n {:15}mm'.format(
    n, (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))
