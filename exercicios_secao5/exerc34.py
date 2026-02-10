nota = float(input('Digite a nota do aluno: '))
falta = int(input('Digite o número de falta do aluno: '))
if falta <= 20:
    if 9 < nota <= 10:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito A')
    if 7.5 < nota <= 8.9:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito B')
    if 5 < nota <= 7.4:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito C')
    if 4 < nota <= 4.9:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito D')
    if 0 < nota <= 3.9:
        print(f'O aluno tem a nota {nota:.2f} com {falta} Faltas e o conceito E')
else:
    if 9 < nota <= 10:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito B')
    if 7.5 < nota <= 8.9:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito C')
    if 5 < nota <= 7.4:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito D')
    if 4 < nota <= 4.9:
        print(f'O aluno tem a nota {nota:.2f} com {falta} faltas e o conceito E')
    if 0 < nota <= 3.9:
        print(f'O aluno tem a nota {nota:.2f} com {falta} Faltas e o conceito E')
