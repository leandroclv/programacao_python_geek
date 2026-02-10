from cmath import log


import math
num = int(input('Digite um número inteiro: '))
if num > 0:
    loga = math.log(num)
    print(loga)
else:
    print('Número inválido')