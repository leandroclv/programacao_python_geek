num = int(input('Digite um número inteiro: '))
if num % 3 == 0 or num % 5 == 0:
    print('Este número é divisível por 3 ou por 5')
elif num % 3 == 0 and num % 5 == 0:
    print('')
else:
    print('Este número não é divisível nem por 3 nem por 5')
