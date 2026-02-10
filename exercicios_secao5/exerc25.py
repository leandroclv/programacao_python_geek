import math
a = float(input('Digite o valor da variável a: '))
b = float(input('Digite o valor da variável b: '))
c = float(input('Digite o valor da variável c: '))
if a != 0:
    delta = (b ** 2) - (4 * a * c)
    x = (-b + math.sqrt(delta))/ (2 * a)
    if delta < 0:
        print('Não existe raiz ')
    elif delta == 0:
        print(f'Raiz única {x}.')        
    else:
        x_1 = (-b - math.sqrt(delta))/ (2 * a)
        print(f'As duas raizes reais são {x} e {x_1} ')
else:
    print('Não é equação de segundo grau')
