number = int(input('Digite um número de 4 digito: '))
unidade = number % 10
number = (number - unidade)/10
dezena = number % 10
number = (number - dezena)/ 10
centena = number % 10
number = (number - centena)/10
milhar = number
print(f'{int(milhar)}\n{int(centena)}\n{int(dezena)}\n{unidade}')

