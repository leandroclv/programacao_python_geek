num = int(input('Digite um número inteiro: '))
if num > 0:
    uni = num % 10
    num = (num - uni)/10
    dez = num % 10
    num = (num - dez)/10
    cent = num % 10
    num = (num - cent)/10
    mil = num % 10
    num = (num - mil)/10
    soma = uni + dez + cent + mil
    print(f'A soma dos números {int(mil)} + {int(cent)} + {int(dez)} + {int(uni)} = {int(soma)}!')
else:
    print('Número inválido')