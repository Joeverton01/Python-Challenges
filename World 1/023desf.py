# Unidade,dezena,centena,milhar
n = int(input('Digite um numero de 0 a 9999-->> '))
milhar = int(n//1000)
cent = int(n-milhar*1000)
centena = int(cent//100)
dez = cent-centena*100
# dez2 = n-(milhar*10**3+centena*10**2)
dezena = dez//10
uni = int(dez-dezena*10)


print(uni)
print(dezena)

print(centena)
print(milhar)
'''
# OUTRA SOLOUÇÃO INCRIVEL
n = int(input('Digite um numero de 0 a 9999-->> '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('unidade:',u)
print('dezena:',d)
print('centena:',c)
print('milhar:',m)
'''
