a = float(input('Digite o valor do lado a do triângulo: '))
b = float(input('Digite o valor do lado b do triângulo: '))
c = float(input('Digite o valor do lado c do triângulo: '))
if (a + b > c) or (a + c > b) or (b + c > a):
    if a == b == c:
        print('Este triângulo é equilátero.')
    elif (a == b) or (a == c) or (c == b):
        print('Este triângulo é isóceles.')
    elif (a != b != c):
        print('Este triângulo é escaleno')
else:
    print('Não é um triângulo.')