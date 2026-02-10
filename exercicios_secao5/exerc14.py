n1 = float(input('Digite a nota do trabalho de laboratório: '))
n2 = float(input('Digite a nota da avaliação semestral: '))
n3 = float(input('Digite a nota do exame final: '))
media = ((n1 * 2) + (n2 * 3) + (n3 * 5))/ 10
if (0 < n1 <= 10) and (0 < n2 <= 10) and (0 < n3 <= 10):
    if (0 < media < 3):
        print(f'O aluno teve a média de {media:.2f} e foi reprovado!')
    elif (3 < media < 5):
        print(f'O aluno teve a média de {media:.2f} e está de recuperação!')
    else:
        print(f'O aluno teve a média de {media:.2f} e foi aprovado!')
else:
    print('Dados inválidos!')