n1 = float(input('Digite a 1° nota do aluno: '))
n2 = float(input('Digite a 2° nota do aluno: '))
if (0 < n1 <= 10) and (0 < n2 <= 10):
    media = (n1 + n2) / 2
    print(f'A media das notas é {media:.2f}.')
else:
    print('As notas não possuem um valor válido')