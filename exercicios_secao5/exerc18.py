num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
oper = int(input('Digite qual operação quer realizar com os números:\nAdição [1]\nSubtração [2]\nMultiplicação [3]\nDivisão [4]\n: '))
if 0 < oper < 5:
    if oper == 1:
        soma = num1 + num2
        print(f'A soma do número {num1} e do número {num2} é igual a {soma}!')
    elif oper == 2:
        sub = num1 - num2
        print(f'A subtração do número {num1} e do número {num2} é igual a {sub}!')
    elif oper == 3:
        mult = num1 * num2
        print(f'A multiplicação do número {num1} e do número {num2} é igual a {mult}!')
    else:
        div = num1 / num2
        print(f'A divisão dos números {num1} e do número {num2} é igual a {div:.2f}!')
else:
    print('Dados inválidos')
