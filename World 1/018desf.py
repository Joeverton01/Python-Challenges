# Sen Cos Tg de um angulo

import math
an = float(input('Digite um angulo: \n'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))

print('O seno de {} é {:.2f}'.format(an, sen))
print('O cosseno de {} é {:.2f}'.format(an, cos))
print('A tangente de {} é {:.2f}'.format(an, tg))
