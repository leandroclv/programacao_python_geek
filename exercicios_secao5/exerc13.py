n1 = float(input('Digite a 1° nota do aluno: '))
n2 = float(input('Digite a 2° nota do aluno: '))
n3 = float(input('Digite a 3° nota do aluno: '))
media = ((n1 * 1) + (n2 * 1) + (n3 * 2))/ 4
if media >= 6:
    print(f'O aluno tirou uma média de {media:.2f} igual ou acima de 6 e foi aprovado.')
else:
    print(f'O aluno tirou uma média de {media:.2f} inferior a 6 e foi reprovado.')
