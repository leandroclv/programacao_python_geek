#valor = 1.44
#print(valor)

nome = str(input('Digite uma frase: ')).replace(' ','').lower()
if nome == nome[::-1]:
    print('É um palindromo')
else:
    print('Não é um palindromo')
